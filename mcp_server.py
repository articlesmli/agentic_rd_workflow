# mcp_server.py
from fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Clinical R&D Extension Server")

@mcp.tool()
async def fetch_hospital_site_registry(site_id: str) -> str:
    """Dynamically lookup active clinical trial site compliance and details."""
    # Simulated external registry lookup
    mock_db = {
        "SITE-001": "Hospital A: Certified for Phase III trials, max capacity 200.",
        "SITE-002": "Hospital B: Certified for Phase II/III trials, max capacity 150."
    }
    return mock_db.get(site_id, "Site ID not found in active hospital network registry.")

if __name__ == "__main__":
    mcp.run()
