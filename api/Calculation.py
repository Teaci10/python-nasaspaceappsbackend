# Module-level variables that will be set by other modules
CO = 0
SO2 = 0
NO2 = 0
O3 = 0
PM2_5 = 0
PM10 = 0

#Index values
CO_index = 0
SO2_index = 0
NO2_index = 0
O3_index = 0
PM2_5_index = 0
PM10_index = 0

#CO index calculation
def CO_indexcalc():
    global CO, CO_index
    if CO<=4.4:
        CO_index = (CO/4.4)*50
    elif CO<=9.4:
        CO_index = ((CO-4.5)/(9.4-4.5))*49 + 51
    elif CO<=12.4:
        CO_index = ((CO-9.5)/(12.4-9.5))*49 + 101
    elif CO<=15.4:
        CO_index = ((CO-12.5)/(15.4-12.5))*49 + 151
    elif CO<=30.4:
        CO_index = ((CO-15.5)/(30.4-15.5))*99 + 201
    elif CO<=40.4:
        CO_index = ((CO-30.5)/(40.4-30.5))*99 + 301
    elif CO<=50.4:
        CO_index = ((CO-40.5)/(50.4-40.5))*99 + 401
    else:
        CO_index = 500
    return CO_index

#CO alert function
def CO_alert():
    global CO_index
    if CO_index<=50:
        return "Healthy"
    elif CO_index<=100:
        return "Moderate"
    elif CO_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif CO_index<=200:
        return "Unhealthy"
    elif CO_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#SO2 index calculation
def SO2_indexcalc():
    global SO2, SO2_index
    if SO2<=35:
        SO2_index = (SO2/35)*50
    elif SO2<=75:
        SO2_index = ((SO2-36)/(75-36))*49 + 51
    elif SO2<=185:
        SO2_index = ((SO2-76)/(185-76))*49 + 101
    elif SO2<=304:
        SO2_index = ((SO2-186)/(304-186))*49 + 151
    elif SO2<=604:
        SO2_index = ((SO2-305)/(604-305))*99 + 201
    elif SO2<=804:
        SO2_index = ((SO2-605)/(804-605))*99 + 301
    elif SO2<=1004:
        SO2_index = ((SO2-805)/(1004-805))*99 + 401
    else:
        SO2_index = 500
    return SO2_index

#SO2 alert function
def SO2_alert():
    global SO2_index
    if SO2_index<=50:
        return "Healthy"
    elif SO2_index<=100:
        return "Moderate"
    elif SO2_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif SO2_index<=200:
        return "Unhealthy"
    elif SO2_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#NO2 index calculation
def NO2_indexcalc():    
    global NO2, NO2_index
    if NO2<=53:
        NO2_index = (NO2/53)*50
    elif NO2<=100:
        NO2_index = ((NO2-54)/(100-54))*49 + 51
    elif NO2<=360:
        NO2_index = ((NO2-101)/(360-101))*49 + 101
    elif NO2<=649:
        NO2_index = ((NO2-361)/(649-361))*49 + 151
    elif NO2<=1249:
        NO2_index = ((NO2-650)/(1249-650))*99 + 201
    elif NO2<=1649:
        NO2_index = ((NO2-1250)/(1649-1250))*99 + 301
    elif NO2<=2049:
        NO2_index = ((NO2-1650)/(2049-1650))*99 + 401
    else:
        NO2_index = 500
    return NO2_index

#NO2 alert function
def NO2_alert():        
    global NO2_index
    if NO2_index<=50:
        return "Healthy"
    elif NO2_index<=100:
        return "Moderate"
    elif NO2_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif NO2_index<=200:
        return "Unhealthy"
    elif NO2_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#O3 index calculation
