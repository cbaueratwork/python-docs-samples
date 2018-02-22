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
import random

import logging
import logging.handlers
import google.cloud.logging as gcp_logging

from google.oauth2 import service_account
from django.http import HttpResponse

cred = service_account.Credentials.from_service_account_file('./logging-key.json')
gcp_logging_client = gcp_logging.Client(project='gke-python-2', credentials=cred)
handler = gcp_logging_client.get_default_handler()
logger = logging.getLogger('myapp-logs')
gcp_logger = gcp_logging_client.logger('sd-logs')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def index(request):
    if random.randint(1,4) > 2:
      logger.error('about to crash!')
      gcp_logger.log_text('stackdriver is about to crash', labels={'test': 'failure'})
      raise ValueError('Oh no, an invalid value')

    logger.info('it appears to be working')
    gcp_logger.log_text('it appears to be working - sd', severity='INFO')
    logger.warn('yikes this is a warning')
    gcp_logger.log_text('yikes this is a warning - sd', severity='WARNING')
    return HttpResponse("Hello, world, customized. You're at the polls index.")
