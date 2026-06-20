# FROM mcr.microsoft.com/devcontainers/base:trixie AS build
FROM debian:trixie-slim AS build

# Install dependencies
RUN export DEBIAN_FRONTEND=noninteractive && apt update && apt install -y \
  bat \
  eza \
  fd-find \
  fzf \
  git \
  jq \
  ripgrep \
  starship \
  zoxide \
  zsh \
  rustup \
  python3 \
  nodejs \
  npm \
  sudo \
  && rm -rf /var/lib/apt/lists/*

# Create a non-privileged user 
RUN adduser --disabled-password --gecos "" dev
RUN adduser dev sudo && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# ------------------------------------------------------------ #

FROM archlinux:base AS base

RUN pacman-key --init

RUN pacman -Syu --noconfirm && \
  pacman -S --noconfirm \
  bat \
  eza \
  fd \
  fzf \
  git \
  helix \
  jq \
  less \
  openssh \
  ripgrep \
  starship \
  zellij \
  zoxide \
  zsh \
  rust \
  rust-analyzer \
  python \
  tombi \
  ruff \
  ty \
  nodejs \
  biome \
  bun \
  npm \
  prettier \
  shfmt \
  bash-language-server \
  dockerfile-language-server \
  svelte-language-server \
  tailwindcss-language-server \
  typescript-language-server \ 
  vscode-css-languageserver \ 
  vscode-eslint-language-server \
  vscode-html-languageserver \ 
  vscode-json-languageserver \ 
  yaml-language-server \ 
  sudo \
  && rm -rf /var/cache/pacman/pkg   

# Create a non-privileged user 
RUN groupadd -g 1000 dev && useradd -u 1000 -g dev -m dev
RUN echo "dev ALL=(ALL) NOPASSWD: /usr/bin/pacman" >> /etc/sudoers

# ------------------------------------------------------------ #

FROM base AS arch
USER dev

COPY --chown=dev:dev ./config /home/dev
RUN zsh /home/dev/.zshrc

ARG WORKSPACE_NAME
WORKDIR /workspaces/${WORKSPACE_NAME}
CMD ["sleep", "infinity"]

# ------------------------------------------------------------ #

FROM build AS dev
USER dev

COPY --chown=dev:dev ./config /home/dev
RUN zsh /home/dev/.zshrc

ARG WORKSPACE_NAME
WORKDIR /workspaces/${WORKSPACE_NAME}
CMD ["sleep", "infinity"]
