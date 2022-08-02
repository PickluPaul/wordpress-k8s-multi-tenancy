from pickle import TRUE
from flask import Flask, render_template,request
import os
import subprocess

import time
from concurrent.futures import ThreadPoolExecutor
app = Flask(__name__)

text_file='/Users/picklupaul/Desktop/Kubernetes/multitenant-service/urlfile.txt'

def run_service(name):
    os.system('minikube service wordpress --url -n {0} > {1}'.format(name,text_file))

@app.route('/',methods = ['GET','POST'])
def send():
    if request.method == 'POST':
        executor = ThreadPoolExecutor(max_workers=10)
        name = request.form['name']
        os.system('ansible-playbook playbook.yaml --extra-vars "tenantname={0}"'.format(name))
        executor.submit(run_service, (name))
        time.sleep(5)
        print('hello')
        with open(text_file, 'r') as fh:
            url=fh.read()
        return '<html>To access your wordpress blog: <a href="'+url+'">Click Here</a></html>'
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8070)

