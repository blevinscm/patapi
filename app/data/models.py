from enum import Enum, IntEnum
from typing import List, Optional, Set
from odmantic import Model
import datetime


class EntryType (str, Enum):
    """[summary]
        An entry performed by the user.
    [description]
        A user can record of three types of entries:
        1) Traumatic Event
        2) Journal Entry
        3) Incident
    """
    trauma = "Traumatic Event"
    journal = "Journal"
    incident = "Incident"

class IncidentSeverity (int, Enum):
    """[summary]
        In the case of an incident entry a severity level of the incident.
    [description]
        A user can determine the severity of the incident based on how it affected them.
    """
    uncomfortable = 1
    difficult_to_function = 2
    very_difficult_to_function = 3
    unable_to_function = 4
    required_medical_assistance = 5

class IncidentType (str, Enum):
    """[summary]
        In the case of an incident entry the type of incident.
    [description]
        Identification of what happened during the incident.  Can be more than one.
    """
    panic_attack = "Panic Attack"
    nightmare = "Nightmare"
    excessive_anger_outburst = "Excessive Anger Outburst"
    disassociation  = "Disassociation"
    disconnected = "Disconnected"
    flashback = "Flashback"
    auditory_flashback = "Auditory Flashback"
    intrusive_thoughts = "Intrusive Thoughts"
    hyper_arousal = "Hyper Arousal"
    other = "Other"




class Entry (Model):
    """[summary]
        Base data structure of the PAT API. 
    [description]
        All API calls will perform CRUD operations against the record using the appID. No personal identifiable data should be submitted.
   
    """
    appID : str
    entry_type : EntryType
    entry_date : datetime.date
    journal_entry : Optional[str] = None
    trauma_entry : Optional[str] = None 
    incident_severity : Optional[IncidentSeverity]
    incident_type : Optional[Set[IncidentType]] = None
    location : Optional[str] = None
    location_description : Optional[str] = None
    
    class Config:
        schema_extra = {
            "example": {
                "appID" : "00000001",
                "entry_type" : "Incident",
                "entry_date" : "2020-1-1",
                "journal_entry" : "This is a jouurnal entry which is an optional field and free form text entry",
                "trauma_entry" : "This is a trauma entry which is just like a journal entry, but flagged as a traumatic event to make it easier to share with a healthcare provider.",
                "incident_severity" : 3,
                "incident_type" : "nightmare",
                "location" : "111 Microsoft Way",
                "location_description" : "Work"
            }
        } 






