#!/bin/bash

poetry run pytest \
  -v ./tests/* \
  --cov=aws_cdk_update_checker \
  --cov-branch \
  --cov-report=xml
