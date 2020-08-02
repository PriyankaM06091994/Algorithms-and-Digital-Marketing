# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:36:42 2020

@author: Priyanka Malpekar
"""

try:

    from typing import Optional
    from fastapi import FastAPI
    import sys
    import pickle
    import os
    import json
    import papermill as pm
    import pandas as pd
    import surprise
    import numpy as np

    sys.path.append("recommenders")
    os.chdir("recommenders")
    from reco_utils.dataset import movielens
    from reco_utils.dataset.python_splitters import python_random_split
    from reco_utils.evaluation.python_evaluation import map_at_k, ndcg_at_k, precision_at_k, recall_at_k
    from reco_utils.recommender.cornac.cornac_utils import predict_ranking
    from reco_utils.common.timer import Timer
    from reco_utils.common.constants import SEED
    import cornac
    
    from reco_utils.dataset.python_splitters import python_random_split
    from reco_utils.evaluation.python_evaluation import (rmse, mae, rsquared, exp_var, map_at_k, ndcg_at_k, precision_at_k, 
                                                     recall_at_k, get_top_k_items)
    from reco_utils.recommender.surprise.surprise_utils import predict, compute_ranking_predictions

    print("System version: {}".format(sys.version))
    print("Cornac version: {}".format(cornac.__version__))
except Exception as e:
    print(e)
    print("Error ")
    
app = FastAPI()


@app.get("/SVD_recommendation")

def read_item(userId:str,itemID: str):

    userID = userId
    itemID = itemID

    df1 = pd.DataFrame(data={
        "userID":[int(userID)],
        "itemID":[int(itemID)]
    })
    
    svd = pickle.load( open( "SVD_pickle.p", "rb" ))
    with Timer() as t:
     foo = predict_ranking(svd, df1, usercol='userID', itemcol='itemID', remove_seen=True)
    print("Took {} seconds for prediction.".format(t))

    foo["userID"] = foo["userID"] .apply(lambda x :  round(x))
    foo["itemID"] = foo["itemID"] .apply(lambda x :  round(x))
    result = foo[foo["userID"]==int(userID)].sort_values(by='prediction', ascending=False).head(10)
    result = result.drop(columns=["prediction", "userID"], axis=1)


    return result.to_json()

    
  



    
    
    
    
