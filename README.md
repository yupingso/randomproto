# randomproto: Random protobuf object generator
[![travis](https://travis-ci.org/yupingso/randomproto.svg?branch=master)](
    https://travis-ci.org/yupingso/randomproto)
[![codecov](https://codecov.io/github/yupingso/randomproto/branch/master/graphs/badge.svg?job=5406291412)](
    https://codecov.io/gh/yupingso/randomproto)

Refer to the [documentation](https://randomproto.readthedocs.io/en/latest/) for API reference.

## Installation
`pip install randomproto`

## Usage
An example of pre-compiled Python file can be found
in [example2_pb2.py](https://raw.githubusercontent.com/yupingso/randomproto/master/tests/example2_pb2.py).
```py
>>> import randomproto
>>> proto = example2_pb2.TypeMessage
>>> msg = randomproto.randproto(proto)
>>> msg
utm_source: "qv"
utm_medium: "dr"
utm_campaign: "sj"
bwp_lp: ""
usergroup: ""
step: -15511
cartTime: -61655
buyTime: 64308
searchTime: 59939
landingTime {
  value: 1533581008
  scale: MINMAX
}
stepsAfterBuy: 13140
lastSessionTime {
  value: 118924455
  scale: SECONDS
}
landingReferrerDomain: "n"
adGroupID: -30428
initiateCheckoutTime: 11859
```
