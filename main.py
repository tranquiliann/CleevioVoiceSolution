from llamaindex_rag.query_engine import entrypoint
from livekit.agents import cli, WorkerOptions

cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))

