import os

class GitError(Exception):
    pass

def downloadRepository(downloadDir: str, repoLink: str) -> bool:
    full_path = os.path.join(downloadDir, "template.txt")
    if not os.path.exists(full_path):
        try:
            with open(full_path, "w") as f:
                f.write("SubscriptionId: SUBSCRIPTION_ID")
        except:
            return False
    return True