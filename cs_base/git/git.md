# git
> **[根本学习路径](https://git-scm.com/book/zh/v2)**

基本上是`文件未被跟踪`, `文件添加到暂存区`, `文件有改动`, `文件提交到分支上`
![流程图](https://git-scm.com/book/en/v2/images/lifecycle.png)
## 常用命令
- `git add .` # 添加所有的更新的文件到暂存区
- `git commit -m "update"`  # 将暂存区的内容全部更新到分支上 
- `git push origin branchName` # 本地分支同步到远程分支
- `git pull origin branchName` # 远程分支内容拉取到本地分支上
- `git checkout -b branchName` # 创建分支并切换到该分支
- `git branch -D branchName`  # 删除分支
- `git log --oneline`    # 打印分支的所有commit信息
## reset

### hard模式
- `git reset --hard HEAD~`  # 退回到分支上一次commit, 并且距离上次commit的更改的信息也都没了
```shell
echo "test" >> a.txt

git add .
git commit -m "update a.txt"

git reset --hard HEAD~

git status            
# 结果
On branch test
nothing to commit, working tree clean

ls | grep a.txt
# 结果为空
```

### soft 模式
- `git reset --soft HEAD~` # 退回到分支上一次commit, 并且距离上次commit的更改的信息已经被`git add .`了
```shell
echo "test" >> a.txt

git add .
git commit -m "update a.txt"

git reset --soft HEAD~

git status
# 结果
On branch test
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   a.txt

ls | grep a.txt
# 结果显示a.txt
```

### mixed 模式
- `git reset --mixed HEAD~` # 退回到分支上一次commit, 并且距离上次commit的更改的信息还在本地

```shell
echo "test" >> a.txt

git add .
git commit -m "update a.txt"

git reset --mixed HEAD~

git status
# 结果
On branch test
Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.txt

nothing added to commit but untracked files present (use "git add" to track)

ls | grep a.txt
# 结果显示为 a.txt
```

## rm
- `git rm --cached fileName` # 将已经提交到暂存区的文件 删除(本地还有这个文件)
- `git rm -f fileName` # 将已经提交到暂存区的文件 删除(本地没有这个文件)

## merge
- `git checkout branchName` # 切换到工作分支
- `git merge srcBranch` # 将`srcBranch`的内容copy到当前分支


## tag
- `git tag -a tagName commitId` # 打tag
- `git tag -l` # 查看本地所有的tag
- `git tag -d tagName` # 删除本地tag
- `git push origin tagName` # 上传远程分支
- `git push origin --delete tagName`


## 待了解的高级技巧
- [二分查找bug在哪个版本](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E4%BD%BF%E7%94%A8-Git-%E8%B0%83%E8%AF%95)