# Data and Ethical Documentation

## Dataset Source

This project uses the ARMD-UTSW antimicrobial resistance microbiology dataset.

The dataset is de-identified and contains microbiology culture and
antimicrobial susceptibility information together with selected demographic
and temporal variables.

## Privacy

The dataset does not contain directly identifying patient information.

Patient and encounter identifiers are anonymized and are used only for
data organization, grouping, and patient-level data splitting.

They are not used as predictive features.

## De-identification

The dataset contains privacy-preserving transformations.

Age is provided in age groups rather than exact ages.

Gender is represented using anonymized codes. The meaning of the codes is not
assumed or inferred.

Dates and times have been jittered for privacy while preserving relevant
temporal relationships.

## Target Definition

The prediction target is antimicrobial resistance:

- Susceptible = 0
- Resistant = 1

Intermediate, inconclusive, and missing susceptibility results are excluded
from the primary modeling dataset.

## Data Quality

The raw microbiology dataset contains multiple records for a single culture
order because a culture can contain multiple organisms and antibiotic
susceptibility results.

Therefore, one raw row is not necessarily equivalent to one patient or one
culture.

The analytical grain is:

Patient → Culture Order → Organism → Antibiotic → Susceptibility Outcome

## Leakage Prevention

The final susceptibility result is the target and must not be used as a
predictor.

Patient identifiers are excluded from predictive features.

Patient-level splitting is used to reduce the possibility of records from the
same patient appearing in both training and evaluation datasets.

## Limitations

The dataset does not contain every clinical variable that could potentially
be useful for AMR prediction.

For example, the available project data does not provide complete information
about prior antibiotic exposure, symptoms, or all laboratory measurements.

Some microbiology variables may also become available during the laboratory
workflow rather than before susceptibility testing.

Therefore, the exact clinical prediction point must be considered when
interpreting model results.

## Ethical Use

This project is intended for educational, analytical, and portfolio purposes.

The model is not a clinical decision-support system and should not be used to
select antibiotics, diagnose patients, or make treatment decisions.

Model associations should not be interpreted as evidence of causation.

## Reproducibility

The project uses a reproducible Python environment and a fixed random state
where appropriate.

The project includes reusable preprocessing, model, prediction, and
documentation components.

## Responsible Interpretation

Model performance should be interpreted together with:

- Class imbalance
- Precision and recall
- Sensitivity and specificity
- ROC-AUC
- PR-AUC
- Calibration
- Error analysis
- Temporal validation
- External validation where available

A model with strong performance on this dataset would not automatically be
expected to perform similarly in another hospital or population.