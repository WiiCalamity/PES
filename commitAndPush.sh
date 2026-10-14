#!/bin/bash
oldName=`git config --global user.name`
oldEmail=`git config --global user.email`
myName="wiicalamity"
myEmail="wiicalamity@proton.me"

git config --global user.name "${myName}"
git config --global user.email "${myEmail}"

read -p "Commit message: " message
read -p "Confirm? (y/N): " confirm
[[ ${confirm} != "y" ]] && exit

git add .
git commit --message="${message}"
git push

git config --global user.name "${oldName}"
git config --global user.email "${oldEmail}"
exit
