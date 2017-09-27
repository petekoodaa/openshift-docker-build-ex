# Openshift docker build exercise

Testing how to do OpenShift builds using the Docker strategy.

$ cat docker/Dockerfile | oc new-build . --name="hello-openshift" -D -
$ oc new-app --image-stream=hello-openshift
