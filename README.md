# INCOME-TAX

## API END POINT (DEPLOYED IN HEROKU)
```
url = "https://incometaxcalc1.herokuapp.com/calc"

```

```
import requests

data =   {
    "data": [
  {
    "INDEX": 0,
    "DATE": "2020-05-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 1,
    "DATE": "2020-06-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 2,
    "DATE": "2020-07-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 3,
    "DATE": "2020-08-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 4,
    "DATE": "2020-09-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 5,
    "DATE": "2020-10-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 6,
    "DATE": "2020-11-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 7,
    "DATE": "2020-12-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 8,
    "DATE": "2021-01-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 9,
    "DATE": "2021-02-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 10,
    "DATE": "2021-03-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 11,
    "DATE": "2021-04-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  },
  {
    "INDEX": 12,
    "DATE": "2021-05-02",
    "SOURCE NAME": "COMPANY PVT LTD",
    "CREDIT": 80000,
    "DEBIT": 0
  }
]
}

res = requests.post(url = "https://incometaxcalc.herokuapp.com/calc", json = data)

res.json()


```


## LOGS 
```
021-10-17T05:25:58.252668+00:00 heroku[router]: at=info method=POST path="/calc" host=incometaxcalc1.herokuapp.com request_id=7c677324-f65f-4c4f-8bee-d4adad6a93a0 fwd="49.37.150.173" dyno=web.1 connect=0ms service=9ms status=200 bytes=187 protocol=https

2021-10-17T05:25:58.251358+00:00 app[web.1]:     INDEX        DATE      SOURCE NAME  CREDIT  DEBIT
2021-10-17T05:25:58.251370+00:00 app[web.1]: 0       0  2021-05-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251370+00:00 app[web.1]: 1       1  2021-06-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251371+00:00 app[web.1]: 2       2  2021-07-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251371+00:00 app[web.1]: 3       3  2021-08-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251371+00:00 app[web.1]: 4       4  2021-09-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251372+00:00 app[web.1]: 5       5  2021-10-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251372+00:00 app[web.1]: 6       6  2021-11-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251372+00:00 app[web.1]: 7       7  2021-12-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251373+00:00 app[web.1]: 8       8  2021-01-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251373+00:00 app[web.1]: 9       9  2021-02-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251373+00:00 app[web.1]: 10     10  2021-03-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251373+00:00 app[web.1]: 11     11  2021-04-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251374+00:00 app[web.1]: 12     12  2021-05-02  COMPANY PVT LTD   80000      0
2021-10-17T05:25:58.251462+00:00 app[web.1]: income tax calculator function called  
2021-10-17T05:25:58.251491+00:00 app[web.1]: income <= 1250000
2021-10-17T05:25:58.251534+00:00 app[web.1]: tax amount is : 83000.0 Rupees
2021-10-17T05:25:58.252198+00:00 app[web.1]: 10.1.27.253 - - [17/Oct/2021:05:25:58 +0000] "POST /calc HTTP/1.1" 200 35 "-" "PostmanRuntime/7.28.4"
```
