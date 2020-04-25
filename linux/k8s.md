# k8s

## 容器相关的技术
- namespace 是用来进程之间隔离的
- cgroup用来限制资源利用率
- chroot是保证文件系统的隔离的 
- changeset 分层复用

## 为什么大量使用k8s
- 调度 (根据cpu 和 memory等信息 选择合适的进行placement) 
- 自修复 (对宿主机健康检查, 宿主机出现问题会进行迁移)
- 水平伸缩 (对忙的业务进行扩容)

## 结构 
- master & client
  - master
    - 有 apiserver, controller, scheduler, etcd
  - Node
    - kubelet, Pod, Storage Plugins, Network Plugins, Kube-proxy


