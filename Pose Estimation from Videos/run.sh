docker build -t pose-est -f docker/Dockerfile .
docker run --runtime=nvidia -it -p 8888:8888 -v "$(pwd):/pose_est/" pose-est

