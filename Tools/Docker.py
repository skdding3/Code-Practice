docker image pull 이미지이름:tag // 이미지 불러오기

docker image rm 이미지이름 // 이미지 제거

docker image rmi 이미지id // 이미지 아이디로 제거

docker ps // 작동중인 컨테이너 확인

docker ps -a // 모든 컨테이너 확인

docker rm 컨테이너 id, 컨테이너id // 컨테이너 여러개 삭제가능

docker container rm `docker ps -a -q` // 전체삭제

docker inspect 이미지이름 // 환경변수 등 확인 가능

// 컨테이너 RUN
docker container run [options] IMAGE [command] [arg...]
// 예시
docker container run -it --name myName -e NAME=John -e AGE=20 [docker/images:tag] [command:python/bash]
exit // 컨테이너 종료

ctrl+P,Q // 종료없이 나오기
docker start myName // 컨테이너 실행

docker attach myName // 컨테이너 진입