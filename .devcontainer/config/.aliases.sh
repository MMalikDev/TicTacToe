# Bash
alias ag="alias | rg"                           # Find alias
alias uel='find . -type f -exec dos2unix {} \;' # Convert end of line char to unix

# IDE
alias hx='helix'

# Project
alias init="~/sh/init.sh" # Initialize project
alias r="bash run.sh"     # Run project
alias re="bash reset.sh"  # Reset project
alias run="re && r"       # Reset & run project

# Docker
alias de="docker exec -it" # Run command in docker container

alias dcb="docker compose build"          # Build docker services imagas
alias dcc="docker compose config"         # Check docker config
alias dcd="docker compose down --rmi all" # Shutdown docker services
alias dcp="docker compose pull"           # Pull all compose images
alias dcu="docker compose up -d"          # Turn on docker services

alias dpb="docker builder prune"        # Prune docker builds
alias dp="echo y | docker system prune" # Prune docker system

# Git
alias gf="git log --all --graph"                                # Git log verbose
alias glf="git log --oneline --all --graph"                     # Git log simple verbose
alias gl="git log --oneline"                                    # Git log
alias gls='git log -1 --stat'                                   # Show last commit summary
alias gn='echo $(basename `git rev-parse --show-toplevel`).git' # Get current git repo name

alias gprivate='git remote add origin'   # Add private remote
alias gpublic='git remote add portfolio' # Add public remote
alias gv="git remote -v"                 # Show verbose remote

alias ga="git add ."                         # Git add changes
alias gah="git add --patch"                  # Git add hunks manually
alias gc="git commit -m"                     # Git commit
alias gd="git diff --compact-summary HEAD~1" # Git diff last commit
alias gds="git diff --staged"                # Git diff staged changes
alias gs="git status --short"                # Git status

alias gpf="git push -f"  # Git push force
alias gp="git push"      # Git push
alias gr="git rebase -i" # Git rebase (gr head~#)

alias g1="gac 'Initial Commit'"                          # Git initial commit
alias gac="ga && gc"                                     # Git add and commit
alias gam="ga && git commit --amend --no-edit"           # Git amend changes
alias gap="gmc && gpf"                                   # Git amend and force push
alias gftc="git fetch"                                   # Fetch latest changes
alias gg="git pull"                                      # Pull latest changes into repo
alias gmc="ga && git commit --amend --no-edit && git gc" # Git amend changes & clean git
alias gu="gp -u origin"                                  # Set upstream for new branch

alias gb="git branch"                           # Show git branches
alias gcount="git rev-list --count --all"       # Git commit count
alias ghc="git remote set-head origin -d"       # Clear remote head
alias gi="git init"                             # Init git repo
alias gitcb="code /etc/profile.d/git-prompt.sh" # Git bash edit

# System
alias ls1='lsi -1As type'              # List ls
alias ls='eza'                         # Better ls
alias lsi='eza --color=always --icons' # Icons ls
alias lsl='lsi -lAs type'              # Detailed ls

alias cd='z'                                  # Better cd
alias cls="clear"                             # Habit accommodation
alias diffs="diff -y --suppress-common-lines" # Show deferences in columns
alias k="exit 0"                              # Close terminal
alias keygen="ssh-keygen -t ed25519"          # Create new ssh key using ed25519
alias size="du -hd 1 . | sort -hr"            # List folder sizes

alias distro='lsb_release -d'                        # Show Distro (Alt)
alias os='rg ^ID= /etc/os-release | cut -d "=" -f 2' # Show Distribution

# Python
alias py="python3"     # Python3 abbreviation
alias python3="python" # Windows alias

alias pipf="pip freeze -l"                         # Show pip packages
alias pipl="pip list"                              # List pip packages
alias pipr="pip install -r"                        # Install from file
alias pipup="python3 -m pip install --upgrade pip" # Upgrade pip

alias venvdel='find -type d -name "*.venv*" -exec rm -rf {} \;' # Delete all venv
alias venvls="find -type d -name '*.venv*'"                     # Show all venv
alias venvnew="python3 -m venv .venv"                           # Create venv
alias venv="source .venv/bin/activate"                          # Use venv (windows)

alias pyclear='find -type d -name "*pycache*" -exec rm -rf {} \;' # Delete all pycache

# Javascript
alias nodedel='find -type d -name "*node_modules*" -exec rm -rf {} \;' # Delete all node_modules
alias sveltedel='find -type d -name "*.svelte*" -exec rm -rf {} \;'    # Delete all .svelte

# Package Manager
alias get="sudo apt install"                                                 # Install Packages
alias show="apt show"                                                        # Packages Description
alias update="sudo apt update && sudo apt upgrade -y && sudo apt autoremove" # Update Packages

alias get="sudo pacman -S"      # Install Packages
alias show="pacman -Ss"         # Packages Description
alias update="sudo pacman -Syu" # Update Packages

# Fuzzy Finder
alias fzp="fzf --preview='bat --color=always {}'"
alias zls='zellij attach $(zellij ls | fzf --height=10 --ansi | cut -d " " -f 1)'
