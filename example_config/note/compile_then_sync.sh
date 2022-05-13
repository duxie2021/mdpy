echo "=== Current Folder ==="
echo `pwd`

# 编译
echo -e "\n\n=== Compile ==="
py ../mdpy/main.py -d .
# 错误暂停
if [ $? -ne 0 ]; 
    then sleep 1e8; fi

# 同步
echo -e "\n\n=== Git ==="
git add .
git commit -m "Sync by robot"
git pull --rebase
git push

echo success
sleep 10
