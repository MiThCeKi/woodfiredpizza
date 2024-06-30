
import watchtower
import logging

import boto3

from pizza_and_bread.schemas.temperature import DTO_TemperatureRecord, DTO_TemperatureResponse
from pizza_and_bread.services.generate_data import generate_fake_temperature_data
from pizza_and_bread.config import DATABASE_NAME, TABLE_NAME

#create an instance of the timestream client - I'll need another one for queries but can define that in another service.
timestream_write = boto3.client('timestream-write')


# configure logging using logging and watchtower
boto3.setup_default_session(profile_name='pizzabread')
logger = logging.getLogger()
logger.setLevel(logging.ERROR)
cloudwatch_handler = watchtower.CloudWatchLogHandler(log_group='Timestream-errors', stream_name='pizza-bread-timestream')
logger.addHandler(cloudwatch_handler)


# Format the DTO record to a Timestream-compatible record
def DTO_record_to_timestream_record_micro_service(record: DTO_TemperatureRecord) -> dict:
    return {
        'Dimensions': [
            {
                'Name': 'session_id',
                'Value': record.session_id
            }
        ],
        'MeasureName': 'temperature',
        'MeasureValue': str(record.temperature),
        'MeasureValueType': 'DOUBLE',
        'Time': str(record.time)  # Ensure the time is in string format
    }


def write_records_to_timestream(records: DTO_TemperatureResponse, batch_size: int = 99):
    """
    This is an API call to write records and takes in a DTO_TemperatureResponse object that was created by the generate_fake_temperature_data function
    """
    
    try:
        # Convert records to Timestream format
        records_to_write = [DTO_record_to_timestream_record_micro_service(record) for record in records.records]
        
        # writing the records in batches of 100, which is timestreams max batch size
        # using range allows me to work through the whole list but does it in batches of 100
        for i in range(0, len(records_to_write), batch_size):
            
            # Select out the batch of records
            batch = records_to_write[i:i + batch_size]
            
            # Write the batch of records to Timestream
            try:
                timestream_write.write_records(
                    DatabaseName=DATABASE_NAME,
                    TableName=TABLE_NAME,
                    Records=batch
                )
           
            # Catch any errors but a systematic exception will be raised and one for every line of the batch that failed. 
            except timestream_write.exceptions.RejectedRecordsException as e:
                logger.error(f"The RejectedRecordsException says: {e}")
                print(f"The RejectedRecordsException says: {e}")
                
                #iterate over the rejected records and print out the record index and the reason
                for rejected_record in e.respoonse["RejectedRecords"]:
                    logger.error(f"RecordIndex: {rejected_record['RecordIndex']}, Reason: {rejected_record['Reason']}")
                    print(f"RecordIndex: {rejected_record['RecordIndex']}, Reason: {rejected_record['Reason']}")

            except Exception as e:
                print(f"Error writing to Timestream because of: {e}")
    except Exception as e:
        logger.error(f"Error preparing records for Timestream: {e}")
        print(f"Error preparing records for Timestream: {e}")
     
    
   
fake_temperature_DTO = generate_fake_temperature_data(400)
write_records_to_timestream(fake_temperature_DTO)  # Writes to Timestream