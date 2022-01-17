## Contributing to this Jupyter Book Course on Quantum Chemistry

1. Fork the repo by click on the `Fork` button in the top-right corner. This creates a new copy of this repo under your GitHub user account.
2. Clone the repo using git clone (for now the name of repository is IntroQM2022) using this link: https://github.com/QC-Edu/IntroQM2022.git

Once the repo is cloned, you need to do two things:
1. Create a new branch by issuing the command: `git checkout -b new_branch`
2. Create a new remote for the upstream repo with the command: `git remote add upstream https://github.com/QC-Edu/IntroQM2022`

In this case, "upstream repo" refers to the original repo you created your fork from. Also you can take a look at  "Workflow summary" section [here](https://www.neonscience.org/resources/learning-hub/tutorials/git-setup-remote)

Now, you can make changes to the file(s) you want to change.

##  Creating pull request
When changes are done, add, commit and push them using `git add`, `git commit` and `git push -u origin new_branch` commands respectively

Once you push the changes to your repo, find and click `Compare & pull request` button at your GitHub repo.

Open a pull request by clicking the `Create pull request button`. This allows us to review your contribution. 

## Build the book
1. Outside of the main folder run `jb build IntroQM2022`
2. Go to the main folder and than add, commit and push changes using `git add .`, `git commit`, `git push` respectively
3. Run `ghp-import -n -p -f _build/html`

Done!
