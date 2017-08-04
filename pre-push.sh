#!/usr/bin/env bash

# Check if pushing JAVA files. If so, check if pushing tests

# has_java="git diff --stat --cached origin/master | grep \"src\/main.*\.java\""
# has_test="git diff --stat --cached origin/master | grep \"src\/test.*\.java\""

# exit_val=0

# if eval $has_java; then
#     if eval $has_test; then
#         :
#     else
#         echo "*** NO TESTS WERE FOUND WHILE PUSHING JAVA CODE ***"
#         read -n1 -p "Do you want to CONTINUE pushing? [Y/n]" doit < /dev/tty
#         case $doit in  
#             n|N) exit_val=1 ;; 
#             y|Y) exit_val=0 ;;
#             *) exit_val=0 ;;
#         esac
#     fi
# fi

# Execute the tests
# gradle test

# exit $exit_val

exit 1