# class.getResource()和class.getClassLoader().getResource()的区别
```
class.getResource("") // 路径是当前类的位置
class.getResource("/") // 路径是当前项目的根目录
class.getClassLoader().getResource() // 路径同 class.getResource("/")
```