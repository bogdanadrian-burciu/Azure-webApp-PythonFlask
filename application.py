from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """Hello World, this was created by cloning https://github.com/Azure-Samples/python-docs-hello-world to https://github.com/bogdanadrian-burciu/Azure-webApp-PythonFlask repo, then creating a new webApp in Azure Portal,
adding the repo in Azure WebApp Deployment Center.
Once deployment has completed, switch back to the browser window open to http://<app-name>.azurewebsites.net.
Guide used: https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python?tabs=powershell.

PS C:\Users\boburciu\python-docs-hello-world> nslookup boburciu-webapp.azurewebsites.net
Server:  abuhins1.buh.is.keysight.com
Address:  10.25.41.140

Non-authoritative answer:
Name:    waws-prod-db3-141.cloudapp.net
Address:  13.69.228.5
Aliases:  boburciu-webapp.azurewebsites.net
          waws-prod-db3-141.sip.azurewebsites.windows.net

PS C:\Users\boburciu\python-docs-hello-world>
"""
