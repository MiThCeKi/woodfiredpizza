
import boto3
from pizza_and_bread.logging.logging import set_up_logging


timestream_query = boto3.client('timestream-query')
boto3.setup_default_session(profile_name='pizzabread')

# configure logging using logging and watchtower
logger = set_up_logging(log_group='Timestream-query-errors', stream_name='pizza-bread-timestream')


# use boto3 to send the query to timestream

def query_records_from_timestream(query: str) -> dict:
    try:
        response = timestream_query.query(QueryString=query)
    except Exception as e:
        logger.error(f'Error querying Timestream: {e} with the following query:\n {query}')
        print(f"Error querying Timestream: {e} with the following query:\n {query}")
        return None
    return response



# use the dataframe to plot the data

