echo registry.cn-beijing.aliyuncs.com/pspython/demo:$1
docker build -t registry.cn-beijing.aliyuncs.com/pspython/demo:v0.01 .
docker push  registry.cn-beijing.aliyuncs.com/pspython/demo:v0.01
echo  registry.cn-beijing.aliyuncs.com/pspython/demo:$1