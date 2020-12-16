from enum import Enum, IntEnum
from typing import List, Optional
from odmantic import Model


class RecordType (str, Enum):
    """[summary]
        Record typpe to be inserted into database.
    [description]
        A user can record of three types of entries:
        1) Traumatic Event
        2) Journal Entry
        3) Incident
    """
    trauma = "Traumatic Event"
    journal = "Journal"
    incident = "Incident"

class Severity (int, Enum):
    """[summary]
        The severity of an incident.
    [description]
        A user can determine the severity of the incident based on how it affected them.
    """
    uncomfortable = 1
    difficult_to_function = 2
    very_difficult_to_function = 3
    unable_to_function = 4
    required_medical_assistance = 5

class Record (Model):
    """[summary]
        Base data structure of the PAT API. 
    [description]
        All API calls will perform CRUD operations against the record from a appID. No personal identifiable data should be submitted.
    Arguments:
        BaseModel {[type]} -- [description]
    """
    appID : str
    record_type : RecordType
    severity : List[Severity]

