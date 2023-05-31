import os
from src.app import create_app


app = create_app()


if __name__ == "__main__":
    app.worker_main([
        "worker",
        f"--loglevel={app.user_config.log_level}",
        f"--uid={os.environ.get('DOCKER_CELERY_UID', 0)}", # for docker non root user
        f"--gid={os.environ.get('DOCKER_CELERY_GID', 0)}", # for docker non root user       
    ]) 