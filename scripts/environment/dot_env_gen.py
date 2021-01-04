#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import chevron

def get_db_username():
  # Get credential from a secure vault or return default value
  return 'admin'

def get_db_password():
  # Get credential from a secure vault or return default value
  return 'admin'

with open('../../.env.mustache', 'r') as f:
  data = { 'db_username': get_db_username(), 'db_password': get_db_password() }
  template = chevron.render(f, data)

with open('../../.env', 'w') as f:
  f.write(template)
