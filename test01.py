dictionary1 = {"대한민국":"서울", "프랑스":"파리", "중국":"베이징"}
dictionary1.keys()

print(dictionary1.keys())
print(dictionary1.values())

test={
        "products": [
        {
            "productId": "fhsgN2dW",
            "productName": "\t유저 콘솔",
            "statusCode": "STABLE",
            "regDate": "2019-03-11T13:41:11.000+09:00"
        },
        {
            "productId": "0uW4cez8",
            "productName": "(Old) API Gateway",
            "secretKey": "F",
            "statusCode": "CLOSED",
            "regDate": "2016-05-16T15:50:22.000+09:00"
        }
        ]
}

print(test.values())
print(test.items())