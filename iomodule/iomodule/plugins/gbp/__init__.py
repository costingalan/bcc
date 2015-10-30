# Copyright 2015 PLUMgrid
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

import bcc
import os

from iomodule.core import iomodule

_dir = os.path.dirname(__file__)

class GBP(iomodule.IOModule):
    _capabilities_ = ["ebpf"]
    _uuid_ = "1313597e-5d29-4358-934a-e5b561c4b812"

    def __init__(self, *args, **kwargs):
        super(GBP, self).__init__(*args, **kwargs)
        # self.b = bcc.BPF(os.path.join(_dir, "passthrough.c"))
        # self.pairs = self.b["pairs"]
        # self.fn = self.b.load_func("recv", self.b.SCHED_ACT)
        # self.half = None

    def _ifc_create(self, name):
        # (idx1, idx2) = self.mm().get_index_pair(name, self)
        # if self.half:
        #     self.pairs[self.pairs.Key(self.half)] = self.pairs.Leaf(idx1)
        #     self.pairs[self.pairs.Key(idx1)] = self.pairs.Leaf(self.half)
        #     self.half = None
        # else:
        #     self.half = idx1
        # return idx2
        pass

    def fd(self):
        return self.fn.fd

cls = GBP
