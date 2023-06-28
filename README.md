This is a demo project to show that Platform.sh requires UTF-8 encoding for config files.

To be more specific:

- Deployment fails when the `.platform.app.yaml` file is encoded in UTF-16.
- When that same file is converted to UTF-8, deployment succeeds.

Reproduction
---

```sh
$ git clone https://github.com/ehmatthes/ll_demo_platformsh.git
$ cd ll_demo_platformsh
$ python -m venv .venv
$ source .venv/bin/activate
(.venv)$ pip install --upgrade pip
(.venv)$ pip install -r requirements.txt
(.venv)$ python convert_encoding.py utf-16
(.venv)$ git commit -am "Set .platform.app.yaml encoding to utf-16."
(.venv)$ platform create
  ...
  * Project title (--title)
  Default: Untitled Project
  > ll_project
(.venv)$ platform push
  ...
  Validating configuration files

  E: Error parsing configuration files:
      - applications: Error loading data: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
  To git.us-2.platform.sh:i7lrxpu6t4pwo.git
   ! [remote rejected] HEAD -> main (invalid configuration files)
  error: failed to push some refs to 'git.us-2.platform.sh:i7lrxpu6t4pwo.git'
(.venv)$ python convert_encoding.py utf-8
(.venv)$ git commit -am "Set .platform.app.yaml encoding to utf-8."
(.venv)$ platform push
  ...
  deployment succeeds
```