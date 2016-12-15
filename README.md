# traffic_simulate
Here is for Gaussian and Self similarity module

##拓扑
仿真拓扑写在half_useful_topo.py文件中

##mininet部分
cli.py,net.py，mn三个文件是mininet中被修改的部分，前两个文件存放目录分别为/mininet/mininet，第三个文件存放目录为/mininet/bin
修改mininet后扩展了四条功能，分别是hostports,iperfmulti,onoffmulti,poissonmulti,他们的用法如下：
hostports 0.1(Gbit/s,bandwidth）：该命令可以限制主机h1到h100的出口速率，第一个参数为主机最大出口速率
iperfmulti 15(s,test_time):该命令可以让h1到h100向服务器主机打稳定的TCP流，第一个参数为稳定流的持续时间
onoffmulti 15(s,test_time) 1.2(alpha1) 1.3(alpha2):该命令可以让h1到h100向服务器主机打符合自相似规律的TCP流，第一个参数为打流持续时间，第二个参数为Pareto分布参数alpha
poissonmulti 15(s,test_time) 17(lambda1) 27(lambad2):该命令可以让h1到h100向服务器主机打符合MMPP规律的TCP流，第一个参数为打流持续时间，第二个参数为指数分布分布参数lambda

##端口配置部分
主机端口配置文件为host_port_config.sh，是mininet中hostports命令的基础
交换机端口配置文件为sw_port_config.sh，使用方法如下：
./sw_port_config.sh 1(switch name) 101(port number) 1000(us,limit) 10(Gbit/s,bandwidth)

##数据提取部分
负载率信息放在ifconfig.txt文件中，由load_s1.py文件提取
丢包率信息放在interfaces.txt文件中，由measure_s1.py文件提取

##Traffic Get
Using traffic_read.py,traffic_process.py,traffic_process2.py to get traffic information from rough data like Traffic_rough.txt
