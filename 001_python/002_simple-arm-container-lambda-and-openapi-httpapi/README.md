## How to

1. setup docker

[Lima on macOS](https://github.com/lima-vm/lima)

```bash
limactl start template://docker --arch "aarch64" --cpus 2 --disk 10 --memory 2

# See last log displayed in limactl
docker context create ....
docker context user ....

# Edit ~/.zshrc
# add 「export DOCKER_HOST="unix:///Users/【UserName replace】/.lima/docker/sock/docker.sock"」
```

2. setup awssam

[AWS SAM Doc](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

3. sam build and Local start api

```bash
sam build && sam local start-api
```

4. local api request

```bash
curl localhost:3000/hello
```
