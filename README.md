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
