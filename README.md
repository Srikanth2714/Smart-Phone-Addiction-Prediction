# 📱 Smart Phone Addiction Prediction

This project predicts smartphone addiction levels using machine learning techniques.  
By analyzing user data, it helps individuals understand and manage their digital usage patterns effectively.

---

## 🚀 Features

- **Data Preprocessing**: Cleans and balances the dataset to improve model accuracy.
- **Model Training**: Applies multiple machine learning algorithms for classification.
- **Web Application**: Provides an interactive Flask app for end users to get predictions.
- **Visualization & Analysis**: Jupyter Notebook contains detailed exploratory data analysis (EDA) and model evaluation.

---

## 🗂️ Project Structure

- `smart-phone-dataset.csv`: Raw dataset with user responses.
- `balanced_dataset.csv`: Processed and balanced version of the dataset.
- `Smart_Phone.ipynb`: Jupyter Notebook with EDA and ML modeling.
- `app.py`: Streamlit-based web app for smartphone addiction prediction.
- `multiple_models.pkl`: Saved machine learning models.
- `users.pkl`: Stores user input and prediction logs.
- `requirements.txt`: Required Python packages.

---

## 🛠️ Installation

1. Clone the repository: `git clone https://github.com/Srikanth2714/Smart-Phone-Addiction-Prediction.git && cd Smart-Phone-Addiction-Prediction`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app/streamlit_app.py`

## ▶️ Usage

1. Open the Streamlit app in your browser.
2. Input details such as screen time, app usage patterns, and self-reported habits.
3. Click the **"Predict"** button to get the predicted level of smartphone addiction.

## 🧰 Technologies Used

- **Python**:For data preprocessing, model training, and application logic.
- **Scikit-learn**: For building and training machine learning models.
- **Pandas**: For data loading, cleaning, and manipulation.
- **Streamlit**: To build the interactive and user-friendly web application.
- **Jupyter Notebook**: For exploratory data analysis, preprocessing, and model development.
