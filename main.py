#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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

import os
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import webapp2
import jinja2
from google.appengine.ext import ndb
from google.appengine.api import users
import logging
import datetime
template_env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.getcwd()))
#import firebase_admin
#from firebase_admin import credentials
#cred = credentials.Certificate('templates/firebase/service_account.json')
#default_app = firebase_admin.initialize_app(cred)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/index.html')
        context = {}
        self.response.write(template.render(context))

class PrivacyHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/privacy.html')
        context = {}
        self.response.write(template.render(context))

class TermsHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/terms.html')
        context = {}
        self.response.write(template.render(context))

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/about/about.html')
        context = {}
        self.response.write(template.render(context))

class ContactHandler(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/contact/contact.html')
        context = {}
        self.response.write(template.render(context))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/contact', ContactHandler),
    ('/privacy', PrivacyHandler),
    ('/terms', TermsHandler)
], debug=True)
