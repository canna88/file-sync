import shutil
import os
import pandas as pd
from datetime import datetime
import time

# get the source directory, destination directory, log path, and sync interval from command-line arguments
source_dir = input("Enter the source directory path: ")
while os.path.exists(source_dir) == False:
    source_dir = input("Path does not exist - Enter the source directory path: ")

destination_dir = input("Enter the destination directory path: ")
while os.path.exists(destination_dir) == False:
    destination_dir = input("Path does not exist - Enter the destination directory path: ")

log_path = input("Enter the log directory path: ")
while os.path.exists(log_path) == False:
    log_path = input("Path does not exist - Enter the log directory path: ")
    
interval = input("Enter the positive and numeric synchronization interval in seconds: ")
while interval.isdigit() == False or int(interval) <= 0:
    interval = input("Your interval is not correct - Enter the positive and numeric synchronization interval in seconds: ")
interval = int(interval)



while True:
    
    try:
        
        # get the list of files in the source directory and destination directory
        list_source = os.listdir(source_dir)
        list_destination_dir = os.listdir(destination_dir)
                
        # create a Pandas dataframe to store events
        columns = {"time": [], "event" :[], "file_name" :[]}
        df_events = pd.DataFrame(columns)
        
        # check if there are files inside the source directory
        if len(list_source)==0 and len(list_destination_dir)==0:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            new_row_no_file = {"time": dt_string,"event" : "empty_source_dir", "file_name" : "no_file_to_copy"}
            df_events = pd.concat([df_events, pd.DataFrame([new_row_no_file])], ignore_index=True)
        else:
                        
            # find files to remove, add, and update
            list_remove = [i for i in list_destination_dir if i not in list_source] #Find files to delete
            list_add = [i for i in list_source if i not in list_destination_dir] #Find files to add
            list_update = [i for i in list_source if i  in list_destination_dir] #Find files to update 

            # remove files
            for filename_del in list_remove:
                destination = os.path.join(destination_dir, filename_del)
                if os.path.isfile(destination):
                    os.remove(destination)
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    new_row_del = {"time": dt_string, "event" : "deleted", "file_name" :filename_del}
                    df_events = pd.concat([df_events, pd.DataFrame([new_row_del])], ignore_index=True)

            # add files
            for filename_copy in list_add:
                source = os.path.join(source_dir, filename_copy)
                destination = os.path.join(destination_dir, filename_copy)
                if os.path.isfile(source):
                    shutil.copy(source,destination)
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    new_row_copy = {"time": dt_string,"event" : "copied", "file_name" :filename_copy}
                    df_events = pd.concat([df_events, pd.DataFrame([new_row_copy])], ignore_index=True)

            # update files
            for filename_upd in list_update:
                source = os.path.join(source_dir, filename_upd)
                destination = os.path.join(destination_dir, filename_upd)
                if os.path.isfile(source):
                    shutil.copy(source,destination)
                    now = datetime.now()
                    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                    new_row_upd = {"time": dt_string,"event" : "updated", "file_name" :filename_upd}
                    df_events = pd.concat([df_events, pd.DataFrame([new_row_upd])], ignore_index=True)

        # create the directory for logs if it doesn't exist and save events to a CSV file
        log_path_name = os.path.join(log_path, "{0}_log_file.csv".format(datetime.now().strftime("%Y%m%d_%H%M%S")))
        df_events.to_csv(log_path_name, index = False)

        # print events dataframe
        print(df_events)

        # wait for sync interval before running again
        time.sleep(int(interval))
    
    except Exception as e:
        # print an error message if an exception is caught
        print(f"An error occurred during synchronization: {e}")
