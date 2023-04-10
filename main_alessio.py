


# source_dir = r"C:\Users\Admin\Documents\Python_Analisi_Quantitativa\ALESSIO - progetti personali\Veeam - application\Source"
# destination_dir = r"C:\Users\Admin\Documents\Python_Analisi_Quantitativa\ALESSIO - progetti personali\Veeam - application\Replica"
# log_path = r"C:\Users\Admin\Documents\Python_Analisi_Quantitativa\ALESSIO - progetti personali\Veeam - application"

# print("source_dir=")

import shutil
import os
import pandas as pd
from datetime import datetime
import sys
import time


while True:
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    log_path = sys.argv[3]
    interval = sys.argv[4]
    
    try:
        list_source = os.listdir(source_dir)
        list_destination_dir = os.listdir(destination_dir)
        
        list_remove = [i for i in list_destination_dir if i not in list_source] #Find files to delete
        list_add = [i for i in list_source if i not in list_destination_dir] #Find files to add
        list_update = [i for i in list_source if i  in list_destination_dir] #Find files to update 

        columns = {"time": [], "event" :[], "file_name" :[]}
        df_events = pd.DataFrame(columns)

        for filename_del in list_remove:
            destination = os.path.join(destination_dir, filename_del)
            if os.path.isfile(destination):
                os.remove(destination)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                new_row_del = {"time": dt_string, "event" : "deleted", "file_name" :filename_del}
                #df_events = df_events.concat(new_row_del, ignore_index=True)
                df_events = pd.concat([df_events, pd.DataFrame([new_row_del])], ignore_index=True)


        for filename_copy in list_add:
            source = os.path.join(source_dir, filename_copy)
            destination = os.path.join(destination_dir, filename_copy)
            if os.path.isfile(source):
                shutil.copy(source,destination)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                new_row_copy = {"time": dt_string,"event" : "copied", "file_name" :filename_copy}
                #df_events = df_events.concat(new_row_copy, ignore_index=True)
                df_events = pd.concat([df_events, pd.DataFrame([new_row_copy])], ignore_index=True)

        for filename_upd in list_update:
            source = os.path.join(source_dir, filename_upd)
            destination = os.path.join(destination_dir, filename_upd)
            if os.path.isfile(source):
                shutil.copy(source,destination)
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                new_row_upd = {"time": dt_string,"event" : "updated", "file_name" :filename_upd}
                #df_events = df_events.concat(new_row_upd, ignore_index=True)
                df_events = pd.concat([df_events, pd.DataFrame([new_row_upd])], ignore_index=True)

        # create the directory if it doesn't exist

        log_path = os.path.join(log_path, "{0}_log_file.csv".format(datetime.now().strftime("%Y%m%d_%H%M%S")))
        df_events.to_csv(log_path, index = False)

        print(df_events)
        # wait for sync interval before running again
        time.sleep(int(interval))
    except Exception as e:
        print(f"An error occurred during synchronization: {e}")