# Skin-Con: Skin Condition Classifier for Dark Skin Tones

**Skin-Con** is a FastAPI-based application that serves a fine-tuned EfficientNet model designed to classify skin conditions, with a focus on dark skin tones. This project aims to provide a more inclusive tool for skin condition diagnosis.

## Features

- **EfficientNet Model**: Utilizes a fine-tuned EfficientNet architecture for accurate image classification.
- **FastAPI Integration**: Provides a high-performance API for serving the model.
- **Targeted Dataset**: Focuses on skin conditions prevalent in individuals with dark skin tones.
- **Modular Structure**: Organized codebase with separate directories for application logic, model training, and testing.

## Project Structure

```
skin-con/
├── app/                # FastAPI application code
│   ├── main.py         # Entry point for the API
│   └── utils.py        # Utility functions
├── model/              # Saved model weights and architecture
├── test_images/        # Sample images for testing the model
├── training/           # Scripts and notebooks for training the model
├── requirement.txt     # Python dependencies
└── README.md           # Project documentation
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Muyiiwaa/skin-con.git
   cd skin-con
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

## Usage

1. **Start the FastAPI server**
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API documentation**

   Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to interact with the API using the automatically generated Swagger UI.

3. **Classify a skin condition**

   Use the `/predict` endpoint to upload an image and receive a classification result.
