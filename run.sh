#!/bin/bash

# set -e

source ./scripts/run.sh
# ---------------------------------------------------------------------- #
# Define Docker Variables
# ---------------------------------------------------------------------- #
declare -a reloads=(
    #
)

declare -a logs=(
    #
)

# ---------------------------------------------------------------------- #
# OPTIONS
# ---------------------------------------------------------------------- #
run_devcontainer(){
    load_env
    run_python_dev $@
    exit 0
}
run_locally(){
    load_env
    run_python $@
    exit 0
}
run_docker(){
    reload_services ${reloads[*]}
    handle_errors $?
    
    docker image prune -f
    # follow_logs ${logs[*]}
    exit 0
}

docker_exec(){
    set -f
    local input=$1
    local IFS=','
    local array=($OPTARG)
    
    docker exec -it python python3 main.py ${array[*]}
    exit 0
}
use_env_file(){
    [[ $(get_bool DEVCONTAINER) == "true" ]] && run_devcontainer $@
    [[ $(get_bool RUN_LOCAL) == "true" ]] && run_locally $@
    run_docker
}

# ---------------------------------------------------------------------- #
# Main Function
# ---------------------------------------------------------------------- #
main(){
    while getopts "e:dlch" OPTION; do
        case $OPTION in
            d) run_devcontainer $@  ;;
            l) run_locally $@       ;;
            c) run_docker           ;;
            e) docker_exec $OPTARG  ;;
            h) display_usage        ;;
            ?) display_usage        ;;
        esac
    done
    shift $((OPTIND -1))
    
    use_env_file $@
}

main $@
