from pydantic import BaseModel

class VehicleIncidentRequestModel(BaseModel):
    vehicle: str
    issue: str

    
class VehicleIncidentResponseModel(BaseModel):
    category: str
    status: str
    action: str

class VehicleIncidentDBModel(BaseModel):
    id: int
    vehicle: str
    issue: str
    category: str
    status: str
    action: str
    severity: str

class VehicleIncidentUpdateModel(BaseModel):
    status: str
    action: str