from git import Git


def git_update(directory, repository):
    Git(directory).clone(f"git://{}")


if __name__ == '__main__':
    print_hi('PyCharm')

