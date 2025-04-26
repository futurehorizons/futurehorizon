# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "25cfc506-b0f7-4804-8f85-1858bd77f445",
# META       "default_lakehouse_name": "lakehouse",
# META       "default_lakehouse_workspace_id": "2358b2cc-6241-466e-a6ad-c55ee157f648",
# META       "known_lakehouses": [
# META         {
# META           "id": "25cfc506-b0f7-4804-8f85-1858bd77f445"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/order/2019.csv")
# df now is a Spark DataFrame containing CSV data from "Files/order/2019.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
