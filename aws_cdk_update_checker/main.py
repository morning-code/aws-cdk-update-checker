import requests

AWS_CDK_RELEASES_URL = 'https://api.github.com/repos/aws/aws-cdk/releases'


def main():
    json_body = fetch_aws_cdk_all_releases()
    all_releases = sorted([j['name'] for j in json_body], reverse=True)

    latest_version = all_releases[0]

    print(latest_version)


def fetch_aws_cdk_all_releases():
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    r = requests.get(AWS_CDK_RELEASES_URL, headers=headers)

    if r.status_code != 200:
        raise Exception("could not fetch releases from github...please try again later!")

    return r.json()


if __name__ == '__main__':
    main()
