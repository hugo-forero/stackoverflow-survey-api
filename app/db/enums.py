
from enum import Enum


class RemoteWork(str,Enum):
    REMOTE = "Remote"
    HYBRID_REMOTE = "Hybrid (some in-person, leans heavy to flexibility)"
    IN_PERSON = "In-person"
    HYBRID_IN_PERSON = "Hybrid (some remote, leans heavy to in-person)"
    CHOICE = "Your choice (very flexible, you can come in when you want or just as needed)"


class NewRole(str,Enum):
    DID_NOT_CONSIDER = "I have neither consider or transitioned into a new career or industry"
    VOLUNTARY_TRANSITION = "I have transitioned into a new career and/or industry voluntarily"
    INVOLUNTARY_TRANSITION = "I have transitioned into a new career and/or industry involuntarily"
    CONSIDER = "I have somewhat considered changing my career and/or the industry I work in"
    STRONGLY_CONSIDER = "I have strongly considered changing my career and/or the industry I work in"