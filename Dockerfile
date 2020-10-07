FROM mcr.microsoft.com/azure-functions/python:3.0-python3.8-appservice

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true

RUN apt-get -y install graphviz

COPY . /home/site/wwwroot

RUN pip install -r /home/site/wwwroot/requirements.txt