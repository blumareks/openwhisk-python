# openwhisk-python
This repository demonstrates the building of the complex Python based Serverless actions with Apache Openwhisk in IBM Cloud.

## creating an account
In order to follow the next steps you need to create an account on IBM Cloud. Alternatively you might want to install Apache OpenWhisk on your system. In my opinion - see my book Serverless Swift - it is great if the Serverless infrastructure is being managed by the vendor.

If you decide to run the native Apache OpenWhisk (and not Serverless in IBM Cloud) change the instructions below from ```ibmcloud fn ...``` to ```wsk ...```

### sign up to IBM Cloud
You might want to sign in/up to IBM Cloud. After creating an account on http://cloud.ibm.com use this link to download a CLI: https://cloud.ibm.com/functions/learn/cli

Please mind that I will be using CF based Namespace for the following actions (as they are required for Serverless Swift to operate).

The CF based Namespace look like something this: serverless.swift@roboticsind.com_dev

### login from IBM Cloud CLI
The easiest way to login from CLI is using your browser's existing session in IBM Cloud. Simply type:

```
ibmcloud login -a cloud.ibm.com -o "serverless.swift@roboticsind.com" -s "dev" --sso
```

This should open a new window, and the session token should be presented to you. Copy it and paste in the terminal window.

```
Get a one-time code from https://identity-1.us-south.iam.cloud.ibm.com/identity/passcode to proceed.
Open the URL in the default browser? [Y/n] > 
One-time code > 
Authenticating...
OK

Targeted account Marek  ...
```
Also you need to target the environment:

```
ibmcloud resource groups
...some groups here...

ibmcloud target -g Default
```

### connect to IBM Cloud Functions

You would need to dowload the CF plugin:

```
ibmcloud plugin install cloud-functions
```

And now you can test if the connection works (if not, check my book - Serverless Swift - for hints):
```
ibmcloud fn list
```

Cloud the above code to your directory:

```
git clone https://github.com/blumareks/openwhisk-python.git
cd openwhisk-python
```

### download the libraries with virtualenv
Now you are ready to create the environment in order to create the complex Python action with additional libraries.

```
docker run --rm -v "$PWD:/tmp" openwhisk/python3action bash -c   "cd tmp && virtualenv virtualenv && source virtualenv/bin/activate && pip install -r requirements.txt"
```

The logs:
```
Using base prefix '/usr/local'
New python executable in /tmp/virtualenv/bin/python
Installing setuptools, pip, wheel...done.
Collecting yattag
  Downloading yattag-1.14.0.tar.gz (26 kB)
Building wheels for collected packages: yattag
  Building wheel for yattag (setup.py): started
  Building wheel for yattag (setup.py): finished with status 'done'
  Created wheel for yattag: filename=yattag-1.14.0-py3-none-any.whl size=15658 sha256=492d02876192b4240b96a3586d7affe22b3bf67e7bf3ee023daa7fd73b5168d2
  Stored in directory: /root/.cache/pip/wheels/e7/aa/fd/c1d0692564453adf9b34ddaf9a22e9a9f48b53d35ddc096864
Successfully built yattag
Installing collected packages: yattag
Successfully installed yattag-1.14.0
```

This command should have create for your the dependency directory ```virtualenv```

### compressing your action
You are ready to zip your files and resources for your action:
```
zip -q -r yattag.zip __main__.py searchfile.py virtualenv
```

### creating updating your Action
If you haven'y done it before, create your package:

```
ibmcloud fn package create test
```


Update your action in IBM Cloud

```
ibmcloud fn action update test/yathello yattag.zip --web true --kind python:3 
```

### test and call your action:
Calling your web action (```--web true```):
```
curl $(ibmcloud fn action get test/yathello --url | tail -1)
```

And if you want to debug it:

```
ibmcloud fn action invoke test/yathello --blocking
```

You can also add a parameter ```url``` (the parameter ```name``` just to demonstrate the multiples):

```
ibmcloud fn action invoke test/yathello --param url myurl --param name Marek --blocking
```

Let me know how it worked for you. Follow / DM me on Twitter: @blumareks