def O3_indexcalc():
    global O3, O3_index
    if O3<=0.054:
        O3_index = (O3/0.054)*50
    elif O3<=0.070:
        O3_index = ((O3-0.055)/(0.070-0.055))*49 + 51
    elif O3<=0.085:
        O3_index = ((O3-0.071)/(0.085-0.071))*49 + 101  
    elif O3<=0.105:
        O3_index = ((O3-0.086)/(0.105-0.086))*49 + 151
    elif O3<=0.200:
        O3_index = ((O3-0.106)/(0.200-0.106))*99 + 201
    elif O3<=0.404:
        O3_index = ((O3-0.201)/(0.404-0.201))*99 + 301
    elif O3<=0.504:
        O3_index = ((O3-0.405)/(0.504-0.405))*99 + 401
    else:
        O3_index = 500
    return O3_index

#O3 alert function
def O3_alert():
    global O3_index
    if O3_index<=50:
        return "Healthy"
    elif O3_index<=100:
        return "Moderate"
    elif O3_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif O3_index<=200:
        return "Unhealthy"
    elif O3_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#PM2.5 index calculation
def PM2_5_indexcalc():
    global PM2_5, PM2_5_index
    if PM2_5<=9.0:
        PM2_5_index = (PM2_5/9.0)*50
    elif PM2_5<=35.4:
        PM2_5_index = ((PM2_5-9.1)/(35.4-9.1))*49 + 51
    elif PM2_5<=55.4:
        PM2_5_index = ((PM2_5-35.5)/(55.4-35.5))*49 + 101
    elif PM2_5<=125.4:
        PM2_5_index = ((PM2_5-55.5)/(125.4-55.5))*49 + 151
    elif PM2_5<=225.4:
        PM2_5_index = ((PM2_5-125.5)/(225.4-125.5))*99 + 201
    elif PM2_5<=325.4:
        PM2_5_index = ((PM2_5-225.5)/(325.4-225.5))*99 + 301
    elif PM2_5<=425.4:
        PM2_5_index = ((PM2_5-325.5)/(425.4-325.5))*99 + 401
    else:
        PM2_5_index = 500
    return PM2_5_index      

#PM2.5 alert function
def PM2_5_alert():
    global PM2_5_index
    if PM2_5_index<=50:
        return "Healthy"
    elif PM2_5_index<=100:
        return "Moderate"
    elif PM2_5_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif PM2_5_index<=200:
        return "Unhealthy"
    elif PM2_5_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#PM10 index calculation
def PM10_indexcalc():
    global PM10, PM10_index
    if PM10<=54:
        PM10_index = (PM10/54)*50
    elif PM10<=154:
        PM10_index = ((PM10-55)/(154-55))*49 + 51
    elif PM10<=254:
        PM10_index = ((PM10-155)/(254-155))*49 + 101
    elif PM10<=354:
        PM10_index = ((PM10-255)/(354-255))*49 + 151
    elif PM10<=424:
        PM10_index = ((PM10-355)/(424-355))*99 + 201
    elif PM10<=504:
        PM10_index = ((PM10-425)/(504-425))*99 + 301
    elif PM10<=604:
        PM10_index = ((PM10-505)/(604-505))*99 + 401
    else:
        PM10_index = 500
    return PM10_index

#PM10 alert function
def PM10_alert():
    global PM10_index
    if PM10_index<=50:
        return "Healthy"
    elif PM10_index<=100:
        return "Moderate"
    elif PM10_index<=150:
        return "Unhealthy for Sensitive Groups"
    elif PM10_index<=200:
        return "Unhealthy"
    elif PM10_index<=300:
        return " Very Unhealthy"
    else:
        return "Hazardous"

#Highest AQI calculation
def AQI_calculation():
    global CO_index, SO2_index, NO2_index, O3_index, PM2_5_index, PM10_index
    AQI = max(CO_index, SO2_index, NO2_index, O3_index, PM2_5_index, PM10_index)
    return AQI

# New function to set pollutant data from external source
def set_pollutant_data(pollutant_data):
    global CO, SO2, NO2, O3, PM2_5, PM10
    CO = pollutant_data.get('CO', 0)
    SO2 = pollutant_data.get('SO2', 0)
    NO2 = pollutant_data.get('NO2', 0)
    O3 = pollutant_data.get('O3', 0)
    PM2_5 = pollutant_data.get('PM2_5', 0)
    PM10 = pollutant_data.get('PM10', 0)