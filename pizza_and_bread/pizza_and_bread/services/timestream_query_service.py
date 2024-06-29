
import watchtower
import logging

import boto3


timestream_query = boto3.client('timestream-query')


# configure logging using logging and watchtower
boto3.setup_default_session(profile_name='pizzabread')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group='Timestream-errors', stream_name='pizza-bread-timestream')
logger.addHandler(cloudwatch_handler)



