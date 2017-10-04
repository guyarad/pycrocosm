# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from changeset.models import Changeset

from querymap.views import p
import gc
import sys

# Create your tests here.

class ElementsTestCase(TestCase):
	def setUp(self):
		self.username = "john"
		self.password = "glass onion"
		self.email = 'jlennon@beatles.com'
		self.user = User.objects.create_user(self.username, self.email, self.password)
		self.client = Client()
		self.client.login(username=self.username, password=self.password)

	#def test_put_node(self):

	#	response = self.client.put(reverse('element', args=['node', '5']), "", content_type='text/xml')

	#	self.assertEqual(response.status_code, 200)

	def test_create_node(self):
		cs = Changeset.objects.create(user=self.user, tags={"foo": "me"}, is_open=True)

		createXml = """<osm>
			 <node changeset="{}" lat="51.0" lon="2.2">
			   <tag k="note" v="Just a node"/>
			 </node>
			</osm>""".format(cs.id)
		response = self.client.put(reverse('create', args=['node']), createXml, content_type='text/xml')
		if response.status_code != 200:
			print response.content

		self.assertEqual(response.status_code, 200)

	def test_create_node_invalid_xml(self):
		cs = Changeset.objects.create(user=self.user, tags={"foo": "me"}, is_open=True)

		createXml = """<osm>
			 <node changeset="{}" lat="51.0" lon="2.2">
			   <tag k="note" v="Just a node"/>
			</osm>""".format(cs.id)
		response = self.client.put(reverse('create', args=['node']), createXml, content_type='text/xml')

		self.assertEqual(response.status_code, 400)


	def tearDown(self):
		u = User.objects.get(username = self.username)
		u.delete()

		#Swig based transaction object is not freed if an exception is thrown in python view code
		#Encourage this to happen here.
		#https://stackoverflow.com/a/8927538/4288232
		sys.exc_clear()

