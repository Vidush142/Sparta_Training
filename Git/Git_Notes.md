# Git and GitHub Notes 

## Version Control
 - For any situation where content is created
   - Remembers each version
   - Provides history of all changes
   - Can go back to earlier version
 - Version control can provide off-site copy of data
 - Version control supports collaboration

## Git
 - Git is a version control system
 - It is fast, modern and fully featured
 - Most popular VCS
 - Open source and free
 - Provides version history
 - Distributed
   - Can have local copy of data
   - And optional remote copy
 
### What is provided with Git?
 - Git comes with a command-line user interface called Git Bash
 - Git Server can be used to copy data
 - Most people use internet solutions eg. GitHub, GitLab, BitBucket
 - GUI can also be used e.g. GitHub Desktop
 - A directory/folder controlled by Git is called a repository

### Installing Git
 - Download Git using the following link: https://git-scm.com/downloads
 - Git can be installed on Windows, Mac and Linux systems.
 - Once installed change current directory to the directory you want 
to use as your Git repository and use the lines of code below to set 
up and initialise git repository:

``` 
   git config --global user.name
   git config --global user.email
   git init
``` 
### Commiting changes
 - Once changes have been made to the Git repository, these changes
needs to nbe commited.
 - Adding changes to Git repository consists of three stages <br>

![Image showing three stages of commiting files to Git](https://git-scm.com/book/id/v2/images/lifecycle.png)
 
 - Following lines of code can be used to commit changes after the changes are made:
```
git add file_name or git add --all (for multiple files)
git commit -m "commit message"
```
 - Commit message must be brief and precise
 - Following code can be used to check commit stage of files:
```
git status
```

### Copying to GitHub
 - GitHub is a web platform to store, manage and share files
 - It uses Git to provide version control
 - Repositories can be created on GitHub and copied to local system using following code
```
git clone [url-for-repo]
```
 - Local repository can be pushed to Github using following code:
```
git push origin main
```
 - Following code can be used to copy newer version of files from GitHub repo to local repo
```
git pull
```
 - Ensure not to upload secure information to GitHub repo


## Collaborative Git
### Adding collaborators on GitHub
 - Go to repo settings and collaborators to add new collaborators

### Branch Structure
 - Main branch contains fully tested and working code. 
 - Dev branch contains code changes made by development team.
 - Feature branch is the one where developers should work on.
### Why do we need branches
 - To ensure there is fully working version of code without conflicts.
### Working with branches
 - Following lines of code can be used to:
   - Create a new branch
   - Switch to the new branch
   - Merge branch to main branch once changes have been made
```
 git branch branch_name
 git checkout branch_name
 git merge branch_name
```
### Git Workflow
#### Git Authority (Auth)
Responsible for:
 - Creating the repo on their own GitHub account.
 - Creating a new dev branch.
 - Adding branch protection rules to the main and dev branches.
 - Requiring reviewers for merging to main or dev.
 - Creating the initial folder structure for the project.
 - Setting the dev branch as the default.

#### Team member
Responsible for:
 - Clone the project locally.
 - Create their own feature/developer branches.
 - Develop all code on these branches.
 - Never code directly on main or dev branch.
 - Commit locally at frequent intervals.
 - Push updates to GitHub.

Overall Workflow:
 - Update feature branch.
 - Switch to dev branch.
 - Use git pull to sync with remote dev branch.
 - Resolve merge conflicts.
 - Merge changes to dev branch:
   - Resolve merge conflicts
   - Check everything works
   - Commit changes
   - Push feature branch to GitHub
 - Open pull request
   - Choose the reviewers
   - Reviewers will look at updates, add any comments
   - If everything is approved, complete pull request
   - If changes required, make them locally on feature branch, commit and push to remote, complete pull once approved
