# 🏥 Health Insurance Cost Prediction

An end-to-end Machine Learning project designed to predict medical insurance charges based on patient health and demographic information.

This project demonstrates a complete ML workflow:

* Data loading and analysis
* Exploratory Data Analysis (EDA)
* Data preprocessing
* Regression model training
* Hyperparameter tuning
* Model evaluation and interpretation
* Model export with Joblib
* Interactive Streamlit web application

---

# 📌 Project Objective

An insurance company wants to estimate medical insurance costs more accurately in order to:

* anticipate healthcare expenses,
* improve pricing transparency,
* optimize insurance policies,
* better understand risk factors.

The AI system predicts medical charges using patient-related information such as:

* Age
* Sex
* BMI
* Number of children
* Smoking habits
* Geographic region

---

# 📂 Dataset

The dataset contains historical insurance records with the following columns:

| Feature  | Description                                 |
| -------- | ------------------------------------------- |
| age      | Age of the insured person                   |
| sex      | Gender                                      |
| bmi      | Body Mass Index                             |
| children | Number of dependent children                |
| smoker   | Smoking habit                               |
| region   | Geographic region                           |
| charges  | Medical insurance charges (target variable) |

Dataset size:

* 1338 rows
* 7 columns

---

# 🧠 Machine Learning Workflow

## 1. Data Loading

The dataset was loaded using Pandas.

Tasks completed:

* CSV loading
* Structure inspection
* Data type verification

Libraries used:

* Pandas

---

## 2. Exploratory Data Analysis (EDA)

Performed analyses:

* Descriptive statistics
* Missing values analysis
* Duplicate detection
* Numerical distributions
* Correlation analysis
* Outlier visualization

Visualizations created:

* Histograms
* Boxplots
* Scatterplots
* Correlation heatmaps

Main insights discovered:

* Smoking status strongly impacts insurance charges
* BMI and age moderately influence charges
* Region has limited impact
* Medical charges are highly right-skewed
* High-cost patients behave like outliers

Libraries used:

* Matplotlib
* Seaborn

---

# ⚙️ Data Preprocessing

The preprocessing pipeline was implemented using Scikit-learn.

Steps performed:

* Duplicate removal
* Train/Test split (80/20)
* OneHotEncoding for categorical variables
* StandardScaler for numerical variables
* Preprocessing pipelines

Categorical Features:

* sex
* smoker
* region

Numerical Features:

* age
* bmi
* children

---

# 🤖 Regression Models

Several regression models were trained and compared.

Models used:

* Linear Regression
* Random Forest Regressor
* SVR
* XGBoost Regressor

Evaluation metrics:

* RMSE
* MAE
* R² Score

---

# 📊 Baseline Model Results

| Model             | RMSE   | MAE   | R²      |
| ----------------- | ------ | ----- | ------- |
| Linear Regression | ~5956  | ~4177 | ~0.807  |
| Random Forest     | ~4679  | ~2584 | ~0.881  |
| SVR               | ~14425 | ~9260 | ~-0.132 |
| XGBoost           | ~5059  | ~2857 | ~0.861  |

Observation:

* Random Forest and XGBoost performed significantly better than Linear Regression and SVR.

---

# 🔥 Hyperparameter Tuning

GridSearchCV with 5-fold cross-validation was used to optimize:

* Random Forest
* XGBoost

Tuned parameters included:

## Random Forest

* n_estimators
* max_depth
* min_samples_split

## XGBoost

* learning_rate
* max_depth
* n_estimators
* subsample

---

# 🏆 Final Model Performance

The final selected model was:

# ✅ Tuned XGBoost Regressor

Final metrics:

| Metric | Value  |
| ------ | ------ |
| RMSE   | ~4766  |
| MAE    | ~2528  |
| R²     | ~0.893 |

This means the model explains approximately:

* 89% of the variance in insurance charges.

---

# 📈 Model Evaluation

Evaluation visualizations included:

* Predicted vs Actual values
* Residual distribution
* Residual scatterplots
* Feature importance analysis

Main findings:

* Predictions are globally accurate
* Most residuals are centered around zero
* High-cost patients remain harder to predict
* Smoking status dominates feature importance

---

# 🌳 Feature Importance

The trained XGBoost model identified the following important factors:

| Feature        | Importance |
| -------------- | ---------- |
| Smoking Status | Very High  |
| BMI            | Moderate   |
| Age            | Moderate   |
| Children       | Low        |
| Region         | Very Low   |

Key business insight:

> Smoking behavior is the strongest driver of insurance costs.

---

# 💾 Model Export

The final trained model was exported using Joblib.

Exported file:

```bash
models/health_insurance_xgboost_model.joblib
```

This allows the model to be:

* reused,
* deployed,
* integrated into applications.

---

# 🖥️ Streamlit Application

An interactive Streamlit web application was developed.

Features:

* User-friendly interface
* Real-time insurance cost prediction
* Dynamic patient inputs
* AI-powered estimation

Inputs available:

* Age
* Sex
* BMI
* Number of children
* Smoker status
* Region

---

# 🚀 Installation

## Clone the repository

```bash
git clone https://github.com/Laraibi/health-insurance-cost-prediction.git
```

## Navigate into the project

```bash
cd health-insurance-cost-prediction
```

## Install dependencies using uv

```bash
uv sync
```

---

# ▶️ Run the Streamlit App

```bash
uv run streamlit run app/app.py
```

---

# 📁 Project Structure

```bash
health-insurance-cost-prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── assurance-maladie.csv
│
├── models/
│   └── health_insurance_xgboost_model.joblib
│
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_regression_models.ipynb
│   ├── 03_hyperparameter_tuning.ipynb
│   ├── 04_model_evaluation.ipynb
│   ├── 05_feature_importance.ipynb
│   └── 06_model_export.ipynb
│
├── reports/
│
├── src/
│   ├── eda.py
│   ├── load_data.py
│   └── visualization.py
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn

## Machine Learning

* Scikit-learn
* XGBoost

## Deployment/UI

* Streamlit

## Environment Management

* uv

---

# 📚 Learning Outcomes

This project helped practice:

* Data Analysis
* Machine Learning workflows
* Feature engineering
* Regression modeling
* Hyperparameter tuning
* Pipeline engineering
* Model evaluation
* Model deployment
* Interactive AI applications

---

# 🔮 Future Improvements

Possible future enhancements:

* SHAP explainability
* Target log transformation
* Model monitoring
* Cloud deployment
* Docker containerization
* CI/CD pipeline
* API version with FastAPI
* Authentication system
* Insurance risk categorization

---

# 👨‍💻 Author

Mehdi Laraibi

* Full Stack Developer
* Machine Learning Enthusiast
* AI & SaaS Builder

GitHub:

[https://github.com/Laraibi](https://github.com/Laraibi)

LinkedIn:

[https://www.linkedin.com/in/mehdi-laraibi-33703ab6](https://www.linkedin.com/in/mehdi-laraibi-33703ab6)
