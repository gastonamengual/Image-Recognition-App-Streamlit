from dataclasses import dataclass


@dataclass
class _Settings:
    RENDER_DOCKER_BASE_URL = "https://gamr-backend-service-vercel.onrender.com"
    VERCEL_BASE_URL = (
        "https://gamrbackendservice-93u32xecj-gastonamenguals-projects.vercel.app"
    )
    LOCAL_BASE_URL = "http://localhost:8080"


# streamlit run __main__.py --server.runOnSave true

Settings = _Settings()
