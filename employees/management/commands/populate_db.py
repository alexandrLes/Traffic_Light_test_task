import random
from django.core.management.base import BaseCommand
from faker import Faker

from company_tree.employees.models import Department, Employee


class Command(BaseCommand):
    help = 'Populate the database with departments and employees'

    def handle(self, *args, **kwargs):
        fake = Faker()

        departments = []
        for i in range(1, 26):
            if i == 1:
                department = Department.objects.create(name=f'Department {i}', parent=None)
            else:
                parent = departments[random.randint(0, len(departments) - 1)]
                department = Department.objects.create(name=f'Department {i}', parent=parent)
            departments.append(department)

        for _ in range(50000):
            Employee.objects.create(
                full_name=fake.name(),
                position=fake.job(),
                hire_date=fake.date_between(start_date='-10y', end_date='today'),
                salary=random.randint(30000, 150000),
                department=random.choice(departments)
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with departments and employees'))
