# Mustelidae-Data
All Data related functionalities module. Storage, analysis, connections and everything else.

# Firebase

## Setup

First install this repository as dependency, adding this to your requirements.txt:

* Using HTTPS:
```
https://github.com/black-lutrinae/must-data.git
```
* Using SSH:
```
git@github.com:black-lutrinae/must-data.git
```

Environment:

```bash
virtualenv -p python3 venv
source venv/bin/activate
source .env
```

Requirements:
```bash
pip install -r requirements.txt
```
## Credentials

To generate credentials, you go to the admins sdk [page](https://console.firebase.google.com/project/mustelidae-data/settings/serviceaccounts/adminsdk), and click in "generate new private key". Then you will download a `.json` file, which you will save as `db-credentials.json` in the root of this project.

## Contributing

Updating requirements:
```bash
pip freeze > requirements.txt
```