import tkinter as tk
from controller.user_controller import UserController
from controller.schedule_controller import ScheduleController

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro e Agendamento")
        self.user_controller = UserController()
        self.schedule_controller = ScheduleController()

        # Aba de cadastro de usuários
        self.frame_user = tk.LabelFrame(root, text="Cadastro de Usuário")
        self.frame_user.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.frame_user, text="Nome:").grid(row=0, column=0)
        tk.Label(self.frame_user, text="Email:").grid(row=1, column=0)
        self.entry_name = tk.Entry(self.frame_user)
        self.entry_email = tk.Entry(self.frame_user)
        self.entry_name.grid(row=0, column=1)
        self.entry_email.grid(row=1, column=1)
        self.btn_cadastrar = tk.Button(self.frame_user, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.grid(row=2, column=0, columnspan=2)
        self.text_users = tk.Text(self.frame_user, height=5, width=40)
        self.text_users.grid(row=3, column=0, columnspan=2)

        # Aba de agendamento
        self.frame_schedule = tk.LabelFrame(root, text="Agendamento")
        self.frame_schedule.grid(row=1, column=0, padx=10, pady=10)

        tk.Label(self.frame_schedule, text="Título:").grid(row=0, column=0)
        tk.Label(self.frame_schedule, text="Data (DD-MM-YYYY):").grid(row=1, column=0)
        tk.Label(self.frame_schedule, text="Hora (HH:MM):").grid(row=2, column=0)
        tk.Label(self.frame_schedule, text="Descrição:").grid(row=3, column=0)

        self.entry_title = tk.Entry(self.frame_schedule)
        self.entry_date = tk.Entry(self.frame_schedule)
        self.entry_time = tk.Entry(self.frame_schedule)
        self.entry_desc = tk.Entry(self.frame_schedule)

        self.entry_title.grid(row=0, column=1)
        self.entry_date.grid(row=1, column=1)
        self.entry_time.grid(row=2, column=1)
        self.entry_desc.grid(row=3, column=1)

        self.btn_agendar = tk.Button(self.frame_schedule, text="Agendar", command=self.cadastrar_agendamento)
        self.btn_agendar.grid(row=4, column=0, columnspan=2)
        self.text_schedules = tk.Text(self.frame_schedule, height=5, width=40)
        self.text_schedules.grid(row=5, column=0, columnspan=2)

    
    def cadastrar_usuario(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        password = self.user_controller.create_user(name, email)
        self.text_users.insert(tk.END, f"Usuário cadastrado!\nNome: {name}\nEmail: {email}\nSenha: {password}\n\n")
        self.text_users.insert(tk.END, "Usuários cadastrados:\n")
        users = self.user_controller.list_users()
        for user in users:
            self.text_users.insert(tk.END, f"ID: {user[0]} | Nome: {user[1]} | Email: {user[2]}\n")
        self.text_users.insert(tk.END, "\n")


    def cadastrar_agendamento(self):
        title = self.entry_title.get()
        data_br = self.entry_date.get()
        date = self.converter_data_para_iso(data_br)  # converte para yyyy-mm-dd
        time = self.entry_time.get()
        description = self.entry_desc.get()
        self.schedule_controller.create_schedule(title, date, time, description)
        self.text_schedules.insert(tk.END, f"Agendamento cadastrado!\nTítulo: {title}\nData: {data_br}\nHora: {time}\nDescrição: {description}\n\n")
        self.text_schedules.insert(tk.END, "Todos os agendamentos:\n")
        schedules = self.schedule_controller.list_schedules()
        for sched in schedules:
            data_br_formatada = self.converter_data_para_br(sched[2])
            self.text_schedules.insert(tk.END, f"ID: {sched[0]} | Título: {sched[1]} | Data: {data_br_formatada} | Hora: {sched[3]} | Desc: {sched[4]}\n")
        self.text_schedules.insert(tk.END, "\n")

        
    def converter_data_para_iso(self, data_br):
        partes = data_br.split('-')
        return f"{partes[2]}-{partes[1]}-{partes[0]}"  # dd-mm-yyyy → yyyy-mm-dd

    def converter_data_para_br(self, data_iso):
        partes = data_iso.split('-')
        return f"{partes[2]}-{partes[1]}-{partes[0]}"  # yyyy-mm-dd → dd-mm-yyyy

