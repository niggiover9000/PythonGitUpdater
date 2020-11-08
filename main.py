from git import Git
from pythonping import ping


def git_update(directory, repository):
    try:
        Git(directory).clone(repository)
    except C


def ping_server(ip):
    print("Trying to reach update server...")
    request = ping(ip, timeout=2)
    request = str(request)
    if request.startswith("Request timed out"):
        raise TimeoutError("Could not reach update server. Please make sure you are connected to the internet.")
    else:
        return True


if __name__ == '__main__':
    if ping_server("github.com") is True:
        print("Connected to the update server. Trying to clone.")
        git_update(None, "https://github.com/niggiover9000/PythonGitUpdater.git")

