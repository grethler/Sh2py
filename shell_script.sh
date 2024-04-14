#!/bin/bash
b64=ZGVmIEhlbGxvV29ybGQoKToNCiAgICByZXR1cm4gIkhlbGxvIFdvcmxkISINCg0KcHJpbnQoSGVsbG9Xb3JsZCgpKQ0K
echo $b64 | base64 -d > _test.py