from django.test import TestCase, Client
from django.urls import reverse

from commands.models import Command


print(f"Tests in '{__name__}' started")


class CommandsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cmd = Command.objects.create(
            name="Liv",
        )

    test_true_data = {
        # "view_name": ("status_code", "template", ),
        "commands": (200, "templates/commands/commands.html", ),
        "create_commands": (200, "templates/commands/create.html", ),
    }

    def setUp(self):
        self.client = Client()

    def test_commands_view(self):

        for view_name, (status_code, template) in self.test_true_data.items():
            response = self.client.get(reverse(view_name))

            self.assertEqual(response.status_code, status_code)
            self.assertTemplateUsed(response, template)

    def test_commands_id_view(self):

        cmd = Command.objects.get(pk=1)

        response = self.client.get(reverse("id", args=[cmd.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "templates/commands/info_command.html")


print(f"Tests in '{__name__}' finished")


    # test_true_data_id = {
    #     "view_name": ("status_code", "template", ),
    #     "id": (200, "templates/commands/info_command.html",),
    #     "player": (200, "templates/commands/player.html", ),
    #     "create_capitan": (200, "templates/commands/create_capitan.html", ),
    # }