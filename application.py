from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return """
Hello World program, this was created by cloning github.com/Azure-Samples/python-docs-hello-world to github.com/bogdanadrian-burciu/Azure-webApp-PythonFlask repo, then creating a new webApp in Azure Portal, adding the repo in Azure WebApp Deployment Center.
Once deployment has completed, switch back to the brower and http to <app-name>.azurewebsites.net. 

> nslookup boburciu-webapp.azurewebsites.net 
Server:  abuhins1.buh.is.keysight.com 
Address:  10.25.41.140 
Non-authoritative answer: 
Name:    waws-prod-db3-141.cloudapp.net 
Address:  13.69.228.5 
Aliases:  boburciu-webapp.azurewebsites.net 
          waws-prod-db3-141.sip.azurewebsites.windows.net 

"""
