import os
from pathlib import Path


base_dir = Path(__file__).resolve().parent

class config:
    secret_key= os.environ.get("secret_key","key123")
    sqlalchemy_database_url = os.environ.get("database_url","splite:///seloedu.db")
    sqlalchemy_track = False

    upload_loader = str(base_dir/"static"/"uploads")
    max_contenr_length = 4 *1024 * 1024
    allowed_image_extentions = ("png","jpg","jpeg","gif")
    thumbnail_size = (200,200)