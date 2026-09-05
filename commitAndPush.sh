#!/bin/bash
oldName=`git config --global user.name`
oldEmail=`git config --global user.email`
myName="wiicalamity"
myEmail="wiicalamity@proton.me"
git config --global user.name "${myName}"
git config --global user.email "${myEmail}"
echo updated stuff

read -p "Commit message: " message
read -p "Confirm? (y/N): " confirm
[[ ${confirm} != "y" ]] && exit

git add .
echo git added
git commit
#git commit --message=${message}
echo git commited
git push
echo git pushed!!

git config --global user.name "${oldName}"
git config --global user.email "${oldEmail}"
