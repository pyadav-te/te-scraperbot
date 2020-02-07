from flask import Flask, render_template, request, make_response, send_from_directory
from data import ReportList
from Test import APITests
from AlertRules import APIAlertRules
from UnitCalculator import APIUnitCalculator
from AccountGroups import APIAccountGroups
from EnterpriseAgents import APIEnterpriseAgents
from AgentIPList import APIAgentIPList
from auditRepo import getAll, save
import datetime
import json
import time

app = Flask(__name__)

ReportList = ReportList()

# Home
@app.route('/')
def index():
    return render_template('home.html')

# Query
@app.route('/querypage')
def querypage():
    return render_template('query.html')

@app.route('/generate', methods=['POST'])
def result():
    if request.method == 'POST':
        username = request.form.get('user')
        token = request.form.get('auth')
        aid = request.form.get('aid')
        report =  request.form.get('report')

        now = str(time.time())

        fileName = ''.join(report + '_' + str(aid) + '_' + now)
        if report == 'Tests':
            APITests(username, token, aid, fileName)
        elif report == 'AlertRules':
            APIAlertRules(username, token, aid, fileName)
        elif report == 'TestUsage':
            APIUnitCalculator(username, token, aid, fileName)
        elif report == 'AccountGroups':
            APIAccountGroups(username, token, fileName)
        elif report == 'EnterpriseAgents':
            APIEnterpriseAgents(username, token, aid, fileName)
        elif report == 'AgentIPList':
            APIAgentIPList(username, token, aid, fileName)

        save(username, report, str(datetime.datetime.now()), fileName)

        return send_from_directory('reports',
                                   fileName+ '.csv', as_attachment=True)
@app.route('/reportlist')
def reportlist():
    users = getAll()
    return render_template('reportlist.html', reportlist = users )

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug='True')
