# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
#
# Copyright 2022 The NiPreps Developers <nipreps@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# We support and encourage derived works from this project, please read
# about our expectations at
#
#     https://www.nipreps.org/community/licensing/
#
__packagename__ = "nibrex"
__copyright__ = "2022, The NiPreps developers"
try:
    from ._version import __version__
except ModuleNotFoundError:
    from pkg_resources import get_distribution, DistributionNotFound

    try:
        __version__ = get_distribution(__packagename__).version
    except DistributionNotFound:
        __version__ = "unknown"
    del get_distribution
    del DistributionNotFound

