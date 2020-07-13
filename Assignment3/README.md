# Algorithms-and-Digital-Marketing


### Assignment 3 - Implementing Visual search

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
| Priyanka Malpekar |   001302741     |
|   Jui Ashinkar    |   001443824     |


#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=17eNMDqSmghdf-Fq4rKjazl2In8refahJ6sLwHXJ2_Ds

#### About Dataset

Our image dataset has been extracted from the full list of more than 40M products available at cdiscount.com in July, 2017.The dataset is organized according to a 3-level classification tree with categories labeled in French. So, to be precise there are 12,371,293 images for 7,069,896 products.

The information about this publicly released dataset can be found here:  https://www.kaggle.com/c/cdiscount-image-classification-challenge

####train.bson :
(Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format. This kernel provides an example of how to process the data.

###category_names.csv:
Shows the hierarchy of product classification. Each category_id has a corresponding level1, level2, and level3 name, in French. The category_id corresponds to the category tree down to its lowest level. This hierarchical data may be useful, but it is not necessary for building models and making predictions. All the absolutely necessary information is found in train.bson.

###train_example.bson:
Contains the first 100 records of train.bson so you can start exploring the data before downloading the entire set.


#### Objectives

Who- Marketa analytics has hired us as an Algorithmic marketing analysts. Marketa is a consulting organization specializing in Marketing analytical solutions. 

What- To analyze data and build analytical dashboards 
			
Why- To illustrate the value of data driven analytics and to derive meaningful insights to help their business

When- Over a 2 weeks period timeline 

Where- This project will be delivered to our client Instacart. Business Analyst, Pricing Specialist and Business Strategist can use these dashboards to make business decisions which will help Instacart maximize its sales

How- The company has a challenge using large scale datasets.
To use tools like XSV,Trifacta,Snowflake,Salesforce Einstein Analytics and Python. 


![Capture](https://user-images.githubusercontent.com/59594174/84547477-a1263700-acd1-11ea-835f-8240b9c5ac2e.PNG)



### Salesforce Dashboards

#### Onboarding Feature

![InstacartVideo](https://user-images.githubusercontent.com/59594174/84546697-e3e70f80-accf-11ea-9d4a-251c613fdc56.PNG)

#### Products Dashboard

![Products_Dashboard](https://user-images.githubusercontent.com/59594174/84546714-e9445a00-accf-11ea-98e6-d94fb2daaa88.png)

#### Insights Dashboards

![Insights_Dashboard](https://user-images.githubusercontent.com/59594174/84546725-f2352b80-accf-11ea-97f6-ba314c8e1150.png)


