# Backend Repository

## 接口说明
### 接口规范
末尾必须加'/', 否则请求会失败
### user/
#### login/
用户登录, 包含信息为username和password
#### 

## 运行环境和启动说明
### mysql
mysql 当中应该有名为brog_db的数据库
### 库依赖
部署时将用venv(虚拟环境)进行打包
### 启动
shell进入本菜单, python run.py 启动即可

## 开发规范
### 组件化
#### import
任何非package的内容, import使用相对路径, 这样依赖关系的时候更加清楚
#### 组件化与是否需要__init__.py的问题
全部一个文件夹都视为单纯的文件夹, 换言之, 不添加__init__.py使它变成包
事实上这种操作是因为架构考虑得不成熟而导致的, 它的目的是为了避免循环import带来的问题