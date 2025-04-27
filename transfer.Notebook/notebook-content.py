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

# CELL ********************

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_and_log(message, level='INFO'):
    """
    Print the specified message and log it with the specified level.

    Args:
        message (str): The message to be printed and logged.
        level (str, optional): The log level. Defaults to 'INFO'.
    """
    print(message)

    # Mapping log level strings to their corresponding logging functions
    log_levels = {
        'INFO': logging.info,
        'WARNING': logging.warning,
        'ERROR': logging.error,
        'CRITICAL': logging.critical
    }

    # Get the logging function based on the specified level
    log_func = log_levels.get(level.upper())

    if log_func:
        log_func(message)
    else:
        raise ValueError("Invalid log level specified")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
