#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

from google.appengine.api import users
import os
import webapp2
import jinja2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	lang = ""
        country = "POR"
        tempcountry = "webcams_surf_windsurf_espanya.html"
    	lang = self.request.get("lang")
        country = self.request.get("country")
        if country == "ESP":
            tempcountry = "webcams_surf_windsurf_espanya.html"
        elif country == "POR":
            tempcountry = "webcams_surf_windsurf_portugal.html"
        elif country == "ITA":
            tempcountry = "webcams_surf_windsurf_italia.html"
        #logging.info("value of my contry is %s", lang)
    	if lang == "eng":
    		template_values = {
            	'textfav': "Configure your Favourite Cams! And they will appear in this section.",
                'lang':lang,
                'country':country,
                'fav':"Favourite",
                'perm':"Permanent",
                'ESP': "Spain", 
                'POR': "Portugal",
                'SUD': "South",
                'NORTE': 'North',
                'ITA': "Italy",
                'GARDA': "Garda",
                'CERDENYA': "Sardinia", 
                'langt': "en-EN"
        	}
        else:
        	template_values = {
            	'textfav': u"Configura tus camaras FAVORITAS para que aparezcan siempre en esta sección",
                'lang':lang,
                'country':country,
                'fav':"Favorita",
                'perm':"Permanente",
                'ESP': u"España", 
                'POR': "Portugal",
                'SUD': 'Sur',
                'NORTE': 'Norte',
                'ITA': 'Italia',
                'GARDA': "Garda",
                'CERDENYA': u"Cerdeña",
                'langt': "es-ES"
        	}
        
        #self.response.out.write(tempcountry)
        template = JINJA_ENVIRONMENT.get_template(tempcountry)
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/webcams', MainHandler),
], debug=False)
