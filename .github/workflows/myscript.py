import os

good_hash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad_hash = "HEAD"
command = "python manage.py test"

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system(f"git bisect run {command}")
os.system("git bisect reset")