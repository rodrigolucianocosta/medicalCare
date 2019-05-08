"""
medicalCare - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    javascripts   = [
        'js/medicalCare/routes.js',
        'js/opal/controllers/discharge.js'
    ]