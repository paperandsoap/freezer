"""Freezer restore.py related tests

(c) Copyright 2014,2015 Hewlett-Packard Development Company, L.P.
(c) Copyright 2016 Hewlett-Packard Enterprise Development Company, L.P
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""
import unittest

from freezer.openstack import restore
from freezer.tests import commons


class TestRestore(unittest.TestCase):

    def test_restore_cinder_by_glance(self):
        backup_opt = commons.BackupOpt1()
        ros = restore.RestoreOs(backup_opt.client_manager, backup_opt.container)
        ros.restore_cinder_by_glance(35, 34)

    def test_restore_cinder(self):
        backup_opt = commons.BackupOpt1()
        ros = restore.RestoreOs(backup_opt.client_manager, backup_opt.container)
        ros.restore_cinder(35, 34)

    def test_restore_nova(self):
        backup_opt = commons.BackupOpt1()
        ros = restore.RestoreOs(backup_opt.client_manager, backup_opt.container)
        ros.restore_nova(35, 34)
