
import cv_19
import city_cv_19
import weather
import weather2
import time
from flask import Flask, render_template, request,send_from_directory
from datetime import date,timedelta




app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols') 
app.jinja_env.globals.update(
    zip=zip, 
    enumerate=enumerate, 
) 

@app.route('/')
def index():
    key= request.args.get("keyword")
    if key=="-- 선택 --" or key is None:
        return render_template("index.html")
        
    else:    
        today_1 = date.today()
        today = today_1.strftime("%Y%m%d")
        yesterday_1 = today_1 - timedelta(days=1)
        yesterday = yesterday_1.strftime("%Y%m%d")
        time1 = time.strftime("%H%M")
        time2 = time.strftime("%H%M")
        w_1_time ="0000"
        w_2_time ="0000"

        time1 = int(time1)
        time2 = int(time2)
        

        if  0 <= time1 < 1000 :
            
            
            if 0 <= time1 < 210 :
                w_1_time = "2300"
            if 210 <= time1 <510 :
                w_1_time = "0200" 
            if 510 <= time1 <810 :
                w_1_time = "0500"
            if 810 <= time1 <=959 :
                w_1_time = "0800"

            if 0 <= time2 < 40:
                w_2_time = "2300"
            if 40 <= time2 < 140:
                w_2_time = "0000"
            if 140 <= time2 < 240:
                w_2_time = "0100"
            if 240 <= time2 < 340:
                w_2_time = "0200"
            if 340 <= time2 < 440:
                w_2_time = "0300"
            if 440 <= time2 < 540:
                w_2_time = "0400"
            if 540 <= time2 < 640:
                w_2_time = "0500"
            if 640 <= time2 < 740:
                w_2_time = "0600"
            if 740 <= time2 < 840:
                w_2_time = "0700"
            if 840 <= time2 < 940:
                w_2_time = "0800"
            if 940 <= time2 < 959:
                w_2_time = "0900"
            
            
        elif 1000 <= time1 < 2400 :
            
            if 1000<=time1 <1110:
                w_1_time = "0800"
            if 1110<=time1 <1410:
                w_1_time = "1100"
            if 1410<=time1 <1710:
                w_1_time = "1400"
            if 1710<=time1 <2010:
                w_1_time = "1700"
            if 2010<=time1 <2310:
                w_1_time = "2000"
            if 2310<=time1 <2400:
                w_1_time = "2300"


            if 1000<=time2 < 1040:
                w_2_time = "0900"
            if 1040<=time2 < 1140:
                w_2_time = "1000"
            if 1140<=time2 < 1240:
                w_2_time = "1100"
            if 1240<=time2 < 1340:
                w_2_time = "1200"
            if 1340<=time2 < 1440:
                w_2_time = "1300"
            if 1440<=time2 < 1540:
                w_2_time = "1400"
            if 1540<=time2 < 1640:
                w_2_time = "1500"
            if 1640<=time2 < 1740:
                w_2_time = "1600"
            if 1740<=time2 < 1840:
                w_2_time = "1700"
            if 1840<=time2 < 1940:
                w_2_time = "1800"
            if 1940<=time2 < 2040:
                w_2_time = "1900"
            if 2040<=time2 < 2140:
                w_2_time = "2000"
            if 2140<=time2 < 2240:
                w_2_time = "2100"
            if 2240<=time2 < 2340:
                w_2_time = "2200"
            if 2340<=time2 < 2400:
                w_2_time = "2300"


        data1 = cv_19.get_cv_19_data(today,today)
        data2 = city_cv_19.get_city_cv_19_data(today,today)
        data3 = weather.get_weather_data(today,key,w_1_time)
        data4 = weather2.get_weather2_data(today,key,w_2_time)
        if not data3:
            data3 = weather.get_weather_data(yesterday,key,w_1_time)
       
        if not data4:
            data4 = weather2.get_weather2_data(yesterday,key,w_2_time)
      

        if not data1 or not data2:
            yesterday_1 = today_1 - timedelta(days=1)
            yesterday = yesterday_1.strftime("%Y%m%d")

            time1 = time.strftime("%H%M")
            time2 = time.strftime("%H%M")
            w_1_time ="0000"
            w_2_time ="0000"
            
            time1 = int(time1)
            time2 = int(time2)
           

            
            

            if  0 <= time1 < 1000 :
                
                
                if 0 <= time1 < 210 :
                    w_1_time = "2300"
                if 210 <= time1 <510 :
                    w_1_time = "0200" 
                if 510 <= time1 <810 :
                    w_1_time = "0500"
                if 810 <= time1 <=959 :
                    w_1_time = "0800"

                if 0 <= time2 < 40:
                    w_2_time = "2300"
                if 40 <= time2 < 140:
                    w_2_time = "0000"
                if 140 <= time2 < 240:
                    w_2_time = "0100"
                if 240 <= time2 < 340:
                    w_2_time = "0200"
                if 340 <= time2 < 440:
                    w_2_time = "0300"
                if 440 <= time2 < 540:
                    w_2_time = "0400"
                if 540 <= time2 < 640:
                    w_2_time = "0500"
                if 640 <= time2 < 740:
                    w_2_time = "0600"
                if 740 <= time2 < 840:
                    w_2_time = "0700"
                if 840 <= time2 < 940:
                    w_2_time = "0800"
                if 940 <= time2 < 959:
                    w_2_time = "0900"
                
                
            elif 1000 <= time1 < 2400 :
                
                if 1000<=time1 <1110:
                    w_1_time = "0800"
                if 1110<=time1 <1410:
                    w_1_time = "1100"
                if 1410<=time1 <1710:
                    w_1_time = "1400"
                if 1710<=time1 <2010:
                    w_1_time = "1700"
                if 2010<=time1 <2310:
                    w_1_time = "2000"
                if 2310<=time1 <2400:
                    w_1_time = "2300"


                if 1000<=time2 < 1040:
                    w_2_time = "0900"
                if 1040<=time2 < 1140:
                    w_2_time = "1000"
                if 1140<=time2 < 1240:
                    w_2_time = "1100"
                if 1240<=time2 < 1340:
                    w_2_time = "1200"
                if 1340<=time2 < 1440:
                    w_2_time = "1300"
                if 1440<=time2 < 1540:
                    w_2_time = "1400"
                if 1540<=time2 < 1640:
                    w_2_time = "1500"
                if 1640<=time2 < 1740:
                    w_2_time = "1600"
                if 1740<=time2 < 1840:
                    w_2_time = "1700"
                if 1840<=time2 < 1940:
                    w_2_time = "1800"
                if 1940<=time2 < 2040:
                    w_2_time = "1900"
                if 2040<=time2 < 2140:
                    w_2_time = "2000"
                if 2140<=time2 < 2240:
                    w_2_time = "2100"
                if 2240<=time2 < 2340:
                    w_2_time = "2200"
                if 2340<=time2 < 2400:
                    w_2_time = "2300"
                
            data1 = cv_19.get_cv_19_data(yesterday,yesterday)
            data2 = city_cv_19.get_city_cv_19_data(yesterday,yesterday)
            data3 = weather.get_weather_data(today,key,w_1_time)
            data4 = weather2.get_weather2_data(today,key,w_2_time)
            if not data3:
                data3 = weather.get_weather_data(yesterday,key,w_1_time)
        
            if not data4:
                data4 = weather2.get_weather2_data(yesterday,key,w_2_time)
                

        
        return render_template("index.html",data1=data1,data2=data2,data3=data3,data4=data4,city=key) 
       

@app.route('/sitemap.xml')
@app.route('/robots.txt')
def robot_to_root():
    return send_from_directory(app.static_folder, request.path[1:])



if __name__ == "__main__":
    app.run(debug=True)


