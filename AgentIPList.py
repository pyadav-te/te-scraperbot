import requests
from requests.auth import HTTPBasicAuth
import json
import os
import shutil
from util import generateCSV, APIAuthCreate

# Function Definitions
def APIGetAgents(auth, aid):
    aid = "?aid=" + aid
    # Define URL
    url = 'https://api.thousandeyes.com/v6/agents.json{}'.format(aid)

    # Obtain a list of agents
    response = requests.get(url, auth=auth)

    # Convert the response into a json python dictionary/list
    agentsdict = response.json()

    # Obtain the metrics
    agentslist = agentsdict['agents']

    return agentslist


# Main
def APIAgentIPList(username, token, aid, fileName):

    # list used to store agent metadata
    # (this is what gets output to CSV at the end)
    agentobjectlist = []

    # Define the agent dictionary
    agentdict = {}

    auth = APIAuthCreate(username, token)

    # Pull agent list for later
    agentsList = APIGetAgents(auth, aid)

    # Something to look at on the console
    print('Extracting agent data..')

    # Loop through each agent
    for agent in agentsList:

        agentData={}

        # Columns will be output in this order later. Order only affects output.
        agentFields=[
            'agentType',
            'agentId',
            'agentName',
            "location",
            'countryId',
            'ipAddresses'
        ]

        for field in agentFields:
            if field in agent.keys():
                if field is 'ipAddresses':
                    agentData[field]=", ".join(agent[field])
                else:
                    agentData[field]=agent[field]
            else:
                agentData[field]="NULL"

        agentobjectlist.append(agentData)

    # ALL OUTPUT CODE HERE

    # WRITE TO CSV
    generateCSV(fileName, agentobjectlist)

    return
