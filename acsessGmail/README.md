# Steps:
*Step 1:* Goto [https://developers.google.com/gmail/api/quickstart/python](https://developers.google.com/gmail/api/quickstart/python) and click the button ```Enable the gmail api``` to get credentials.json, store it in a same folder where you store your .py files.
*Step 2:* Run the following command in terminal
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
*Step 3:* Then run [initializeGmail.py](https://github.com/mysg147/basicProjects/blob/master/acsessGmail/initializeGmail.py) only once. It will open Gmail page on your browser enter your credentials. In the end you will get token.json file. 
*Step 4:* Then run [gmailBy.py](https://github.com/mysg147/basicProjects/blob/master/acsessGmail/gmailBy.py)
