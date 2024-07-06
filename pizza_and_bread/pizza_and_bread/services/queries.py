from enum import Enum

class Queries(Enum):
    GET_RECENT_RECORDS = '''
        SELECT time, measure_name, measure_value::double, session_id
        FROM "pizzabread"."timetemp"
        ORDER BY time DESC
        LIMIT 100
    '''
    GET_AGGREGATED_RECORDS = '''
        SELECT time, measure_name, AVG(measure_value::double) as avg_temp
        FROM "pizzabread"."timetemp"
        GROUP BY time
        ORDER BY time DESC
        LIMIT 100
    '''