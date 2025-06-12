from fastapi import FastAPI,UploadFile,File, HTTPException, status
from pathlib import Path
import shutil
from utils import predict_image
from schema import SkinPredictionResponse
import uvicorn
import logfire
import os
from dotenv import load_dotenv
import time

# load the environment variable
load_dotenv()

LOGFIRE_TOKEN = os.getenv("LOGFIRE_WRITE_TOKEN")


app = FastAPI(
    version = "1.0.1",
    title ="Skin Condition"
)

# setup logfire for monitoring and logging
logfire.configure(token= LOGFIRE_TOKEN)
logfire.instrument_fastapi(app=app)

@app.get("/", tags= ["Root"])
async def root():
    return{"message":"Hi! Welcome to Skin Con app!!"}


@app.post(
    "/predict_skin/",
    tags=["Skin Condition Prediction"],
    response_model=SkinPredictionResponse,
    summary="Analyze skin conditions from facial images",
    response_description="Predicted skin condition with confidence probability"
)
async def predict_skin_condition(
    image_file: UploadFile = File(
        ...,
        title="Facial Image Upload",
        description="High-quality image of a face with dark skin tone (JPEG or PNG format)"
    )
) -> SkinPredictionResponse:
    """
    Analyze an uploaded facial image to detect skin conditions in individuals with dark skin tones.
    
    This endpoint performs sophisticated image analysis to identify:
    - Clear skin (no visible conditions)
    - Common skin conditions: vitiligo, keloids, boils, or eczema
    
    The prediction includes both the identified condition and a confidence probability score.
    
    ### Implementation Details:
    - Accepts standard image formats (JPEG/PNG)
    - Processes images temporarily in memory for security
    - Automatically cleans up temporary files
    - Provides detailed error logging
    
    ### Typical Use Cases:
    - Telemedicine applications
    - Dermatology screening tools
    - Skin health monitoring systems
    
    ### Args:
        image_file: Uploaded image file containing a facial photograph. 
                   Should be well-lit and clearly show the skin area of interest.
    
    ### Returns:
        SkinPredictionResponse: Structured response containing:
            - skin_condition: Predicted condition (string)
            - probability: Confidence score (float between 0-1)
    
    ### Raises:
        HTTPException: 500 if processing fails with detailed error information
    
    ### Example:
        >>> import requests
        >>> files = {'image_file': open('patient_face.jpg', 'rb')}
        >>> response = requests.post('http://api/predict/', files=files)
        >>> print(response.json())
        {"skin_condition": "eczema", "probability": 0.873}
    """
    # Create secure temporary file path with timestamp to prevent collisions
    temp_file = Path(f"temp_{int(time.time())}_{image_file.filename}")
    
    try:
        # Safely write uploaded file to temporary location
        with temp_file.open(mode="wb") as file_buffer:
            shutil.copyfileobj(image_file.file, file_buffer)
        
        # Perform the core prediction logic
        confidence, predicted_condition = predict_image(temp_file)
        
        # Clean up temporary file immediately after use
        temp_file.unlink(missing_ok=True)
        
        # Format and log results
        confidence_score = round(confidence, 3)
        logfire.info(
            "Successful skin condition prediction",
            condition=predicted_condition,
            confidence=confidence_score,
            original_filename=image_file.filename
        )
        
        return SkinPredictionResponse(
            skin_condition=predicted_condition,
            probability=confidence_score
        )
        
    except Exception as error:
        logfire.error(
            "Skin condition prediction failed",
            error=str(error),
            filename=image_file.filename,
            stack_info=True
        )
        #delete the file
        temp_file.unlink(missing_ok=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "message": "Skin condition analysis failed",
                "error": str(error),
                "filename": image_file.filename
            }
        )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload = True)
