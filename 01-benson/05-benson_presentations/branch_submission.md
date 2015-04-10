# Git Branches and Submitting on GitHub


### Objectives:

 * Use git branches to work on specific topics
 * Use pull requests from your branches to submit, discuss, and update work


### Ideas:

 * Git commits have "ancestors," typically forming a long chain
 * A "branch" refers to one line of git ancestry
 * The "master" branch is the default and often main branch for a repo
 * You can organize new work in a "topic branch"


### Process:

#### This is a recipe for a new challenge (etc.) submission

First, get into the right directory (any directory in your local repository) and make sure you're on the master branch:

    git checkout master

Get up to date with the "official" repo:

    git pull upstream master

Create a new branch to use:

    git checkout -b benson_challenges

Work on some files (or add files from elsewhere) and make commits:

    cp ~/my_great_file.py ./correct/path/aaron/
    git add ./correct/path/aaron/my_great_file.py
    git commit -m "initial version"

Push your branch to your fork on GitHub:

    git push origin benson_challenges

Now you can go to the GitHub interface and make a pull request. You can continue to make commits on the `benson_challenges` branch until everything is good and can be merged. But don't forget what branch you're on! If you aren't working on `benson_challenges` any more, it's good to switch back to `master`:

    git checkout master
