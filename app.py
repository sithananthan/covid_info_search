from flask import Flask, render_template
from flask import request, jsonify
import pandas as pd
import json

app = Flask(__name__)
cols = ["Name", "Phone", "Tag", "District", "City", "Pincode", "Remarks"]
dataframe = pd.DataFrame({}, columns = cols)
df = pd.read_csv('data.csv')
df = df.drop(df.columns[0],axis=1)
data_district = df['District']
data_district = data_district.to_dict()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():   
    if request.method == 'POST':
        data_rx = [request.form['name'], request.form['phone'], request.form['tag'], request.form['district'], request.form['city'], request.form['pincode'], request.form['remarks']]
        dataframe.loc[len(dataframe)] = data_rx
        dataframe.to_csv('data.csv')
        return render_template('home.html')
    return render_template('register.html')


@app.route('/resource', methods = ['GET', 'POST'])
def resource(): 
    df = pd.read_csv('data.csv')
    df = df.drop(df.columns[0],axis=1)
    data_district = df['District']
    data_district = data_district.to_dict()
    data_resource = ""
    if request.method == 'POST' and request.form['district'] == "Any":
        data_resource =request.form['resource']
        df = df.loc[df['Tag'] == data_resource]
        dataframe_resource = df.to_dict(orient="records")
        print(dataframe_resource)
        return render_template('resource.html', dist= data_district, data= dataframe_resource)

    elif request.method == 'POST' and request.form['district'] != "Any":
        data_dist =request.form['district']
        data_resource =request.form['resource']
        df = df.loc[df['Tag'] == data_resource]
        df = df.loc[df['District'] == data_dist]
        dataframe_resource = df.to_dict(orient="records")
        print(dataframe_resource)
        return render_template('resource.html',  dist= data_district, data= dataframe_resource)
        
    else :
        return render_template('resource.html', dist= data_district)

@app.route('/district', methods = ['GET', 'POST'])
def district():
    df = pd.read_csv('data.csv')
    df = df.drop(df.columns[0],axis=1)
    data_district = df['District']
    data_district = data_district.to_dict()
    if request.method == 'POST':
        data_resource =request.form['district']
        print(data_resource)
        df = df.loc[df['Tag'] == data_resource]
        df = df.loc[df['District'] == data_resource]
        dataframe_resource = df.to_dict(orient="records")
        print(dataframe_resource)
        return render_template('district.html', dist= data_district, data= dataframe_resource)
    return render_template('district.html', dist= data_district)

if __name__ == '__main__':
    app.run(debug=True)