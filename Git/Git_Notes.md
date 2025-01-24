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
 - GUI can also be used eg GitHub Desktop
 - A directory/folder controlled by Git is called a repository

### Installing Git
 - Download Git and install it
 - Set up config parameters:
   - user.name
   - user.email
   - init.defaultBranch

### Creating Repo and Copying to Github
 - Git init to initialise the repo
 - Git add to add files to staging process
 - Git commit -m "message" to commit to git
 - Git push origin master to copy local repo to remote
 - Ensure not to upload secure information to GitHub repo
 - git ls-files show information about files

### Copying from GitHub to local
 - git clone *URL* to copy repository to local system
 - git pull to get newer version of code from remote repo