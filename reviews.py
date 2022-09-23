import mysql.connector as conn
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pandas as pd
#from sqlalchemy import create_engine

# #df = pd.read_excel(r"QPR_DA (1).xlsx")
# mydb = conn.connect(host= "localhost", user ="root", passwd= "mangesh",database="weekly_scorecard")
# cursor = mydb.cursor(buffered = True)
#
#
# cursor.execute("use weekly_scorecard")
# engine = create_engine('mysql://root:mangesh@localhost/weekly_scorecard')
# #reviews.to_sql("scorecard", con=engine)


app = Flask(__name__,template_folder='templates')
@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/abc',methods=['POST','GET'])
@cross_origin()
def scorecard():
    if request.method == 'POST':
        a = dict(request.form.items())
        MMID = a["MMID"]
        mydb = conn.connect(host="localhost", user="root", passwd="mangesh",auth_plugin='mysql_native_password')
        cursor = mydb.cursor(buffered=True)
        cursor.execute("use weekly_scorecard")
        df = pd.read_sql(f"select * from scorecard where MMID = '{MMID}'",mydb)
        column_name = df.columns
        data = [[df.loc[i, col] for col in df.columns] for i in range(len(df))]
    return render_template('results.html', columns=column_name, data1=data)

#@app.route('/scorecard',methods=['POST','GET'])
#@cross_origin()
# def scorecard():
#     if request.method == 'GET':
#
#         a = request.args.get('a')
#         mydb = conn.connect(host="localhost", user="root", passwd="mangesh",auth_plugin='mysql_native_password')
#         cursor = mydb.cursor(dictionary=True)
#         cursor.execute("use weekly_scorecard")
#         cursor.execute(f"select * from scorecard where MMID = '{a}'")
#         my_result = cursor.fetchall()
#     return jsonify(my_result)

if __name__ == '__main__':
    app.run(debug=True)
