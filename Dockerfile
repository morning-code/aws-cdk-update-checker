FROM python:3-alpine

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install aws-cdk-update-checker

ENTRYPOINT ["sh", "-c", "aws_cdk_update_-checker"]
