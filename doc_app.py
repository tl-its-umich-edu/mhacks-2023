# Import the Operating System os module. This is used to help set environment variables.
import os
# Import the necessary bigquery modules
from google.cloud import bigquery
import pandas as pd


# Create a client object that points to the BigQuery instance.
# Note if this step fails make sure the GOOGLE_APPLICATION_CREDENTIALS environment variable was set properly.
bqclient = bigquery.Client() 
# If you receive an error google.auth.exceptions.DefaultCredentialsError: File was not found
# make sure the GOOGLE_APPLICATION_CREDENTIALS environment variables points to your 
# Service Account Key File.
# Set up some SQL for a query
# sql_query = 'select * from `udp-mhacks-november-2023.context_store_keymap.academic_term`'
# sql_query ="SELECT id FROM `udp-mhacks-november-2023.event_store.expanded` where event_date = '2022-04-29'"
# sql_query = "SELECT display_name, size FROM `udp-mhacks-november-2023.mart_course_offering.file_interactions` limit 10"
# sql_query = "SELECT launch_app_name, tool_name FROM udp-mhacks-november-2023.mart_general.lti_tool limit 10"
# sql_query = "select canvas_tool, asset_type from udp-mhacks-november-2023.mart_general.lms_tool limit 10"
sql_query = "select course_subject, program_name from udp-mhacks-november-2023.mart_taskforce.course_profile limit 10"

# Schedule a job to run the query
query_job = bqclient.query(sql_query)

# Fetch the results of the query
query_results = query_job.result()

# # Loop through the results and print out one of the columns
# for row in query_results:
#     print(row)

# Convert the results to a Pandas DataFrame
df = query_results.to_dataframe()

# Print the DataFrame
print(df)