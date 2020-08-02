# Algorithms-and-Digital-Marketing


### Assignment 3 - Recommendation System

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
| Priyanka Malpekar |   001302741     |
|   Jui Ashinkar    |   001443824     |

#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=1M6xhA8zgyiUENIBwdv9W5Z5ya89shhp1Ha27zDs31uU#0

### Objectives

![Untitled Diagram (2) (1)](https://user-images.githubusercontent.com/59594174/89115596-1c95a080-d458-11ea-9af4-5f11cff66b15.jpg)

Who- For a custom snack shipping company called Universal Yums, which only has an online presence and wants to differentiate themselves with their superior recommendation system

What- To prototype, build, evaluate and deploy a recommendation system

Why- To upgrade their recommendation system to speed up searches which will make it easier for the users to access snacks they are interested in. Also, it will help the company to provide personalized offers and enhance customer experience.

When -Over a 2 weeks period timeline.

Where -This project will be delivered to the company Universal Yums.

How- To implement machine learning Models and use technologies like Streamlit, FastAPI, Flask, JMeter

## Machine Learning Models

## Bayesian Personalized Ranking
Matrix factorization algorithm for predicting item ranking with implicit feedback

![BPR Workflow](https://user-images.githubusercontent.com/59594174/89115615-74cca280-d458-11ea-9b2b-51b377af686e.jpg)

### Introduction
1. User Feedback are drawn from different channels.
Eg: clicks, likes, listens, follows, purchases, comments etc

2. We propose BPR algorithm to exploit different types of feedback.

3. The available observations are only positive feedback where the non-observed ones are a mixture of real negative feedback and missing values.

### How it Works?
1. When doing matrix factorization for implicit feedback data (users' clicks, view times), we start with a user-item matrix R where R is nonzero elements of the matrix and U are the user's interaction with the items.

R=U×V

2. Matrix factorization assumes that: Each user can be described by d features.

3. For example, feature 1 might be referring to how much each user likes Indian Snacks. Each item, snacks in this case, can be described by an analogous set of d features. To correspond to the above example, feature 1 for the snack might be a number that says how close the snack is to a Indian Snack.

### Formulation

1. Suppose ‘u' is the set of all the users and ‘i' is the set of all the items
2. Our goal is to provide ‘u' with personalized ranking denoted by > u
3. The usual approach of this item recommendation algorithm is to predict a personalized score for an item that reflects the user's preference for that item
4. Then the items are ranked by sorting them according to that score and the TOP N is recommended to the user
5. If the user has interacted with item i i.e. (u,i) ∈ S, then we assume that the user prefers this item over all other non-observed items
6. In the figure below, user u1 has interacted with item i2 but not item i1, so we assume that this user prefers item i2 over i1
7. And, we will denote this generally by i > j where i stands for positive item and j stands for negative item
8. For items that the user has both interacted with, we cannot infer any preference. The same is true for two items that a user has not interacted yet

## Singular Value Decomposition (SVD)

1. Surprise Singular Value Decomposition (SVD) model is a collaborative filtering algorithm that can be used for training a matrix factorization model, which predicts explicit or implicit ratings of users on items for recommendations.
2. SVD algorithm was specifically designed to predict ratings as close as possible to their actual values.
3. SVD mainly functions with two variables: user and the item. Depending upon the item's rated by user SVD will make the recommendation for the next time
4. It works by searching a large group of people and finding a smaller set of users with tastes similar to a particular user. It looks at the items they like and combines them to create a ranked list of suggestions.

### Steps Involved in implementing the algorithm:

1. Singular value decomposition (SVD) is one of the most popular algorithms to factorize a matrix
2. First step is to find similar users or items
3. The second step is to predict the ratings of the items that are not yet rated by a user
4. The similarity is calculated based on the ratings of similar users
5. The Surprise is a Python SciKit that comes with various recommender algorithms and similarity metrics to make it easy to build and analyze recommenders
6. Surprise supports data frames as long as they have three columns representing the user ids, item ids, and the ratings (in this order)
7. We start by splitting our data into the train set and test set with the python_random_split function
8. We can call predict to get some predictions. Predict returns an internal object Prediction which can be easily converted back to a data frame

![Recommendation Systems](https://user-images.githubusercontent.com/59594174/89115681-194ee480-d459-11ea-865a-791d4a3b2db3.png)

## Fast API

Fast API - BPR

![BPR_85_101_FastAPI](https://user-images.githubusercontent.com/59594174/89115696-4ac7b000-d459-11ea-86d4-052118c196c9.PNG)

Fast API - SVD

![FastAPI_SVD](https://user-images.githubusercontent.com/59594174/89115699-4e5b3700-d459-11ea-800e-c7a9308892e4.PNG)


## Flask - BPR Method

![Flask](https://user-images.githubusercontent.com/59594174/89115725-895d6a80-d459-11ea-85b9-2ee071d86169.PNG)

Validation

![Validation](https://user-images.githubusercontent.com/59594174/89115729-90847880-d459-11ea-86f2-8239e25ec0a4.PNG)


## Streamlit - SVD Method

![Streamlit](https://user-images.githubusercontent.com/59594174/89115746-bd389000-d459-11ea-9f0c-a05321407e44.PNG)

## Jmeter

### BPR

![Jmeter_85_3_ResponseGraph](https://user-images.githubusercontent.com/59594174/89115766-f6710000-d459-11ea-8959-8001ffa8f818.PNG)

### SVD

![Jmeter_41_2_ResponseGraph](https://user-images.githubusercontent.com/59594174/89115817-ac3c4e80-d45a-11ea-8015-39447f702a1f.PNG)

## Load Testing

### BPR
Response Time for 500 Users per second

![Jmeter_500](https://user-images.githubusercontent.com/59594174/89115838-e6a5eb80-d45a-11ea-8a79-40dd280a1e85.PNG)

Response Time for 1000 Users per second

![Jmeter_1000](https://user-images.githubusercontent.com/59594174/89115839-e6a5eb80-d45a-11ea-917b-d440eec2900a.PNG)

### SVD
Response Time for 500 Users per second

![WhatsApp Image 2020-07-31 at 20 50 28](https://user-images.githubusercontent.com/59594174/89115876-587e3500-d45b-11ea-9a93-0e7dee0209a2.jpeg)

Response Time for 1000 Users per second

![WhatsApp Image 2020-07-31 at 20 50 28 (1)](https://user-images.githubusercontent.com/59594174/89115881-6338ca00-d45b-11ea-877e-403bd2143d11.jpeg)


## Jmeter Dashboard

![Dashboard](https://user-images.githubusercontent.com/59594174/89115851-0806d780-d45b-11ea-9dfc-000b763aa9f3.PNG)









