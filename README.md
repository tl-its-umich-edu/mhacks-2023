# MHack 2023

This repo contains resource for connecting with Synthetic Data of Learning Environment

### Connecting to BigQuery via Service account json
## Docker
1. Store the JSON file receviewed locally for running the python script
2. Make sure to install docker desktop https://docs.docker.com/desktop/
3. Build and run
```sh
docker build -t "gcp-mhack" . #build
docker run -v /path/to/service-account-json/udp-mhacks23-10.json:/app/udp-mhacks23-10.json gcp-mhack #run the build
```
## Local run Python script
1. Install python on your machine. create and activate python virtual enviroment
2. pip install -r requirements.txt
3. run as `python app.py`

### Information about the synthetic data documentation
1. Overview diagram of the data https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/system-overview
2. Context Store: https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/system-overview/context-data-pipeline
3. Event store: https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/system-overview/event-data-pipeline
4. Data Marts: https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/data-stores/data-marts

Caliper Analytics spec for the Event store : https://www.imsglobal.org/activity/caliper

### Browsing the Data via SQL Client (DBeaver)
1. Download the DBeaver: https://dbeaver.io/download/. 
2. Connect to Bigquery using DBeaver or choice of SQL CLient
3. Here is the Guide: https://www.cdata.com/kb/tech/bigquery-odbc-dbeaver.rst#:~:text=Open%20the%20DBeaver%20application%20and,the%20JDBC%20URL%20as%20well.

### Sample Queries
1. `Event_store.expanded` dataset. This table consist of click stream/log/behavioral data about the learning environment like Canvas
    1. always query by datatime to reduce the huge pull of the data
    2. Review the basic of Caliper Analytics specification that generated the events : https://www.imsglobal.org/activity/caliper
    3.  https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/system-overview/event-data-pipeline
    ```sql
    SELECT action, actor.id, actor.name, ed_app.id,object.extensions, event  FROM `event_store.expanded` WHERE event_time BETWEEN DATETIME("2021-09-26") AND DATETIME_ADD("2021-09-26", INTERVAL 1 DAY) 
    ```
2. They are quiet a few data sets in the that can be joined to get the desired results
    1. Context store has 2 schema's Entity and Keymap and joins could be made as below
    ```sql
    select kco.lms_ext_id, eco.* from `context_store_entity.course_offering` eco join `context_store_keymap.course_offering` kco on eco.course_offering_id = kco.id 
    ```
    2. Context Store: https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/system-overview/context-data-pipeline
  
3. Datamart Query combining context store entity schema and lms_tool mart. More lnfo: https://resources.unizin.org/products/data-and-analytics/unizin-data-platform/data-stores/data-marts
```sql
SELECT eco.le_code as course_name,eco.course_offering_id ,mart.* FROM `udp-mhacks-november-2023.mart_general.lms_tool`  mart join `context_store_entity.course_offering` eco on mart.udp_course_offering_id = eco.course_offering_id
```

### Additional Resources
https://docs.google.com/document/d/1U4aI557vSdDx1Ve9CToscrA-p8ERH51umFzUe9nCvvs/edit


