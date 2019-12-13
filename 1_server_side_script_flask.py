from flask import Flask, jsonify, request

app = Flask(__name__)

emp_det = {'ename':'KUMAR', 'eid':343}

@app.route('/get', methods=['GET'])
def get_emp_details():
    '''
    To get all emp details
    Method ==> GET
    URL    ==> http://127.0.0.1:5000/get
    '''
    return jsonify(emp_det)

@app.route('/create', methods=['POST'])
def create_emp():
    '''
    To create new record
    Method ==> POST
    URL    ==> http://127.0.0.1:5000/create
    Request Data   ==> {"sal":"50000"}
    '''
    d = request.json
    emp_det.update(d)
    return jsonify(emp_det)

@app.route('/update', methods=['PUT'])
def update_emp():
    '''
    To update emp details
    Method ==> UPDATE
    URL    ==> http://127.0.0.1:5000/update
    Request Data   ==> {"ename":"kumar"}
    '''
    d = request.json
    emp_det.update(d)
    return ' {0} RECORD UPDATED SUCCESSFULLY'.format(d)

@app.route('/delete', methods=['DELETE'])
def delete_emp():
    '''
    To delete emp record
    Method ==> DELETE
    URL    ==> http://127.0.0.1:5000/delete
    Request Data   ==> {"sal":"50000"}
    '''
    d = request.json
    keys = list(d.keys())
    k = keys[0]
    del emp_det[k]
    return 'Deleted {0} record SUCCESSFULLY'.format(k)


# To run app
app.run(debug=True)

