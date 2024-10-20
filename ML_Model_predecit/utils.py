import numpy as np
import pandas as pd
import joblib# save model and load it
import os
from pydantic import BaseModel, Field

# Load the pipeline & models
pipe = joblib.load(os.path.join(os.getcwd(), 'artifacts', 'pipeline.pkl'))
model_forest = joblib.load(os.path.join(os.getcwd(), 'artifacts', 'lin_reg.pkl'))# model we chosse 

# Columns in order as user input (updated)
columns = ['brand', 'os', 'ram', 'cpu', 'storage', 'screen size', 'resolution',
           'cpu speed', 'model', 'wireless provider', 'cellular technology', 
           'color', 'refresh rate', 'sim count', 'wireless technology', 'camera', 
           'width resolution', 'height resolution']

# Define desired valid dtypes (updated)
dtypes = {
    'brand': object,
    'os': object,
    'ram': float,
    'cpu': object,
    'storage': float,
    'screen size': float,
    'resolution': object,
    'cpu speed': object,
    'model': object,
    'wireless provider': object,
    'cellular technology': object,
    'color': object,
    'refresh rate': object,
    'sim count': object,
    'wireless technology': object,
    'camera': object,
    'width resolution': float,
    'height resolution': float
}

# Define the new model for the device data
class DeviceData(BaseModel):
    brand: str = Field(..., description="Brand of the device")
    os: str = Field(..., description="Operating System of the device")
    ram: float = Field(..., description="RAM of the device in GB")
    cpu: str = Field(..., description="CPU of the device")
    storage: float = Field(..., description="Storage capacity of the device in GB")
    screen_size: float = Field(..., description="Screen size of the device in inches")
    resolution: str = Field(..., description="Screen resolution of the device")
    cpu_speed: str = Field(..., description="CPU speed of the device")
    model: str = Field(..., description="Model of the device")
    wireless_provider: str = Field(..., description="Wireless provider of the device")
    cellular_technology: str = Field(..., description="Cellular technology of the device")
    color: str = Field(..., description="Color of the device")
    refresh_rate: str = Field(..., description="Refresh rate of the screen")
    sim_count: str = Field(..., description="Number of SIM cards supported")
    wireless_technology: str = Field(..., description="Wireless technology of the device")
    camera: str = Field(..., description="Camera details of the device")
    width_resolution: float = Field(..., description="Width resolution of the screen")
    height_resolution: float = Field(..., description="Height resolution of the screen")

def predict_new(data: DeviceData) -> str:
    """ This function takes the user input as Pydantic and returns the response """

    # Concatenate all features from Pydantic
    input_data = np.array([data.brand, data.os, data.ram, data.cpu, data.storage, 
                           data.screen_size, data.resolution, data.cpu_speed, 
                           data.model, data.wireless_provider, data.cellular_technology, 
                           data.color, data.refresh_rate, data.sim_count, 
                           data.wireless_technology, data.camera, 
                           data.width_resolution, data.height_resolution])
    
    # Adjust the column names and dtypes
    input_data = pd.DataFrame([input_data], columns=columns)
    X_new = input_data.astype(dtypes)

    # Apply Transformation
    X_processed = pipe.transform(X_new)

    # Prediction
    y_pred = model_forest.predict(X_processed)[0]

    return y_pred
