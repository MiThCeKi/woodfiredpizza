
import logging
import watchtower


def set_up_logging(log_group: str, stream_name: str):
    logger = logging.getLogger()
    logger.setLevel(logging.ERROR)
    cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group=log_group, stream_name=stream_name)
    logger.addHandler(cloudwatch_handler)
    return logger

