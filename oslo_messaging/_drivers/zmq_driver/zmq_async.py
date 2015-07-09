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

import logging

from oslo_utils import importutils

from oslo_messaging._i18n import _LE

LOG = logging.getLogger(__name__)

green_zmq = importutils.try_import('eventlet.green.zmq')


def import_zmq():
    imported_zmq = green_zmq or importutils.try_import('zmq')
    if imported_zmq is None:
        errmsg = _LE("ZeroMQ not found!")
        LOG.error(errmsg)
        raise ImportError(errmsg)
    return imported_zmq


def get_poller():
    if green_zmq:
        from oslo_messaging._drivers.zmq_driver.poller import green_poller
        return green_poller.GreenPoller()
    else:
        from oslo_messaging._drivers.zmq_driver.poller import threading_poller
        return threading_poller.ThreadingPoller()


def get_reply_poller():
    if green_zmq:
        from oslo_messaging._drivers.zmq_driver.poller import green_poller
        return green_poller.HoldReplyPoller()
    else:
        from oslo_messaging._drivers.zmq_driver.poller import threading_poller
        return threading_poller.ThreadingPoller()


def get_executor(method):
    if green_zmq is not None:
        from oslo_messaging._drivers.zmq_driver.poller import green_poller
        return green_poller.GreenExecutor(method)
    else:
        from oslo_messaging._drivers.zmq_driver.poller import threading_poller
        return threading_poller.ThreadingExecutor()