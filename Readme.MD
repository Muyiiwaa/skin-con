# Skin Condition Prediction API

This project is a FastAPI-based application that uses a pre-trained PyTorch model to predict skin conditions from uploaded images.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Running the Application](#running-the-application)
  - [Locally](#locally)
  - [Using Docker](#using-docker)
- [API Endpoint](#api-endpoint)
  - [`POST /predict/`](#post-predict)
- [Environment Variables](#environment-variables)
- [Model Information](#model-information)
- [Contributing](#contributing)

## Project Overview

The application provides an API endpoint where users can upload an image of a skin condition. The backend processes this image using a deep learning model and returns a prediction.

## Features

-   FastAPI backend for high performance.
-   Image processing and prediction using a PyTorch model.
-   Dockerized for easy deployment and scalability.
-   Simple API endpoint for image uploads and predictions.

## Project Structure

```
skin-con/
├── .env                # Environment variables (create this file based on .env.example or requirements)
├── .gitignore          # Specifies intentionally untracked files
├── Dockerfile          # Instructions to build the Docker image
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── app/                # FastAPI application code
│   ├── main.py         # API endpoint definitions and application logic
│   ├── schema.py       # Pydantic models for request/response validation
│   └── utils.py        # Utility functions, including image prediction logic
├── model/              # Saved model weights and architecture
│   └── skin_model.pth  # Pre-trained PyTorch model file
├── test_images/        # Sample images for testing the model
└── training/           # Scripts and notebooks for training the model (if applicable)
    └── Skin_condition.ipynb # Jupyter notebook for model training/exploration
```

## Prerequisites

-   Python 3.12 (as specified in Dockerfile, though other 3.x versions might work with adjustments)
-   pip (Python package installer)
-   Docker (if using Docker-based setup)

## Setup and Installation

### Local Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repository-url>
    cd skin-con
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the project root directory. If your application uses Logfire or other services requiring API keys, add them here. For example:
    ```env
    # .env
    LOGFIRE_WRITE_TOKEN="your_logfire_write_token_here"
    # Add other environment variables as needed
    ```

### Docker Setup

1.  **Build the Docker image:**
    Ensure Docker is running. In the project root directory, run:
    ```bash
    docker build -t skin_con:v2 .
    ```
    This will create a Docker image named `skin_con` with the tag `v2`.

## Running the Application

### Locally

1.  **Ensure your virtual environment is activated and dependencies are installed.**
2.  **Navigate to the project root directory.**
3.  **Run the FastAPI application using Uvicorn:**
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The `--reload` flag enables auto-reloading when code changes, which is useful for development.

The application will be accessible at `http://localhost:8000` or `http://0.0.0.0:8000`.
The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

### Using Docker

1.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 --env-file .env skin_con:v2
    ```
    -   `-p 8000:8000`: Maps port 8000 of the container to port 8000 on your host machine.
    -   `--env-file .env`: Loads environment variables from the `.env` file into the container. Make sure your `.env` file is correctly formatted and `LOGFIRE_WRITE_TOKEN` (and any other necessary variables) are present if needed.
    -   `skin_con:v2`: The name and tag of the Docker image to run.

    If you prefer to pass environment variables directly (e.g., for `LOGFIRE_WRITE_TOKEN`):
    ```bash
    docker run -p 8000:8000 -e LOGFIRE_WRITE_TOKEN="your_actual_token_value" skin_con:v2
    ```

The application will be accessible at `http://localhost:8000`.
The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## API Endpoint

### `POST /predict/`

Upload an image file to get a skin condition prediction.

-   **Method:** `POST`
-   **URL:** `/predict/`
-   **Request Body:** `multipart/form-data`
    -   `file`: The image file to be analyzed (e.g., JPEG, PNG).
-   **Success Response (200 OK):**
    ```json
    {
        "filename": "uploaded_image.jpg",
        "content_type": "image/jpeg",
        "prediction": "Predicted Condition", // Example: "Eczema"
        "confidence": 0.85 // Example: 85% confidence
    }
    ```
    (Note: The actual structure of `prediction` and `confidence` depends on the implementation in `app/utils.py` and `app/schema.py`.)
-   **Error Responses:**
    -   `400 Bad Request`: If the file is not an image or other validation fails.
    -   `422 Unprocessable Entity`: If the uploaded file is not a valid image format that can be processed.
    -   `500 Internal Server Error`: If there's an issue during model prediction.

**Example using `curl`:**
```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8000/predict/
```
Replace `/path/to/your/image.jpg` with the actual path to an image file. You can use images from the `test_images/` directory.

## Environment Variables

The application may use the following environment variables. Create a `.env` file in the project root to configure them:

-   `LOGFIRE_WRITE_TOKEN`: Your write token for the Logfire service (if integrated).
-   *(Add any other environment variables your application might require)*

## Model Information

-   **Model Type:** PyTorch
-   **Model File:** `model/skin_model.pth`
-   **Details:** The model is trained to classify skin conditions based on input images. Specific details about the architecture, classes, and training data can be found in the `training/Skin_condition.ipynb` notebook or related documentation.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to any existing style guidelines and includes tests where appropriate.
```// filepath: /workspaces/skin-con/README.md
# Skin Condition Prediction API

This project is a FastAPI-based application that uses a pre-trained PyTorch model to predict skin conditions from uploaded images.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
  - [Local Setup](#local-setup)
  - [Docker Setup](#docker-setup)
- [Running the Application](#running-the-application)
  - [Locally](#locally)
  - [Using Docker](#using-docker)
- [API Endpoint](#api-endpoint)
  - [`POST /predict/`](#post-predict)
- [Environment Variables](#environment-variables)
- [Model Information](#model-information)
- [Contributing](#contributing)

## Project Overview

The application provides an API endpoint where users can upload an image of a skin condition. The backend processes this image using a deep learning model and returns a prediction.

## Features

-   FastAPI backend for high performance.
-   Image processing and prediction using a PyTorch model.
-   Dockerized for easy deployment and scalability.
-   Simple API endpoint for image uploads and predictions.

## Project Structure

```
skin-con/
├── .env                # Environment variables (create this file based on .env.example or requirements)
├── .gitignore          # Specifies intentionally untracked files
├── Dockerfile          # Instructions to build the Docker image
├── README.md           # This file
├── requirements.txt    # Python dependencies
├── app/                # FastAPI application code
│   ├── main.py         # API endpoint definitions and application logic
│   ├── schema.py       # Pydantic models for request/response validation
│   └── utils.py        # Utility functions, including image prediction logic
├── model/              # Saved model weights and architecture
│   └── skin_model.pth  # Pre-trained PyTorch model file
├── test_images/        # Sample images for testing the model
└── training/           # Scripts and notebooks for training the model (if applicable)
    └── Skin_condition.ipynb # Jupyter notebook for model training/exploration
```

## Prerequisites

-   Python 3.12 (as specified in Dockerfile, though other 3.x versions might work with adjustments)
-   pip (Python package installer)
-   Docker (if using Docker-based setup)

## Setup and Installation

### Local Setup

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <your-repository-url>
    cd skin-con
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the project root directory. If your application uses Logfire or other services requiring API keys, add them here. For example:
    ```env
    # .env
    LOGFIRE_WRITE_TOKEN="your_logfire_write_token_here"
    # Add other environment variables as needed
    ```

### Docker Setup

1.  **Build the Docker image:**
    Ensure Docker is running. In the project root directory, run:
    ```bash
    docker build -t skin_con:v2 .
    ```
    This will create a Docker image named `skin_con` with the tag `v2`.

## Running the Application

### Locally

1.  **Ensure your virtual environment is activated and dependencies are installed.**
2.  **Navigate to the project root directory.**
3.  **Run the FastAPI application using Uvicorn:**
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The `--reload` flag enables auto-reloading when code changes, which is useful for development.

The application will be accessible at `http://localhost:8000` or `http://0.0.0.0:8000`.
The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

### Using Docker

1.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 --env-file .env skin_con:v2
    ```
    -   `-p 8000:8000`: Maps port 8000 of the container to port 8000 on your host machine.
    -   `--env-file .env`: Loads environment variables from the `.env` file into the container. Make sure your `.env` file is correctly formatted and `LOGFIRE_WRITE_TOKEN` (and any other necessary variables) are present if needed.
    -   `skin_con:v2`: The name and tag of the Docker image to run.

    If you prefer to pass environment variables directly (e.g., for `LOGFIRE_WRITE_TOKEN`):
    ```bash
    docker run -p 8000:8000 -e LOGFIRE_WRITE_TOKEN="your_actual_token_value" skin_con:v2
    ```

The application will be accessible at `http://localhost:8000`.
The API documentation (Swagger UI) will be available at `http://localhost:8000/docs`.

## API Endpoint

### `POST /predict/`

Upload an image file to get a skin condition prediction.

-   **Method:** `POST`
-   **URL:** `/predict/`
-   **Request Body:** `multipart/form-data`
    -   `file`: The image file to be analyzed (e.g., JPEG, PNG).
-   **Success Response (200 OK):**
    ```json
    {
        "filename": "uploaded_image.jpg",
        "content_type": "image/jpeg",
        "prediction": "Predicted Condition", // Example: "Eczema"
        "confidence": 0.85 // Example: 85% confidence
    }
    ```
    (Note: The actual structure of `prediction` and `confidence` depends on the implementation in `app/utils.py` and `app/schema.py`.)
-   **Error Responses:**
    -   `400 Bad Request`: If the file is not an image or other validation fails.
    -   `422 Unprocessable Entity`: If the uploaded file is not a valid image format that can be processed.
    -   `500 Internal Server Error`: If there's an issue during model prediction.

**Example using `curl`:**
```bash
curl -X POST -F "file=@/path/to/your/image.jpg" http://localhost:8000/predict/
```
Replace `/path/to/your/image.jpg` with the actual path to an image file. You can use images from the `test_images/` directory.

## Environment Variables

The application may use the following environment variables. Create a `.env` file in the project root to configure them:

-   `LOGFIRE_WRITE_TOKEN`: Your write token for the Logfire service (if integrated).
-   *(Add any other environment variables your application might require)*

## Model Information

-   **Model Type:** PyTorch
-   **Model File:** `model/skin_model.pth`
-   **Details:** The model is trained to classify skin conditions based on input images. Specific details about the architecture, classes, and training data can be found in the `training/Skin_condition.ipynb` notebook or related documentation.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

Please ensure your code adheres to any existing style guidelines and includes tests