import logging
from enum import StrEnum
from typing import Any, List, Optional

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class EventType(StrEnum):
    DELTA_TEXT_EVENT = "delta_text_event"
    COMPLETED_TEXT_EVENT = "completed_text_event"
    NEW_AGENT_EVENT = "new_agent_event"
    TOOL_CALL_EVENT = "tool_call_event"
    TOOL_CALL_OUTPUT_EVENT = "tool_call_output_event"
    TERMINATING_EVENT = "terminating_event"
    ERROR_EVENT = "error_event"


class AgentResponse(BaseModel):
    """Pydantic model for agent response structure"""

    event_type: EventType
    agent_name: str
    history: Optional[
        List[Any]
    ]  # You might want to create a more specific type for history items
    message: Optional[str] = None
    data_type: Optional[str] = None
    data: Optional[Any] = (
        None  # Could be dict, str, or other types depending on use case
    )


class AgentService:

    def __init__(self):
        self.sample_agent = "Create your agent here"

    def list_agents(self):
        """
        Return all available agents in the system.
        """
        return [self.sample_agent]
