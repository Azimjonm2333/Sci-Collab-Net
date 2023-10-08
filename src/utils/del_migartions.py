import os

def clean_migrations(path):
    for root, dirs, files in os.walk(path):
        if "migrations" in dirs:
            migrations_dir = os.path.join(root, "migrations")
            for filename in os.listdir(migrations_dir):
                if filename.endswith(".py") and filename != "__init__.py":
                    file_path = os.path.join(migrations_dir, filename)
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")

if __name__ == "__main__":
    src_apps_path = "src/apps/"
    clean_migrations(src_apps_path)
