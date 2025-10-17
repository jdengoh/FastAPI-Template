import logging

from fastapi import APIRouter
from fastapi.params import Depends

from app.core.dependencies import get_agent_service
from app.services.agent_service import AgentService

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/agent", tags=["Agent"])


@router.post("/list", summary="List All Agents")
async def list_agents(agent_service: AgentService = Depends(get_agent_service)):
    """
    List all available agents and their configurations.
    """
    logger.info("Listing all agents")
    agents = agent_service.list_agents()
    return {"agents": agents}
