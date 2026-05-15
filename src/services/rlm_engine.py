from openrlm import build_runtime

from src.config import AI_MODEL, RLM_PROVIDER

async def RlmEngine(content):
    runtime = build_runtime(
        provider=RLM_PROVIDER,
        model=AI_MODEL,
    )
    
    async with runtime: 
        session = await runtime.create_session("session_1")
        result = await session.run_single(content)
        await runtime.close_session("session_1")
        return result