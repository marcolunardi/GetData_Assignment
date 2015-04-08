# Pull Requests


### Objectives:

 * Keep in sync by pulling from an "upstream" remote.
 * Use pull requests to submit class work.
 * Get feedback and discuss work on GitHub.
 * Improve work and re-submit as needed.


### Ideas:

 * You can `pull` commits from a remote repository to your local one to keep it in sync. (Equivalently, `fetch` and then `merge`.)
 * Local git repositories can reference more than one remote.
 * On GitHub, you can submit changes by asking that they be pulled in by someone else - this is called a pull request.


### Process:

 * Fork the class repository.
 * Clone your fork.
 * If there are changes in the original, how do you get them? You need to tell your local repo that it can also get updates from the original:

```bash
# add remote with the appropriate reference
git remote add upstream ...

# display configured remotes
git remote -v

# pull in changes
git pull upstream master
```

 * Make local changes by adding a directory in [test_pr/](test_pr/), putting a file in it, committing the change, and pushing it to your fork.
 * Submit a pull request and feel the joy of modern technical collaboration.
