#    Copyright 2015 Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

import six


@six.add_metaclass(abc.ABCMeta)
class ZmqPoller(object):

    @abc.abstractmethod
    def register(self, socket, recv_method=None):
        """Register socket to poll"""

    @abc.abstractmethod
    def poll(self, timeout=None):
        """Poll for messages"""

    @abc.abstractmethod
    def close(self):
        """Terminate polling"""

    def resume_polling(self, socket):
        """Resume with polling"""


@six.add_metaclass(abc.ABCMeta)
class Executor(object):

    def __init__(self, thread):
        self.thread = thread

    @abc.abstractmethod
    def execute(self):
        'Run execution'

    @abc.abstractmethod
    def stop(self):
        'Stop execution'

    @abc.abstractmethod
    def wait(self):
        'Wait until pass'