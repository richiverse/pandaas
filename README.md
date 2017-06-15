# RYP
RestY Interface 4 Python ![RYP](https://s-media-cache-ak0.pinimg.com/originals/e2/92/cf/e292cf96f3c81989f716951e5960137d.jpg)

## Features
* Deploy your dependencies to AWS API Gateway to have a RESTful API to your
  favorite packages.
* Store intermediate results to Dynamodb


## Usage
For these examples, you can use a REST client like postman but I will be using [httpie]()

```bash
To install:
pip install rip
```
run rip clone on your repo to get started
```bash
rip clone https://github.com/richiverse/rip
https://<api-gateway-id>.execute-api.<region>.amazonaws.com/<stage>
```

## Requirements
At a minimum you will need a [Zappa file]().

You can also include the following files in the root of your repo.
* requirements.txt 
* [aptfile]()

## Quickstart
