# Algorithms-and-Digital-Marketing


### Assignment 3 - Implementing Visual search

#### Team Information

| NAME              |     NUID        |
|------------------ |-----------------|
| Priyanka Malpekar |   001302741     |
|   Jui Ashinkar    |   001443824     |


#### CLAAT Link
https://codelabs-preview.appspot.com/?file_id=17eNMDqSmghdf-Fq4rKjazl2In8refahJ6sLwHXJ2_Ds

### About Dataset

Our image dataset has been extracted from the full list of more than 40M products available at cdiscount.com in July, 2017.The dataset is organized according to a 3-level classification tree with categories labeled in French. So, to be precise there are 12,371,293 images for 7,069,896 products.

The information about this publicly released dataset can be found here:  https://www.kaggle.com/c/cdiscount-image-classification-challenge

#### train.bson :
(Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format. This kernel provides an example of how to process the data.

#### category_names.csv:
Shows the hierarchy of product classification. Each category_id has a corresponding level1, level2, and level3 name, in French. The category_id corresponds to the category tree down to its lowest level. This hierarchical data may be useful, but it is not necessary for building models and making predictions. All the absolutely necessary information is found in train.bson.

#### train_example.bson:
Contains the first 100 records of train.bson so you can start exploring the data before downloading the entire set.


## Algorithms:

### Similarity Search: Cosine Similarity Algorithm

Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between two vectors projected in a multi-dimensional space.

### Similarity Search: Facebook AI Similarity Search using FAISS

FAISS is a library used for efficient similarity search and clustering of dense vectors. It returns all elements that are within a given radius of the query point. The vector representation for images is designed to produce similar vectors for similar images, where similar vectors are defined that are nearby in Euclidean space.

### Similarity Search: Annoy-Spotify Method
Annoy (Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for finding approximate nearest neighbors. This algorithm builds an annoy index by appending all image feature vectors stored in the local folder.

## Streamlit:

![StreamlitApp1](https://user-images.githubusercontent.com/59594174/87279121-6ff97c00-c4b4-11ea-9458-8f2e5ed09126.PNG)

![StreamlitApp2](https://user-images.githubusercontent.com/59594174/87279142-8a335a00-c4b4-11ea-9958-e7ffe1240db0.PNG)

![StreamlitApp3](https://user-images.githubusercontent.com/59594174/87279154-94edef00-c4b4-11ea-9e24-aeca7186cdb2.PNG)



