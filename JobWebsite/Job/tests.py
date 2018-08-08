import datetime
from django.test import TestCase
from .models import Job
from User.models import User

# Create your tests here.


class JobTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username="mstockton", password='12345')
        user2 = User.objects.create_user(username="Test", password='12345')
        Job.objects.create(title="Test", content="content",
                           created_by=user1, publish=datetime.datetime.now())
        Job.objects.create(title="Test2", content="content2",
                           created_by=user2, publish=datetime.datetime.now())

    def test_jobs_created_sucessfully(self):
        job1 = Job.objects.get(title='Test')
        job2 = Job.objects.get(title='Test2')
        self.assertTrue(job1.title == 'Test',
                        # only displays msg on failure
                        "Job 1's title is {0} instead of {1}"
                        .format(job1.title, 'Test'))
        self.assertIsNotNone(job2)

    def tearDown(self):
        # Clear down the data.
        user1 = User.objects.get(username="mstockton")
        user2 = User.objects.get(username="Test")
        job1 = Job.objects.get(title='Test')
        job2 = Job.objects.get(title='Test2')

        user1.delete()
        user2.delete()
        job1.delete()
        job2.delete()
