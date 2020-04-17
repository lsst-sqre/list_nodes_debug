#!/usr/bin/env python3
import kubernetes
import logging
import time
from kubernetes.client import CoreV1Api
from kubernetes.config import load_incluster_config, load_kube_config
from kubernetes.config.config_exception import ConfigException


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)
log.debug("Debug logging enabled.")
try:
    log.debug("Trying cluster config.")
    load_incluster_config()
except ConfigException:
    log.debug("Cluster config failed.  Trying Kubeconfig.")
    load_kube_config()
log.debug("Getting API.")
api = CoreV1Api()
log.debug("Listing node.")
nl = api.list_node(timeout_seconds=60)
if not nl:
    raise RuntimeError("Did not get node list!")
print("Nodelist: {}".format(nl))
log.debug("Sleeping 600s to let you play with the pod.")
time.sleep(600)
log.debug("Exiting.")
