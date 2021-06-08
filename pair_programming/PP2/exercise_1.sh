#!/bin/bash

read -r -p 'File to commit: ' file
git add $file
git status

read -r -p 'Do you wish to commit? ' varCommit

if [ $varCommit == 'N' ]; then
	git restore --staged $file
	exit 1
elif [ $varCommit == 'Y' ]; then
	read -r -p 'Enter commit message: ' msgCommit
	git commit -m $msgCommit
	git status
fi

echo 'Do you wish to push?'
read varPush

if ['$varPush'='N']; then
	git reset --soft HEAD^
	git restore --staged $file
	exit 1
elif ['$varPush'='Y']; then
	echo "Trying to push '$varCommit'..."
	git push
fi
exit 0
