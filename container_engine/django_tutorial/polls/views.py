# Copyright 2015 Google Inc.
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
import logging
import random

from django.http import HttpResponse


def index(request):
    if random.randint(1,4) > 2:
      logging.error('about to crash!')
      raise ValueError('Oh no, an invalid value')

    logging.info('got request for root')
    logging.warn('AHHHHH got request for root')
    return HttpResponse("Hello, world, modified. You're at the polls index.")
