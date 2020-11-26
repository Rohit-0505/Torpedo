#!/usr/bin/python3

# Copyright 2017 AT&T Intellectual Property. All other rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess
import urllib3
import yaml

from kubernetes import client, config, utils


urllib3.disable_warnings()


class Kubernetes(object):

    def __init__(self, **kwargs):
        if os.path.exists(os.environ['KUBECONFIG']):
            config.load_kube_config()
        else:
            config.load_incluster_config()
