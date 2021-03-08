#import urllib
import urllib.request as urllib
import tempfile
import PyPDF2
import sqlite3
import re
import os

def fetchincidents(url):
   
    #url = ("https://www.normanok.gov/sites/default/files/documents/2021-03/2021-03-03_daily_incident_summary.pdf")

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          

    data = urllib.urlopen(urllib.Request(url, headers=headers)).read()
    return data


def extractincidents(incident_data):
    
    fp = tempfile.TemporaryFile()

    

    # Write the pdf data to a temp file
    fp.write(incident_data)

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    #print(pdfReader.getNumPages())
    pages=[]
    for x in range(pdfReader.getNumPages()):
        page=pdfReader.getPage(x).extractText()
        page=re.sub(' \n',' ',page)
        pages.append(page)
        #print(pages)  
    pdf_dates=[]
    pdf_incident_number=[]
    pdf_location=[]
    pdf_nature=[]
    pdf_incident_ori=[]
    for idx, val in enumerate(pages):
        b=val.split("\n")
        #print(b)
        dates = b[0::5]
        incident_number = b[1::5]
        location = b[2::5]
        nature = b[3::5]
        incident_ori = b[4::5]
        #print(dates)
        dates.pop(-1)
        if idx == 0:
            incident_number.pop(-1) #to remove Daily Incident Summary (Public)
            location.pop(-1) # to remove extra space
        if idx==len(pages)-1:
            #print(incident_number)
            incident_number.pop(-1) # to remove extra space
        #print(len(dates), len(incident_number),len(nature),len(location),len(incident_ori))   
        pdf_dates.extend(dates)
        pdf_incident_number.extend(incident_number)
        pdf_location.extend(location)
        pdf_nature.extend(nature)
        pdf_incident_ori.extend(incident_ori)
    incidents=[]
    for i in range(len(pdf_dates)):
        incidents.append([pdf_dates[i],pdf_incident_number[i],pdf_location[i],pdf_nature[i],pdf_incident_ori[i]])
    return incidents


def createdb():
    #creating a connection with database name parameter
    db_file = "normanpd.db"
    if os.path.exists(db_file):
        os.remove(db_file)
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        #print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def populatedb(db, incidents):
    create_statement="""CREATE TABLE IF NOT EXISTS incidents (
                        incident_time TEXT,
                        incident_number TEXT,
                        incident_location TEXT,
                        nature TEXT,
                        incident_ori TEXT
                        )"""
    db.execute(create_statement)
    for i in range(1, len(incidents)):
        db.execute("INSERT INTO incidents (incident_time, incident_number, incident_location, nature,incident_ori)"
                      " VALUES (?, ?, ?, ?, ?)", (incidents[i][0], incidents[i][1], incidents[i][2], incidents[i][3], incidents[i][4]))
    db.commit()
    
def status(db):
    nature_groups = db.execute("SELECT `nature`, count(*) FROM `incidents`  GROUP BY `nature`" )
    for i in nature_groups:
        print("|".join(map(str,i)))
