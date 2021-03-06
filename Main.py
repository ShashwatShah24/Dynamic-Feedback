from flask import *
import sqlite3  
  
app = Flask(__name__)  

@app.route("/")  
def index():  
    return render_template("home.html");


@app.route("/view",methods =["POST"])  
def view():  
	tables=[]
	global Database
	Database = request.form["db"]
	con = sqlite3.connect(Database)  
	con.row_factory = sqlite3.Row  
	cur = con.cursor()  
	cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
	table=cur.fetchall()
	for Alltable in table:
		for i in range(len(Alltable)):
			tables.append(Alltable[i])

	return render_template("View.html",tables = tables,Database=Database)

@app.route("/viewTable",methods =["POST"])  
def saveDetails():
	tablename = request.form["tab"]
	con = sqlite3.connect(Database)
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	if(tablename=="Steps_Table" or tablename=="Feedback"):	
		column=[]
		cur.execute("select * from {0}".format(tablename))
		rows=cur.fetchall()
		colnames = cur.description
		for Allcolumns in colnames:
			column.append(Allcolumns[0])

		columnlength=len(column)
		
		CompleteDet=[]
		for Allrow in rows:
			Details=[]
			for k in range(0,columnlength):
				Details.append(Allrow[k])
			CompleteDet.append(Details)
		print(CompleteDet)
		
		
	else:
		column=[]
		cur.execute("SELECT Feedback_id,steps,time,name,olmid,manager,team_name,activity_name,remarks FROM Steps_Table LEFT OUTER JOIN Feedback ON Steps_Table.Feedback_id = Feedback.id")
		rows=cur.fetchall()
		colnames = cur.description
		for Allcolumns in colnames:
			column.append(Allcolumns[0])

		columnlength=len(column)
		
		CompleteDet=[]
		for Allrow in rows:
			Details=[]
			for k in range(0,columnlength):
				Details.append(Allrow[k])
			CompleteDet.append(Details)
		print(CompleteDet)

	return render_template("viewTable.html",column=column,rows=rows,columnlength=columnlength,CompleteDet=CompleteDet,tablename=tablename)


# @app.route("/view02")  
# def view():
# 	host =""

if __name__ == "__main__":
	app.run(host='127.0.0.1', port=9090)  
