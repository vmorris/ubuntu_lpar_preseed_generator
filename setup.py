#Copyright 2017 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(name='ubuntu_lpar_preseed_generator',
      version='0.1',
      description='Ubuntu installation preseed generator fro s390x LPAR',
      url='http://github.com/vmorris/ubuntu_lpar_preseed_generator',
      author='Vance Morris',
      author_email='vmorris@us.ibm.com',
      license='Apache 2.0',
      packages=['ubuntu_lpar_preseed_generator', 'jinja2' ],
      zip_safe=False)
