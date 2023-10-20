Customer Churn Prediction Model - Report
Introduction
This report outlines the process of creating a customer churn prediction model. The objective is to forecast whether a customer will leave or continue using a telecom service based on various features such as age, gender, location, subscription length, monthly bill, and total usage.

Exploratory Data Analysis (EDA)
The analysis began by investigating the dataset, which comprises 100,000 rows and 9 columns. The primary steps involved:

Data Overview
The dataset was loaded and its basic properties examined using Python libraries like Pandas. Data types for each column were identified, and checks for missing values were conducted. Descriptive statistics were computed. The dataset includes customer ID, name, age, gender, location, subscription length, monthly bill, total usage, and churn status (0 for retained, 1 for churned).

Data Cleaning
Data cleaning involved converting the "Total_Usage_GB" column to a numeric data type and ensuring no missing values existed.

Data Exploration
The data was visualized and analyzed to better comprehend the relationships between various features and the churn status. Count plots were used to explore how different factors such as gender, location, subscription length, and age groups influenced churn. Density plots were created to examine the distribution of monthly bills and total usage among churned and retained customers.

Model Building
For the prediction model, two machine learning algorithms were implemented - Decision Tree Classifier and Random Forest Classifier. To address class imbalance issues within the dataset, the Synthetic Minority Over-sampling Technique (SMOTE) was employed to balance the classes and enhance predictive performance.

Decision Tree Classifier
A Decision Tree Classifier was trained on the data. However, due to class imbalance, the model's accuracy proved unsatisfactory. Classification reports and confusion matrices were generated to assess its performance.

Random Forest Classifier
A Random Forest Classifier was trained similarly to the Decision Tree. SMOTE was used to address class imbalance, resulting in improved accuracy and precision. Classification reports and confusion matrices were used once more for evaluation.

Principal Component Analysis (PCA)
Principal Component Analysis (PCA) was conducted to reduce dimensionality while preserving predictive power. The reduced feature set was used to train a Random Forest Classifier.

Deployment
To deploy the trained Random Forest Classifier, a web application was created using Flask. Users can input customer data, including age, gender, location, subscription length, monthly bill, and total usage. The model predicts whether the customer will churn or not and displays the confidence level in the prediction.

Future Enhancements
In the future, the customer churn prediction model can be further enhanced to increase accuracy and utility. This can be achieved through advanced feature engineering to include additional customer-related data, exploration of more sophisticated machine learning algorithms, hyperparameter tuning, real-time data integration, customer segmentation for tailored retention strategies, feedback mechanisms for continuous learning, A/B testing for strategy evaluation, user interface improvements, continuous model monitoring, and integration with CRM systems for seamless action. These enhancements will ensure the model remains adaptive and effective in reducing churn and improving customer retention efforts.
