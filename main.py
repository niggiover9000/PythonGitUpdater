from git import Git


def git_update(directory, repository):
    Git(directory).clone(repository)


if __name__ == '__main__':
    git_update(None, "https://github.com/niggiover9000/PythonGitUpdater.git")

