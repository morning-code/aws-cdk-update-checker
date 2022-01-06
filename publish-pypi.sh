#!/bin/bash

usage_exit() {
  echo "Usage: $0 [-d]"
  exit 1
}

dev=0

while getopts dh OPT; do
  case $OPT in
  d)
    dev=1
    ;;
  h)
    usage_exit
    ;;
  \?)
    usage_exit
    ;;
  esac
done
shift $((OPTIND - 1))

poetry build

if [ $dev -eq 1 ]; then
  poetry config repositories.testpypi https://test.pypi.org/legacy/
  username=otajisan
  # shellcheck disable=SC2162
  read -sp "Password: " password
  poetry config http-basic.testpypi "${username}" "${password}"
  poetry publish -r testpypi
else
  poetry publish
fi
