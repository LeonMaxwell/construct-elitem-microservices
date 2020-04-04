class BodyService:
    def __init__(self, name, about):
        super().__init__()
        self.NAME_MICROS = name
        self.ABOUT_MICROS = about

    def get_name(self):
        return self.NAME_MICROS

    def get_about(self):
        return self.ABOUT_MICROS

    def rename_services(self, new_name):
        self.NAME_MICROS = self.NAME_MICROS.replace(self.get_name(), new_name)


class CallService:
    BIND_ADMIN_CONTROL = None
    BIND_COMMAND_CALL = None
    BIND_LITERAL_CALL = None

    def __init__(self, *binds, default=False):
        super().__init__()
        for bind in binds:
            if bind.startswith("//"):
                self.BIND_ADMIN_CONTROL = bind
            elif bind.startswith("/"):
                self.BIND_COMMAND_CALL = bind
            else:
                self.BIND_LITERAL_CALL = bind

    def get_commands(self):
        all_ = dict()

        all_ = {'Литера': self.BIND_LITERAL_CALL, 'Команда': self.BIND_COMMAND_CALL,
                'Админ-команда': self.BIND_ADMIN_CONTROL}

        return all_