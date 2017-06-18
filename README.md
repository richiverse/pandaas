# RYP
RestY Interface 4 Python ![RYP](https://s-media-cache-ak0.pinimg.com/originals/e2/92/cf/e292cf96f3c81989f716951e5960137d.jpg = 200x200)

## Features
* Deploy your dependencies to AWS API Gateway to have a RESTful API to your
  favorite packages.
* Store intermediate results to Dynamodb


## Requirements
At a minimum you will need a [Zappa file](https://github.com/Miserlou/Zappa#advanced-settings).

You can also include the following files in the root of your repo.
* requirements.txt 
* [aptfile](https://github.com/seatgeek/bash-aptfile#usage)

## Installation
For these examples, you can use a REST client like postman but I will be using
[httpie](https://httpie.org/doc#https)

```bash
To install:
pip install ryp
```


## Quickstart

run ryp clone on your repo to get started
```bash
ryp clone https://github.com/richiverse/ryp
https://<api-gateway-id>.execute-api.<region>.amazonaws.com/<stage>
```
