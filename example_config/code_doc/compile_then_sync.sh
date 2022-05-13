echo "=== Current Folder ==="
echo `pwd`

# 编译
echo -e "\n\n=== Compile ==="
py /d/1_Workspace/mdpy/main.py -d ./doc --assets-repository-path . --assets-folder-path ./doc/assets
# 错误暂停
if [ $? -ne 0 ]; 
    then sleep 1e8; fi

# 同步
echo -e "\n\n=== Git ==="
git add .
git commit -m "Doc"
git pull --rebase
git push

echo success
sleep 10
