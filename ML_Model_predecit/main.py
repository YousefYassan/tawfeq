from fastapi import FastAPI
from utils import predict_new
from pydantic import BaseModel, Field
# shakel al youser 
# Initialize the FastAPI app
app = FastAPI(title='Device-Price-Prediction')

# Endpoint for health check
@app.get('/', tags=['General'])
async def home():
    return {'status': 'up & running'}

# Define the DeviceData model
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

# Endpoint for Device Price Prediction
@app.post('/predict', tags=['Regression'])
async def device_price_prediction(data: DeviceData):
    
    # Call the prediction function from utils.py
    pred = predict_new(data=data)

    return {f'Prediction is: ${pred:.3f}'}
