#!/bin/bash

latest_version=$(aws_cdk_update_checker)
echo "::set-output name=latest_version::$latest_version"