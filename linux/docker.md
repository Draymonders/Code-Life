# Docker
docker 需要注意挂载目录的权限问题

## docker commit 
把现有运行的container保存为image
```
commit      Create a new image from a container's changes

docker commit ${container_id} ${image_name}
```

- 演示
```
CONTAINER ID        IMAGE               COMMAND
bc74b9c9a79d        hello-world         "/hello"

# 运行命令
docker commit bc74b9c9a79d hello
# 查看镜像
docker images | grep hello

REPOSITORY               TAG                 IMAGE ID
hello                    latest              1942aeff4eaa
```


## docker save / load
现有的image 与 file的转换
```
docker save ${image_id} > image.tar

docker load < image.tar
```


## docker run
- `-it`参数, 就是分配一个`tty`终端,并且可交互
- `--link`参数 Add link to another container (<name or id>:alias or <name or id>)