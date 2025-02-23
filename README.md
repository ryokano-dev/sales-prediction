# Sales Prediction Project

A machine learning project to predict sales using AWS and Python.

## Tech Stack
- **Python**: pandas, scikit-learn, boto3
- **AWS**: S3, SageMaker (planned)
- **Tools**: Git, VS Code, PowerShell

## Progress
- Data acquisition and preprocessing script (`src/preprocess.py`).
- Uploaded cleaned data to AWS S3 (`src/upload_to_s3.py`).

## Next Steps
- Build and train a regression model with scikit-learn.
- Integrate AWS SageMaker for cloud-based training.
- Visualize predictions with Matplotlib.

## Setup Instructions
1. Clone the repo: `git clone https://github.com/yourusername/sales-prediction.git`
2. Activate virtual environment: `.\ai_env\Scripts\activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run preprocessing: `python src/preprocess.py`

## Notes
- Dataset sourced from [Kaggle Retail Sales Dataset](https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset/code).
- Contributions and feedback welcome!