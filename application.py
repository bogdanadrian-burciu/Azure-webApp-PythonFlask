from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
Hello World program \n, This was created by cloning https://github.com/Azure-Samples/python-docs-hello-world to https://github.com/bogdanadrian-burciu/Azure-webApp-PythonFlask repo, then creating a new webApp in Azure Portal, adding the repo in Azure WebApp Deployment Center.
Once deployment has completed, switch back to the browser window open to http://<app-name>.azurewebsites.net. \n

> nslookup boburciu-webapp.azurewebsites.net \n
Server:  abuhins1.buh.is.keysight.com \n
Address:  10.25.41.140 \n
Non-authoritative answer: \n
Name:    waws-prod-db3-141.cloudapp.net \n
Address:  13.69.228.5 \n
Aliases:  boburciu-webapp.azurewebsites.net \n
          waws-prod-db3-141.sip.azurewebsites.windows.net \n

"""
