# Model Card — Healthcare Antimicrobial Resistance Prediction

## 1. Model Overview

This project develops a machine-learning model for predicting an antimicrobial
resistance (AMR) outcome from microbiological and patient/culture information.

The primary prediction target is:

- 0 = Susceptible
- 1 = Resistant

Intermediate, inconclusive, and missing susceptibility records were excluded
from the modeling dataset.

## 2. Intended Use

The model is intended as a portfolio and research prototype for exploring
patterns associated with antimicrobial resistance.

It is not intended for:

- Clinical diagnosis
- Antibiotic prescribing
- Patient treatment decisions
- Emergency medical decision-making
- Direct deployment in a healthcare setting

## 3. Dataset

The project uses a de-identified microbiology dataset containing culture,
organism, antibiotic susceptibility, demographic, and temporal information.

The analytical dataset contains:

- 1,146,274 AMR records
- 949,098 susceptible records
- 197,176 resistant records
- 45,056 unique patients
- 86,136 culture orders
- 386 organisms
- 75 antibiotics

## 4. Features

The model uses the following feature groups:

### Categorical Features

- Age group
- Recorded gender code
- Ordering mode
- Culture description
- Organism
- Antibiotic
- Order month
- Order quarter
- Order day of week

### Numeric Features

- Order year

Categorical variables are encoded using one-hot encoding.

The numeric year feature is standardized.

## 5. Target Definition

AMR is defined as:

- Susceptible → AMR = 0
- Resistant → AMR = 1

Intermediate, inconclusive, and missing susceptibility results are excluded.

## 6. Model

The primary baseline model is Logistic Regression.

The model was trained using a sparse feature matrix containing 503 encoded
features.

A preprocessing pipeline was used to ensure that categorical encoding and
numeric preprocessing are applied consistently.

## 7. Data Splitting

Patient-level splitting was used to reduce the risk of having records from the
same patient appear in both training and evaluation datasets.

A fixed random state was used for reproducibility.

## 8. Class Distribution

The modeling dataset contains approximately:

- 82.83% Susceptible
- 17.17% Resistant

Because the classes are imbalanced, model performance should not be evaluated
using accuracy alone.

Relevant evaluation metrics include:

- Precision
- Recall
- Sensitivity
- Specificity
- ROC-AUC
- PR-AUC
- Calibration
- Confusion matrix

## 9. Data Leakage Considerations

Patient identifiers and other identifiers are not intended to be used as
predictive features.

The final susceptibility result is the prediction target and must not be
provided to the model as an input feature.

The prediction point must also be considered carefully because some
microbiology fields may only become available during the laboratory workflow.

## 10. Explainability

Model interpretation was explored using feature importance and SHAP-based
analysis.

These explanations describe model associations and contribution patterns.
They should not be interpreted as causal relationships.

## 11. Dataset Limitations

The dataset is de-identified.

Dates have been jittered for privacy while preserving relevant temporal
relationships.

Gender is represented using an anonymized code, and the mapping of the codes
should not be inferred.

The available dataset does not contain every potentially useful clinical
predictor, such as complete symptoms, laboratory measurements, or prior
antibiotic exposure.

## 12. Limitations of the Model

The model is a research and portfolio prototype.

Its predictions may not generalize to:

- Other hospitals
- Other geographic populations
- Different laboratory systems
- Different time periods
- Clinical populations outside the source dataset

Additional external and temporal validation would be required before any
real-world clinical application.

## 13. Ethical Considerations

The dataset is de-identified and was used for analytical and educational
purposes.

The model should not be used to make decisions about individual patients.

The project does not claim that the identified features cause antimicrobial
resistance.

## 14. Reproducibility

The project uses:

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- XGBoost
- SHAP
- Streamlit
- Power BI

A fixed random state is used where appropriate.

The trained prediction pipeline is saved as:

`models/amr_prediction_pipeline.joblib`

## 15. Project Status

This is a portfolio-level healthcare analytics and machine-learning prototype.

Further work includes comprehensive model evaluation, error analysis,
explainability analysis, documentation, and final portfolio presentation.