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

############################################################DRS_Success############################################################
@app.route('/Success_DRS', methods=["GET", "POST"])
def DRS_Success():
    if request.method == 'GET':
        return render_template('upload_logs2.html')
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
            return redirect(url_for('for_autom2', filename1=filename))

@app.route('/forautom2', methods=["GET", "POST"])
def for_autom2():
    if request.method == 'GET':
        return render_template('visualize_logs2.html')

@app.route('/automation2', methods=["GET", "POST"])
def automation_page2():
    if request.method == "GET":
        csvfile = glob.glob(r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_column = []
        for col in data[data.columns]:
            df_column.append(col)
        df_column_2 = [df_column[1], df_column[4], df_column[7], df_column[10], df_column[13], df_column[16]]
        return render_template('choose_visualize2.html', col_2=df_column_2)

@app.route('/visualization_final2', methods=["GET", "POST"])
def final_visualization2():
    if request.method == 'GET':
        vcol = request.args['y_value']
        csvfile = glob.glob(r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_row = []
        for row in data[data.columns[0]]:
            df_row.append(row)
        if vcol == data.columns[1]:
            x = df_row[1:]
            y = data[data.columns[1]][1:]
            y2 = data[data.columns[2]][1:]
            y3 = data[data.columns[3]][1:]
            fig = Figure()
            ax = fig.subplots()
            ax.plot(x, y, color='red')
            ax.plot(x, y2, color='blue')
            ax.plot(x, y3, color='green')
            fig.savefig('static/visual_image/my_plot.png')
            return render_template('successful_visual.html')
        elif vcol == data.columns[4]:
            x = df_row[1:]
            y = data[data.columns[4]][1:]
            y2 = data[data.columns[5]][1:]
            y3 = data[data.columns[6]][1:]
            fig = Figure()
            ax = fig.subplots()
            ax.plot(x, y, color='red')
            ax.plot(x, y2, color='blue')
            ax.plot(x, y3, color='green')
            fig.savefig('static/visual_image/my_plot.png')
            return render_template('successful_visual.html')
        elif vcol == data.columns[7]:
            x = df_row[1:]
            y = data[data.columns[7]][1:]
            y2 = data[data.columns[8]][1:]
            y3 = data[data.columns[9]][1:]
            fig = Figure()
            ax = fig.subplots()
            ax.plot(x, y, color='red')
            ax.plot(x, y2, color='blue')
            ax.plot(x, y3, color='green')
            fig.savefig('static/visual_image/my_plot.png')
            return render_template('successful_visual.html')
        elif vcol == data.columns[10]:
            x = df_row[1:]
            y = data[data.columns[10]][1:]
            y2 = data[data.columns[11]][1:]
            y3 = data[data.columns[12]][1:]
            fig = Figure()
            ax = fig.subplots()
            ax.plot(x, y, color='red')
            ax.plot(x, y2, color='blue')
            ax.plot(x, y3, color='green')
            fig.savefig('static/visual_image/my_plot.png')
            return render_template('successful_visual.html')
        elif vcol == data.columns[13]:
            x = df_row[1:]
            y = data[data.columns[14]][1:]
            y2 = data[data.columns[15]][1:]
            y3 = data[data.columns[16]][1:]
            fig = Figure()
            ax = fig.subplots()
            ax.plot(x, y, color='red')
            ax.plot(x, y2, color='blue')
            ax.plot(x, y3, color='green')
            fig.savefig('static/visual_image/my_plot.png')
            return render_template('successful_visual.html')

@app.route('/visualization_final_all2', methods=["GET", "POST"])
def final_visualization_all2():
    if request.method == 'GET':
        csvfile = glob.glob(
            r"/Users/ladynaltarejos/PycharmProjects/pythonProject/logs_visualization/static/files/*.csv")
        latest_file_rec = max(csvfile, key=os.path.getctime)
        data = pd.read_csv(latest_file_rec)
        df_row = []
        for row in data[data.columns[0]]:
            df_row.append(row)
        x = df_row[1:]
        y = data[data.columns[1]][1:]
        y2 = data[data.columns[2]][1:]
        y3 = data[data.columns[3]][1:]
        y4 = data[data.columns[4]][1:]
        y5 = data[data.columns[5]][1:]
        y6 = data[data.columns[6]][1:]
        y7 = data[data.columns[7]][1:]
        y8 = data[data.columns[8]][1:]
        y9 = data[data.columns[9]][1:]
        y10 = data[data.columns[10]][1:]
        y11 = data[data.columns[11]][1:]
        y12 = data[data.columns[12]][1:]
        y13 = data[data.columns[13]][1:]
        y14 = data[data.columns[14]][1:]
        y15 = data[data.columns[15]][1:]
        y16 = data[data.columns[16]][1:]
        fig = Figure()
        ax = fig.subplots()
        ax.plot(x, y, color='red')
        ax.plot(x, y2, color='blue')
        ax.plot(x, y3, color='green')
        ax.plot(x, y4, color='yellow')
        ax.plot(x, y5, color='red')
        ax.plot(x, y6, color='black')
        ax.plot(x, y7, color='brown')
        ax.plot(x, y8, color='orange')
        ax.plot(x, y9, color='indigo')
        ax.plot(x, y10, color='violet')
        ax.plot(x, y11, color='purple')
        ax.plot(x, y12, color='gray')
        ax.plot(x, y13, color='magenta')
        ax.plot(x, y14, color='cyan')
        ax.plot(x, y15, color='pink')
        ax.plot(x, y16, color='gold')
        fig.savefig('static/visual_image/my_plot.png')

        return render_template('successful_visual.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)