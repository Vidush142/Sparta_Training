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
 - Download Git and install it
 - Set up config parameters:
   - user.name
   - user.email
   - init.defaultBranch

### Creating Repo and Copying to GitHub
 - Git init to initialise the repo
 - Git add to add files to staging process
 - Git commit -m "message" to commit to git
 - Git push origin master to copy local repo to remote
 - Ensure not to upload secure information to GitHub repo
 - git ls-files show information about files

### Copying from GitHub to local
 - git clone *URL* to copy repository to local system
 - git pull to get newer version of code from remote repo

### Collaborative Git
 - Go to repo settings and collaborators to add new collaborators

### Branch Structure
 - Main branch contains fully tested and working code. 
 - Dev branch contains code changes made by development team.
 - Feature branch is the one where developers should work on.
### Why do we need branches
 - To ensure there is fully working version of code without conflicts.
### Git Workflow
#### Git Authority (Auth)
Responsible for:
 - Creating the repo on their own GitHub account
 - Creating a new dev branch
 - Adding branch protection rules to the main and dev branches
 - Requiring reviewers for merging to main or dev
 - Creating the initial folder structure for the project
 - Setting the dev branch as the default

#### Team member
Responsible for:
 - Clone the project locally
 - Create their own feature/developer branches
 - Develop all code on these branches
 - Never code directly on main or dev branch
 - Commit locally at frequent intervals
 - Push updates to GitHub

Overall Workflow:
 - Update feature branch
 - Switch to dev branch
 - Use git pull to sync with remote dev branch
 - Merge conflicts
 - Merge changes to dev
   - Merge conflicts
   - Check everything works
   - Commit changes
   - Push feature branch to GitHub
 - Open pull request
   - Choose the reviewers
   - Reviewers will look at updates, add any comments
   - If everything is approved, complete pull request
   - If changes required, make them locally on feature branch, commit and push to remote, complete pull once approved
