# Copyright 2021 Peng Cheng Laboratory (http://www.szpclab.com/) and FedLab Authors (smilelab.group)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import unittest

from fedlab_core.network import DistNetwork


class NetworkTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.cnet = DistNetwork(address=("localhost", "12345"), world_size=1, rank=0)
        self.cnet.init_network_connection()

    def tearDown(self) -> None:
        self.cnet.close_network_connection()

    def test_(self):
        self.cnet.show_configuration()