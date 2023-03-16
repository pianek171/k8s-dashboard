from kubernetes import client, config
from flask import Flask

#LOAD KUBECONFIG
config.load_kube_config()
# API CLIENT
api = client.CoreV1Api()


print("Listing pods with their IPs:")
ret = api.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))