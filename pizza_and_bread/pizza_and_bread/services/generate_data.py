import numpy as np
from datetime import datetime, timedelta
from pizza_and_bread.schemas.temperature import DTO_TemperatureRecord, DTO_TemperatureResponse

def generate_fake_temperature_data(num_records: int)-> DTO_TemperatureResponse:
    current_time = datetime.utcnow()
    
    # Adjusting the base time to ensure it starts from current time and goes backwards in increments of 5 minutes
    base_time = current_time - timedelta(minutes=1 * num_records)
    
    times = [base_time + timedelta(minutes=1 * i) for i in range(num_records)]
    temperatures = 20 + 5 * np.sin(np.linspace(0, 3 * np.pi, num_records))  # Example temperature curve
    session_ids = ['session1'] * num_records  # Example session ID

    records = [
        DTO_TemperatureRecord(
            temperature=round(temp, 2),
            time=int(t.timestamp() * 1000),
            session_id=sid
        ) for temp, t, sid in zip(temperatures, times, session_ids)
    ]
    
    return DTO_TemperatureResponse(records=records)
