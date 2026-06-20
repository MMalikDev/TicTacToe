# ZSH Configs

export TERM=xterm-256color

# History
HISTFILE=~/.histfile
HISTSIZE=1000
SAVEHIST=$HISTSIZE
HISTDUP=erase
setopt appendhistory                    # Append new commands to the history file instead of overwriting it
setopt sharehistory                     # Share history instantly across all running Zsh sessions
setopt hist_ignore_space                # Ignore commands that start with a space (don’t save them)
setopt hist_ignore_all_dups             # Never save a command if it already exists anywhere in history
setopt hist_save_no_dups                # Don’t write duplicate commands to the history file
setopt hist_ignore_dups                 # Don’t record a command if it’s the same as the previous one
setopt hist_find_no_dups                # Skip duplicates when searching history (Ctrl-R, arrow keys)
setopt beep extendedglob nomatch notify # Enable beep, advanced globbing, error on unmatched globs, and job notifications
setopt correct                          # Auto correct spelling errors
unsetopt autocd                         # Disable auto‑cd so directory names don’t automatically change directories

# ZSH Plugins
ZINIT_HOME="${XDG_DATA_HOME:-${HOME}/.local/share}/zinit/zinit.git"
[ ! -d $ZINIT_HOME ] && mkdir -p "$(dirname $ZINIT_HOME)"
[ ! -d $ZINIT_HOME/.git ] && git clone https://github.com/zdharma-continuum/zinit.git "$ZINIT_HOME"
source "${ZINIT_HOME}/zinit.zsh"

HISTORY_SUBSTRING_SEARCH_HIGHLIGHT_FOUND=''
HISTORY_SUBSTRING_SEARCH_HIGHLIGHT_NOT_FOUND=''

zinit light zsh-users/zsh-history-substring-search
zinit light zsh-users/zsh-syntax-highlighting
zinit light zsh-users/zsh-autosuggestions
zinit light zsh-users/zsh-completions
zinit light Aloxaf/fzf-tab

# Keybindings
bindkey -e
bindkey "^L" clear-screen

bindkey '^[[D' backward-char
bindkey '^[[C' forward-char

bindkey '^[[1;5D' backward-word
bindkey '^[[1;5C' forward-word

bindkey '^[[H' beginning-of-line
bindkey '^[[F' end-of-line

bindkey '^[[1;5B' beginning-of-line
bindkey '^[[1;5A' end-of-line

bindkey '^J' kill-region
bindkey '^K' kill-line

bindkey '^?' backward-delete-char
bindkey '^[[3~' delete-char

bindkey '^H' backward-kill-word
bindkey '^[[3;5~' kill-word

bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down

# Completion Styling
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"
zstyle ':completion:*' menu no
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'
zstyle ':fzf-tab:complete:ls:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'
zstyle ':fzf-tab:complete:cp:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'
zstyle ':fzf-tab:complete:mv:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'
zstyle ':fzf-tab:complete:z:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'
zstyle ':fzf-tab:complete:eza:*' fzf-preview 'eza -1HAs type --icons --color=always $realpath'

# Shell Intergration
eval "$(fzf --zsh)"
eval "$(zoxide init zsh)"
[[ "$TTY" != /dev/tty* ]] && eval "$(starship init zsh)"

# Aliases
test -f ~/.aliases.sh && . ~/.aliases.sh

# Load Completions
autoload -Uz compinit
compinit
