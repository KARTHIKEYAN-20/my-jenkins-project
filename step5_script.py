import os

REPO_URL = "https://github.com/KARTHIKEYAN-20/my-jenkins-project.git"
CLONE_DIR = "my-jenkins-project"

# Remove existing directory if it exists
if os.path.exists(CLONE_DIR):
    os.system(f"rm -rf {CLONE_DIR}")

# Clone the repository
os.system(f"git clone {REPO_URL} {CLONE_DIR}")

print("✅ Repository cloned successfully!")
