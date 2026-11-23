# 用本地预导入的 nginx 镜像（离线环境，避免从 Docker Hub 拉取失败）
# 教学提示：真实项目应先 docker pull 或用内网镜像仓库的地址
FROM nginx:base
COPY app/index.html /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
