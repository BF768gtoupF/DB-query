#!/usr/local/Python-3.7/bin/python
import pymysql
import os,sys
import cgi
import matplotlib
import numpy as np
import pandas as pd
from io import BytesIO
import base64


import cgitb


cgitb.enable()

matplotlib.use('Agg')




import matplotlib.pyplot as plt
# print content-type





print("Content-type: text/html\n")

print("<html><head>")
print("<title>View a heatmap</title>")
print('''<style>
body {margin:30;padding:30}

background-image: url('https://bioed.bu.edu/images/students_20/mkouzmin/100007.jpg')

</style>
</head>''')
print("<body>")

print("<h1>Enter the info you wish to view</h1>")

Taxonomiclist = ["species","genus","family","order","class","phylum"]
MouseType = ["Pure","Mix","All"]
DiseaseStatus = ["WT","AD","All"]


print('''<form action="https://bioed.bu.edu/cgi-bin/students_20/mkouzmin/project_CSS.py" method="POST" >
	Rank:<select name="Rank">
    <option value="Species">Species</option>
    <option value="Genus">Genus</option>
    <option value="Family">Family</option>
    <option value="Order">Order</option>
    <option value="Class">Class</option>
    <option value="Phylum">Phylum</option>
    </select><br />
    Mouse Type::<select name="Mouse Type">
    <option value="Pure">Pure</option>
    <option value="Mix">Mix</option>
    <option value="All">All</option>
    </select><br />
    Disease Status::<select name="Disease Status">
    <option value="AD">Alzheimer's Disease</option>
    <option value="Wild Type">Wild Type</option>
    <option value="All">All</option>
    </select><br />
	<input type="submit" value="View HeatMap" name = "heatmap">
	<input type = "submit" value = "View Stack Bar Plot" name = "stackbar">
	</form>''')

# get the form
form = cgi.FieldStorage()
if form:
    Rank = form.getvalue("Rank")
    Type = form.getvalue("Mouse Type")
    Status = form.getvalue("Disease Status")
    #print(Rank)
    #print(Type)
    #print(Status)
    query = ""

    if Type =="All" and Status == "All":
        query = """SELECT Abundance.value as value, mouse.name as mname, TaxonomicRank.name as tname FROM Abundance join mouse on Abundance.mid = mouse.mid join TaxonomicRank on Abundance.tid = TaxonomicRank.tid WHERE rank ='%s';""" % (
            Rank)
    elif Type == "All":
        query = """SELECT Abundance.value as value, mouse.name as mname, TaxonomicRank.name as tname FROM Abundance join mouse on Abundance.mid = mouse.mid join TaxonomicRank on Abundance.tid = TaxonomicRank.tid WHERE rank ='%s' and WTvsAD = '%s';""" % (
        Rank, Status)
    elif Status == "All":
        query = """SELECT Abundance.value as value, mouse.name as mname, TaxonomicRank.name as tname FROM Abundance join mouse on Abundance.mid = mouse.mid join TaxonomicRank on Abundance.tid = TaxonomicRank.tid WHERE rank ='%s' and PurevsMix = '%s';""" % (
            Rank, Type)
    else:
        query = """SELECT Abundance.value as value, mouse.name as mname, TaxonomicRank.name as tname FROM Abundance join mouse on Abundance.mid = mouse.mid join TaxonomicRank on Abundance.tid = TaxonomicRank.tid WHERE rank ='%s' and PurevsMix = '%s' and WTvsAD = '%s';"""% (Rank,Type,Status)




    #print(query)
    Abundance = []
    MName = []
    TName = []

    try:
        connection = pymysql.connect(host="bioed.bu.edu", user="mkouzmin", password="mkouzmin", db="groupF", port=4253)
        df = pd.read_sql(query, connection)

        #print(table)
        if form.getvalue('heatmap'):
            table = df.pivot(index='tname', columns='mname', values='value')
            fig, ax = plt.subplots()

            ax.pcolor(table.values, cmap=plt.get_cmap('jet'),
                      vmin=df['value'].min(), vmax=df['value'].max())
            ax.set_xticks(np.arange(table.shape[1] + 1) + 0.5, minor=False)
            ax.set_xticklabels(table.columns, minor=False)
            ax.set_yticks(np.arange(table.shape[0] + 1) + 0.5, minor=False)
            ax.set_yticklabels(table.index, minor=False)
            ax.set_xlim(0, table.shape[1])
            ax.set_ylim(0, table.shape[0])
            #plt.show()
            #fig.colorbar(matplotlib.cm.ScalarMappable(cmap=plt.get_cmap('jet')), ax=ax)
            #doesn't work
            figdata = BytesIO()

            fig.savefig(figdata, format='png')
            image_base64 = base64.b64encode(figdata.getvalue()).decode('utf-8').replace('\n', '')
            figdata.close()

            print("<div>")
            print('''<img src="data:image/png;base64, %s" / >'''%(image_base64))
            print("</div>")
        if form.getvalue('stackbar'):
            pivot_df = df.pivot(index='mname', columns='tname', values='value')
            pivot_df = pivot_df.apply(lambda x: pow(10, x))

            plot = pivot_df.plot.bar(stacked=True)
            fig, ax = plt.subplots()
            ax.set_xticks(np.arange(pivot_df.shape[1] + 1) + 0.5, minor=False)
            ax.set_xticklabels(pivot_df.columns, minor=False)
            ax.set_yticks(np.arange(pivot_df.shape[0] + 1) + 0.5, minor=False)
            ax.set_yticklabels(pivot_df.index, minor=False)
            ax.set_xlim(0, pivot_df.shape[1])
            ax.set_ylim(0, pivot_df.shape[0])
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.6, box.height])
            plt.legend(loc=6, bbox_to_anchor=(1, 0.5), fontsize='xx-small')
            fig = plot.get_figure()
            figdata = BytesIO()
            fig.savefig(figdata, format='png')
            image_base64 = base64.b64encode(figdata.getvalue()).decode('utf-8').replace('\n', '')
            figdata.close()
            print("<div>")
            print('''<img src="data:image/png;base64, %s" / >''' %(image_base64))
            print("</div>")
    except Exception as mysqlError:
        print("<p><font color=red><b>Error</b> while executing query</font></p>")
        print(mysqlError)


print("</body></html>")
