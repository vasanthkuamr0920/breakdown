import streamlit as st
import datetime
import pandas as pd
import sqlite3
import math
from streamlit_js_eval import streamlit_js_eval
import time
import timeDelta
import database

#from pages.itemnumber import lines_read
#from pages.itemnumber import tech_read 

#from itemnumber import lines_read
#from itemnumber import tech_read

 

st.set_page_config(
    page_title="Breakdown Log",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="collapsed",
    
    
)

def lines_read():
    df = pd.read_excel('itemnumbers.xlsx')
    
    df=df[['Line','Machines','Item No']]
    #print(df)
    return df

def tech_read():

    df = pd.read_excel("Itemnumbers.xlsx", sheet_name="Techname")
    technames=df["Name"].unique().tolist()
    return technames


df=lines_read()
lines=tuple(df['Line'].unique().tolist())
machinename=tuple(df['Machines'].unique().tolist())
techname=tech_read()

#print(Machinename)

df2=df
l=False

def get_place():
    try:
        global Machinename,df2,l
        linename=st.session_state.selection
        df2=df[df['Line']==linename]
        #print(df2)
        machinename2=df2['Machines'].tolist()
        
    except:
        pass

    
    
Machinename=None
def get_place2():
    try:
            global l,Machinename,df2
        
            Machinename=st.session_state.selection2
            ITEM_NUMBER=df2[df2["Machines"] == Machinename]["Item No"].values[0]
            #st.text(ITEM_NUMBER)
            st.session_state.default_text = ITEM_NUMBER
            #st.session_state.end_time=Machinename   
            
    except:
        pass
    

def get_place3():
   pass

def get_place4():
   pass

def duration_cal(fromtime,endtime):

    timeList = [ '0:00:00', '0:00:15', '9:30:56' ]
    totalSecs = 0
    for tm in timeList:
        timeParts = [int(s) for s in tm.split(':')]
        totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60 + timeParts[2]
        totalSecs, sec = divmod(totalSecs, 60)
        hr, min = divmod(totalSecs, 60)
        print( "%d:%02d:%02d" % (hr, min, sec) ) 
    h1=int(fromtime.hour)
    m1=int(fromtime.minute)
    s1=int(fromtime.second)
    
    h2=int(endtime.hour)
    m2=int(endtime.minute)
    s2=int(endtime.second)
    h3=h1+h2+(m1+m2+(s1+s2)//60)//60
    m3=(m1+m2+(s1+s2)//60)%60
    s3=(s1+s2)%60




if not st.session_state.get("default_text"):
    st.session_state.default_text = ""

col1,col2,col3= st.columns([1,1,1])
col2.title(":red[Breakdown Logs]")
Line = st.selectbox("Select Line", lines,on_change=get_place,key="selection")
Machine = st.selectbox("Select Machine",options=machinename,on_change=get_place2,key="selection2")#options=df2['Machines'].unique().tolist()
#Itemnumber = st.text_input("Itemnumber",key="Machinename",)#st.selectbox("Select Itemnumber", lines)
#text1 = st.text_area('Item Number', st.session_state["text"])

c = st.container()


Itemnumber = c.text_input("Itemnumber", st.session_state.default_text)


now = datetime.datetime.now()
date = st.date_input("Date",datetime.datetime.now())
fromtime = st.time_input("From Time",value=None)
totime = st.time_input("End Time", value=None)
Natureofbreakdown = st.text_input("Nature of Breakdown", placeholder="Enter Details")
Workcarried = st.text_area("Work Carried Out", placeholder="Enter Details")
technician = st.multiselect("Attended By", techname,on_change=get_place3,key="selection3")
SparesUsed = st.text_input("Spares used",placeholder="SICK sensor")
Remarks = st.selectbox("Remarks", ['Breakdown','No Breakdown'],on_change=get_place4,key="selection4")

if st.button("Submit", type="primary",use_container_width=True):
    
    if str(Machine).isalnum():

       st.error('Please select Machine', icon='🚨')
        
    elif str(Line).isalnum():   

        st.error('Please select Line', icon='🚨')

    elif fromtime is None:   

        st.error('Please select From Time', icon='🚨')

    elif totime is None:   

        st.error('Please select End Time', icon='🚨')
    
    elif Natureofbreakdown is "":   

        st.error('Please Enter nature of Breakdown', icon='🚨')
    
    elif Workcarried is "":   

        st.error('Please Enter Work carried', icon='🚨')

    elif SparesUsed is "":   

        st.error('Please Enter Spare used details', icon='🚨')
    
    elif not technician:
        st.error('Please Enter attended by details', icon='🚨')

    else:
        
        duration=timeDelta.time_diff(fromtime, totime)
        st.write(duration)
        attendedby=""
        for i in technician:
            attendedby=attendedby+i+','
        
        data=(date,Machine,Line, Itemnumber ,str(fromtime),str(totime) , Natureofbreakdown,Workcarried,attendedby,SparesUsed,Remarks ,str(duration))
        res=database.insert_fun(data)
        if res=="success":
            st.balloons()
            st.success('Breakdown Data Logged Success', icon="✅")
            time.sleep(3)
            streamlit_js_eval(js_expressions="parent.window.location.reload()")

if st.button("Reset",use_container_width=True):
    streamlit_js_eval(js_expressions="parent.window.location.reload()")