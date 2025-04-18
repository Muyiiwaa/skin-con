from fastapi import FastAPI,UploadFile,File
from pathlib import Path
import shutil
from utils import predict_image
from schema import SkinPredictionResponse


app = FastAPI(
    version = "1.0.1",
    title ="Skin Condition"
)

@app.get("/", tags= ["Root"])
async def root():
    return{"message":"Welcome, we are alive"}


@app.post("/predict/", tags=["Skin Prediction"],
          response_model=SkinPredictionResponse)
async def predict(file:UploadFile = File(...)) -> SkinPredictionResponse:
    """_This endpoint accepts images of a face of a person with dark skin tone and 
    detects whether they have a clear skin or any of the four skin conditions ranging
    from vitiligo, kelloids, boil, eszema._

    Args:
        file (UploadFile, optional): _Upload an image file of the type jpeg or png._. Defaults to File(...).

    Returns:
        SkinPredictionResponse: _The skin condition prediction and the probability associated 
        with the predicted class._
    """
    temp_file = Path(f"temp_{file.filename}")
    with temp_file.open(mode="wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
    # Prediction 
    prob,preds = predict_image(temp_file)
    
    #delete the file after use 
    temp_file.unlink()
    
    return SkinPredictionResponse(
        skin_condition=preds,
        probability= round(prob, 3))