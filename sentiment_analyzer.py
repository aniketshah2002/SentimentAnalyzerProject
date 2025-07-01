#Step 1: Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


#data loading and preparation 
#step 2: loading of the dataset
# i'll be using pandas to read the CSV file
print("Loading Dataset...")
df = pd.read_csv('IMDB Dataset.csv')

#for faster testing, i'll use a smaller sample of the data.
df = df.sample(n=10000, random_state=42)

print("Dataset loaded. Here's a quick look:")
print(df.head())

#step 3: preparing the data 
# for this we need to seperate our data into two parts:
# X: the 'review' text (the input to our model)
# y: the 'sentiment' (the output our model will predict)
X = df['review']
y = df['sentiment']

print("\nData Prepared into features (X) and labels (y).")

#Feature Extraction
#Step 4: Converting text data into numerical features
#Machine learning models don't understand words, they only understand numbers.
#TfidVectorizer converts text into a matrix of numbers.
#It gives more weight to words that are important for distinguishing between sentiments.

print("Vectorizing text data...")
vectorizer = TfidfVectorizer(max_features=5000) #I'll be considering only the top 5000 words
X_vectorized = vectorizer.fit_transform(X)

print("Text data converted to numerical vectors.")

# Model Training 
#Step 5: Spiltting data into training and testing sets
# I'll train model on 80% of the data and test its performance on the remaining 20%.
# This ensures we're testing the model on data it has never seen before.
print("Splitting data into training and testing sets...")
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

# Step 6: Creating and training the model
# I'll be using Logistic Regression, a simple yet powerful classification algorithm.
# The .fit() method is where the model "learns" from the training data.
print("Training the model...")
model = LogisticRegression()
model.fit(X_train, y_train)

print("Model training complete.")

#Model Evaluation
#step 7: Make prediction on the test set
print("making predictions on the test data...")
y_pred = model.predict(X_test)

# Step 8: Evaluate the model's performance
# We compare the model's predictions (y_pred) with the actual sentiments (y_test).
accuracy = accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))

# Testing with new reviews
#Step 9 : Test the model with your own reviews
print("\n--- Testing with new reviews --")
new_reviews = [
    "This movie was fantastic! The acting was superb and the plot was thrilling.",
    "A complete waste of time. The plot was predicatble and the acting was terrible.",
    "It was an okay movie, not great but not bad either.",
    "Well I am unsure what to say about this movie, kind of one time watch."
]

# We need to transform these new reviews using the same vectorizer we used for training.
new_reviews_vectorized = vectorizer.transform(new_reviews)

# Make Predictions
predictions = model.predict(new_reviews_vectorized)

for review, prediction in zip(new_reviews, predictions):
    print(f"\nReview: '{review}'")
    print(f"Predicted Sentiment: {prediction}")
