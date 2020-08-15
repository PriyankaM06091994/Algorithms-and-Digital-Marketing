try:
    from flask import Flask, request
    from flask_restful import Resource, Api, reqparse
    from flask import app,Flask, request
    from flask_restful import Resource, Api, reqparse
    import datetime
    import json
    import os
    import sys
    import numpy as np
    import ssl
    import elasticsearch
    from elasticsearch import Elasticsearch
    import tensorflow as tf
    import tensorflow_hub as hub
except Exception as e:
    print("Some Modules are Missing {}".format(e))




class Tokens(object):

    def __init__(self, word):
        self.word = word

    def token(self):
        module_url = os.getcwd()
        #path = os.path.join(module_url, "API/Compute")
        embed = hub.KerasLayer(module_url)
        embeddings = embed([self.word])
        x = np.asarray(embeddings)
        x = x[0].tolist()
        return x

if __name__  == "__main__":
    helper= Tokens(word="AmazonBasics 11.6-Inch Laptop Sleeve")
    word  = helper.token()
    print(word)
    d = [-1.4570090770721436,
         -1.2611428499221802,
         -2.2360403537750244,
         -2.0578131675720215,
         -0.19287532567977905,
         1.1759151220321655,
         -0.9432284832000732,
         -0.06388998031616211,
         0.70967698097229,
         1.0902105569839478,
         -2.229905843734741,
         0.7123987674713135,
         1.5530931949615479,
         -0.7601292729377747,
         0.2768378257751465,
         0.21263669431209564,
         -1.927385687828064,
         0.9812129139900208,
         0.46344947814941406,
         0.44331127405166626]