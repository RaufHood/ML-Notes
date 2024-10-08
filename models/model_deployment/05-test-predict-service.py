#!/usr/bin/env python
# coding: utf-8


import requests


#url = "http://192.168.2.117:9696/predict" #
#url = "http://0.0.0.0:9696/predict"#
hostAndPort = "localhost:9696"
host = "churn-serving-env.eba-e6kesmrx.eu-central-1.elasticbeanstalk.com" #default port 80
url = f'http://{host}/predict'

customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}

customer

response = requests.post(url, json = customer).json()
response

if response['churn'] == True:
    print('sending promo email to customer %s' % ('xyz-123'))
else:
    print('Not sending promo email to customer %s' % ('xyz-123'))
# python 05-test-predict-service.py