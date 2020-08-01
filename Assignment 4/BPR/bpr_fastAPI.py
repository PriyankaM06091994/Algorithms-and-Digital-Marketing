try:

    from typing import Optional
    from fastapi import FastAPI
    import sys
    import pickle
    import os
    import json
    import papermill as pm
    import pandas as pd

    sys.path.append("recommenders")
    os.chdir("recommenders")
    from reco_utils.dataset import movielens
    from reco_utils.dataset.python_splitters import python_random_split
    from reco_utils.evaluation.python_evaluation import map_at_k, ndcg_at_k, precision_at_k, recall_at_k
    from reco_utils.recommender.cornac.cornac_utils import predict_ranking
    from reco_utils.common.timer import Timer
    from reco_utils.common.constants import SEED
    import cornac


    print("System version: {}".format(sys.version))
    print("Cornac version: {}".format(cornac.__version__))
except Exception as e:
    print(e)
    print("Error ")


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recommendation")
def read_item(userId:str,itemID: str):

    userID = userId
    itemID = itemID

    df1 = pd.DataFrame(data={
        "userID":[int(userID)],
        "itemID":[int(itemID)]
    })

    #bpr = pickle.load( open( "trained_model.p", "rb" ))
    bpr = pickle.load( open( "new_model.p", "rb" ))
    with Timer() as t:
        foo = predict_ranking(bpr, df1, usercol='userID', itemcol='itemID', remove_seen=True)
    print("Took {} seconds for prediction.".format(t))

    foo["userID"] = foo["userID"] .apply(lambda x :  round(x))
    foo["itemID"] = foo["itemID"] .apply(lambda x :  round(x))

    result = foo[foo["userID"]==int(userID)].sort_values(by='prediction', ascending=False).head(10)
    result = result.drop(columns=["prediction", "userID"], axis=1)

    #data = {
     #   "data":result
    #}
    #return json.dumps(data)

    return result.to_json()