# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
from django.apps import AppConfig
from restclients_core.dao import MockDAO


class PrereqMapConfig(AppConfig):
    name = 'prereq_map'

    def ready(self):
        prereq_mocks = os.path.join(os.path.dirname(__file__), "resources")
        MockDAO.register_mock_path(prereq_mocks)
