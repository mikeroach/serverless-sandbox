# randomCoords.py
# -*- coding: utf-8 -*- (to allow emoji in comments, naturally)
#
# AWS Lambda Python function to return random pair of x+y coordinates based on
# max values supplied via GET parameter in HTTP request via AWS API Gateway.
#
# Barely more practical than "hello world".
#
# Written by Mike Roach <mroach@got.net> on 2017-07-04. 🎆

import random
#import json <- That would probably make building the response less tedious.

# With API Gateway/Lambda proxy integration, event input is formatted per http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html#api-gateway-simple-proxy-for-lambda-input-format
# Lambda Python context object is documented here: http://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html
def lambda_handler(event, context):
    # Use GET URL parameters to determine upper limit on returned output
    max_x = int(event['queryStringParameters']['max_x'])
    max_y = int(event['queryStringParameters']['max_y'])
    # Set coordinate variables to random numbers with upper limit from GET input
    x_coord = str(random.randint(0, max_x))
    y_coord = str(random.randint(0, max_y))
    # Build JSON response payload to return. The output format required for
    # Lambda Proxy integration is documented here: http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-set-up-simple-proxy.html#api-gateway-simple-proxy-for-lambda-output-format
    # Set wildcard CORS header to facilitate local frontend javascript testing.
    response = {"statusCode": 200, \
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}, \
        "body": "{\"x\": " + x_coord + ", \"y\": " + y_coord + "}"}
    return response

'''
Sample Lambda event test definition for this function:
{
  "queryStringParameters": {
    "max_x": 100,
    "max_y": 200
  }
}
'''
