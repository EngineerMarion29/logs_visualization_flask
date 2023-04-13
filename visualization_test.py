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

data = pd.read_csv(r'/Users/ladynaltarejos/Downloads/SMART_2022-December_SUCCESS_A2P_Final_Report.csv')

x = data[data.columns[0]][1:]
y = data[data.columns[1]][1:]
y2 = data[data.columns[2]][1:]
y3 = data[data.columns[3]][1:]

fig, ax = plt.subplots()
ax.plot(x, y, color='red')
ax.plot(x, y2, color='blue')
ax.plot(x, y3, color='green')
plt.bar(x, y)
#plt.bar(x, y2)
#plt.bar(x, y3)
plt.show()
#x = df_row
#y = df_column_list[0]
#y2 = df_column_list[1]
#y3 = df_column_list[2]

#fig = Figure()
#ax = fig.subplots()
#ax.plot(x, y, color='red')
#ax.plot(x, y2, color='blue')
#ax.plot(x, y3, color='green')
#fig.plot()
#df_column = []
#df_row = []
#for col in data.columns:
#    df_column.append(col)

#for row in data[data.columns[0]]:
#    df_row.append(row)
#x = df_row
#y = data[df_column[1]]
#y2 = data[df_column[2]]
#y3 = data[df_column[3]]

#fig, ax = plt.subplots()
#ax.plot(x, y, color='red')
#ax.plot(x, y2, color='blue')
#ax.plot(x, y3, color='green')

#plt.savefig('static/my_plot.png')
