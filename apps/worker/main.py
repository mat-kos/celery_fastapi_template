from src.app import create_app


app = create_app()


if __name__ == "__main__":
    app.worker_main([
        "worker",
        f"--loglevel={app.user_config.log_level}"        
    ]) 