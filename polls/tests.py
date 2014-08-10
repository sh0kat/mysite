import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import polls

class PollMethodTests(TestCase):

	def test_was_published recently_with_future_poll(self):
		"""
		was_published_recently() should return False for polls whose
		pub_date is in future
		"""
		future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=30))
		self.assertEqual(future_poll.was_published_recently(), False)