from flask import Flask, render_template, redirect, url_for, send_file, request
import smtplib, ssl, email
#from email.message import EmailMessage
#import imghdr
from email.mime.text import MIMEText
#from flask_wtf import FlaskForm
#from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
#from wtforms.validators import InputRequired
import glob
import pandas as pd
import csv
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib.figure import Figure
from PIL import Image
import seaborn as sns
import range
sns.set()

ALLOWED_EXTENSIONS = {'csv', 'html', 'htm'}


app = Flask(__name__)

app.config['SECRET_KEY'] = 'Innovation'
app.config['UPLOAD_FOLDER'] = r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files"

def allowed_file(filename):
    return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#from email.utils import make_msgid

#my_email = "HirayaManawariTest1@gmail.com"
#password = "vkjgdxuthdlutndw"


@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/upload_logs', methods=["GET", "POST"])
def logs_upload():
    if request.method == 'GET':
        return render_template('upload_logs.html')
    elif request.method == 'POST':
        if 'file1' not in request.files:
            return render_template('selection_main_error1.html')
        file1 = request.files['file1']
        filename = file1.filename
        if file1.filename == '':
            return render_template('selection_main_error1.html')
        if file1 and allowed_file(filename):
            f1 = file1
            filename = secure_filename(f1.filename)
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('for_autom', filename1=filename))

@app.route('/forautom', methods=["GET", "POST"])
def for_autom():
    if request.method == 'GET':
        return render_template('visualize_logs.html')

@app.route('/automation', methods=["GET", "POST"])
def automation_page():
    if request.method == "GET":
        csvfile = glob.glob(r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_column = []
        df_row = []
        for col in data[data.columns]:
            df_column.append(col)
        for row in data[data.columns[0]]:
            df_row.append(row)
        x = df_row
        df_column2 = []

        for col2 in df_column:
            if col2 != df_column[0]:
                df_column2.append(col2)

        return render_template('choose_visualize.html', col_2=df_column2)

@app.route('/visualization_final_all', methods=["GET", "POST"])
def final_visualization_all():
    if request.method == 'GET':
        csvfile = glob.glob(r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_column_list = []
        df_row = []
        for col in data[data.columns]:
            df_column_list.append(col)
        for row in data[data.columns[0]]:
            df_row.append(row)
        x = df_row
        y = data[df_column_list[1]]
        y2 = data[df_column_list[2]]
        y3 = data[df_column_list[3]]

        fig = Figure()
        ax = fig.subplots()
        ax.plot(x, y, color='red')
        ax.plot(x, y2, color='blue')
        ax.plot(x, y3, color='green')
        fig.savefig('static/visual_image/my_plot.png')
        return render_template('successful_visual.html')

@app.route('/visualization_final', methods=["GET", "POST"])
def final_visualization():
    if request.method == 'GET':
        vcol = request.args['y_value']
        csvfile = glob.glob(r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_column_list = []
        df_row = []
        for col in data[vcol]:
            df_column_list.append(col)
        for row in data[data.columns[0]]:
            df_row.append(row)
        x = df_row
        y = df_column_list
        fig = Figure()
        zx = fig.subplots()
        zx.plot(x, y)
        fig.savefig('static/visual_image/my_plot.png')
        return render_template('successful_visual.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)