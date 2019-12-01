#!/bin/bash
git add .
echo "Commit Message?"
read message
git commit -m $message
git push -u origin master

hugo
cd public
git add .
git commit -m $message
git push origin master
cd ..