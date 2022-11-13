#!/bin/bash
set -ex

export FLAG=UTM{17_41n7_7h47_345y_7h15_71m3_175_r0und_7w0} 
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
