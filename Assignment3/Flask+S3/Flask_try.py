# Run Python3 hello.py
#
#

from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import url_for
from flask_pymongo import PyMongo
import base64
import boto3
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'restdb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Cdiscount'
s3 = boto3.resource('s3')
my_bucket = s3.Bucket('cdis3')
mongo = PyMongo(app)
#Application route to hit https:localhost:5000/category/categoryId
@app.route('/category/<cid>', methods=['GET'])
def get_all_stars(cid):
  #Append the files name from the s3 in the array
  output =[]
  s=""
  #create the prefix to find the folder into the s3
  pre ="S3/"+cid
  for object_summary in my_bucket.objects.filter(Prefix=pre):
      #append the files that are under the paticular folder under the s3 folder
     output.append(object_summary.key)
  for  out in output:
      #create the url for the image src
      fileO = "https://cdis3.s3.amazonaws.com/"+out
      #append multiple image tag to the string to get multiple images


      s = s+ f"<img src='{fileO}' />"
  return s 

if __name__ == '__main__':
    app.run(debug=True)
