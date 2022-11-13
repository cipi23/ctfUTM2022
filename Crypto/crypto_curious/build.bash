#!/bin/bash
set -ex

export FLAG=UTM{fr13ndly_70_b3661n3r5_17_15_1nd33d}
case $1 in
    clean)
        rm -rf ./distfiles
        ;;

    *)
        rm -rf ./distfiles
        mkdir -p ./distfiles
        python3 ./challenge/task.py > ./distfiles/output.txt
        cp ./challenge/task.py ./distfiles
        ;;
esac
