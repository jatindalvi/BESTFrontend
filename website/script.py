def script(list):
    li = list.split(",")
    tup=tuple(li)
    # s="""SELECT * FROM `etim_raw_data_new` WHERE (routeNo="%d" OR routeNo="%d" OR routeNo="%d" OR routeNo="%d") AND (frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s") AND (toStopName="%s" OR toStopName="%s" OR toStopName="%s" OR toStopName="%s") ORDER BY routeNo ASC"""
    s="""SELECT * FROM `etim_raw_data_new` WHERE (routeNo="%d" OR routeNo="%d" OR routeNo="%d" OR routeNo="%d") AND (frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s" OR frmStopName="%s")ORDER BY routeNo ASC"""
    return (s % tup)
