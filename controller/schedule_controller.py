from model.schedule_model import ScheduleModel

class ScheduleController:
    def __init__(self):
        self.schedule_model = ScheduleModel()

    def create_schedule(self, title, date, time, description):
        self.schedule_model.add_schedule(title, date, time, description)

    def list_schedules(self):
        return self.schedule_model.get_schedules()