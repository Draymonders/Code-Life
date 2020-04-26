## 添加用户
```shell
useradd -m -s user/bin/zsh test
```
- `-m` 是自动创建`/home/test`作为`test`的用户目录
- `-s` 是修改用户登录的默认shell


## 修改密码
```shell
passwd test
```