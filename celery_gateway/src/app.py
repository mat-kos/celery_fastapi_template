import importlib
from fastapi import FastAPI
from .config import AppConfig, routers_paths, wire_packages
from .containers import AppContainer


def _attach_routers(app: FastAPI, routers_paths: list[str]):
    for path in routers_paths:
        router_path, router_name = path.rsplit(".", 1)
        router = importlib.import_module(router_path).__getattribute__(router_name)
        app.include_router(router)


def _setup_dependency_injector(config: AppConfig):
    app_container = AppContainer()
    app_container.config.from_pydantic(config)
    app_container.wire(packages=wire_packages)
    

def _build_server_config(config: AppConfig) -> dict:
    return {
        "port": config.port,
        "host": config.host,
    }


def create_app() -> tuple[FastAPI, dict]:
    config = AppConfig()
    app = FastAPI()
    _setup_dependency_injector(config)
    _attach_routers(app, routers_paths)
    return app, _build_server_config(config)