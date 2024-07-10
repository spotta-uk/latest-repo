import git


def check_and_update_repo(repo_path):
    try:
        # Open the repository
        repo = git.Repo(repo_path)

        # Check if the repository is dirty (i.e., has uncommitted changes)
        if repo.is_dirty(untracked_files=True):
            print(f"Repository at {repo_path} has uncommitted changes.")
            return

        # Fetch the latest changes from the remote
        print(f"Fetching updates for the repository at {repo_path}...")
        repo.remotes.origin.fetch()

        # Compare local and remote commits
        local_commit = repo.commit('master')
        remote_commit = repo.remotes.origin.refs.master.commit

        if local_commit == remote_commit:
            print("The repository is up-to-date.")
        else:
            print("The repository is not up-to-date. Pulling the latest version...")
            repo.remotes.origin.pull()
            print("Repository has been updated.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    repo_path = './'
    check_and_update_repo(repo_path)


