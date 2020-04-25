# k8s
- 本内容摘抄自 《kubernetes in action中文版》

## 使用k8s & docker
- 拉取并且运行任何公开的镜像。
- 把应用打包成容器镜像, 并且推送到远端的公开镜像仓库让大家都可以使用。
- 进入运行中的容器并检查运行环境。
- 为 kubect1 命令行工具设置别名和 tab 补全。
- **在 Kubernetes 集群中列出查看节点、 pod、 服务和 ReplicationController**
- **在 Kubernetes 中运行容器并可以在集群外访问。**
- 了解 pod、 ReplicationController 和服务是关联的基础场景。
- 通过改变 ReplicationController 的复本数对应用进行水平伸缩。


## pod
- 如何决定是否应将某些容器组合在一个pod中。
- pod可以运行多个进程, 这和非容器世界中的物理主机类似。
- 可以编写 YAML 或 JSON 描述文件用于创建 pod, 然后查看pod的情况及其当前状态。
- 使用标签来组织 pod, 并且一次在多个pod上执行操作。
- 可以使用节点标签将 pod 只调度到提供某些指定特性的节点上。
- 注解允许入们,工具或库将更大的数据块附加到pod 。
- 使用 kubectl explain 命令快速查看任何 Kubernetes 资源的信息。

## 副本机制
- 使用**存活探针**,让Kubernetes在容器不再健康的情况下立即重启它(应用程序定义了健康的条件)。
- 不应该直接创建pod, 因为如果它们被错误地删除,它们正在运行的节点异常,或者它们从节点中被逐出时, 它们将不会被重新创建。
- ReplicationController始终保持所需数量的pod副本正在运行。
- 水平缩放pod与在ReplicationController上更改所需的副本个数一样简单。
- pod不属千ReplicationController, 如有必要可以在它们之间移动 。
- ReplicationController将从pod模板创建新的pod。更改模板对现有的pod没有影响。
- ReplicationController 应该替换为 ReplicaSet 和Deployment,它们提供相同的能力, 但具有额外的强大功能。
- ReplicationController 和 ReplicaSet 将 pod 安排到随机集群节点, 而 DaemonSet 确保每个节点都运行一个 DaemonSet 中定义的pod实例。
- 执行批处理任务的 pod 应通过 Kubernetes Job 资源创建, 而不是直接或通过 ReplicationController 或类似对象创建。
- 需要在未来某个时候运行的 Job 可以通过 CronJob 资源创建。

---- 当前看到了4.2节