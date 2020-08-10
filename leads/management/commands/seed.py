from django.core.management.base import BaseCommand
from leads.models import Lead
import random

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    Lead.objects.all().delete()


def create_leads(index):
    """Creates an leads object combining different elements from the list"""
    names = ["dong", "tay", "nam", "bac"]
    emails = 'trongdong717@gmail.com'
    owners = [1, 2, 3, 4, 5]

    leads = Lead(
        name=random.choice(names),
        email=emails + str(index),
        message="hear is message for test",
    )
    leads.save()
    return leads

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 leads
    for index in range(15):
        create_leads(index)