from launchpad.LaunchpadEditor import LaunchpadEditor
from launchpad.launchpad import Launchpad


class Animator:
    def __init__(self):
        self._launchpad = Launchpad()
        self._display = LaunchpadEditor()


"""

	def __init__(self,ant):
		super().__init__(ant)
		pass



	def make_data_menu(self, menue_bar):

		menue = tkinter.Menu(menue_bar)
		menue.add_command(label="Data Hub", command=self.show_data_hub_data)
		menue.add_command(label="Head Sensors", command=self.show_head_sensors_data)
		menue.add_command(label="Leg Sensors", command=self.show_leg_sensors_data)
		menue.add_command(label="Leg controller", command=self.show_leg_controller_data)
		menue_bar.add_cascade(label="Data View", menu=menue)
		

	def make_control_menu(self, menue_bar):
		menue = tkinter.Menu(menue_bar)
		menue.add_command(label="Leg controller", command=self.show_leg_controller_control)
		menue.add_command(label="Leg sensors", command=self.show_leg_sensors_control)


		menue_bar.add_cascade(label="Control View", menu=menue)





	def make_setup_menu(self, menue_bar):
		menue = tkinter.Menu(menue_bar)
		menue.add_command(label="Leg Sensors", command=self.show_leg_sensors_setup)
		menue.add_command(label="Leg controller", command=self.show_leg_controller_setup)
		menue_bar.add_cascade(label="Setup View", menu=menue)


	def show_data_hub_data(self):
		print("show Data hub data")
		device = self._robot.get_data_hub()
		self._main_data_hub_data = DataHubDataView(device)
		self._main_data_hub_data.draw()

	def show_head_sensors_data(self):
		print("show head Sensors data")
		device = self._robot.get_head_sensors()
		self._head_sensors_data = HeadSensorsDataView(device)
		self._head_sensors_data.draw()

# leg sensors

	def show_leg_sensors_data(self):
		print("show leg Sensors data")
		device = self._robot.get_leg_sensors()
		self._leg_sensors_data = LegSensorsDataView(device)
		self._leg_sensors_data.draw()

	def show_leg_sensors_control(self):
		print("show leg controller data")
		device = self._robot.get_leg_sensors()
		self._leg_controller_data = LegSensorsControlView(device)
		self._leg_controller_data.draw()


# leg controller

	def show_leg_controller_data(self):
		print("show leg controller data")
		device = self._robot.get_leg_controller()
		self._leg_controller_data = LegControllersDataView(device)
		self._leg_controller_data.draw()
	

	def show_leg_controller_control(self):
		print("show leg controller data")
		device = self._robot.get_leg_controller()
		self._leg_controller_data = LegControllersControliew(device)
		self._leg_controller_data.draw()
	

	def show_leg_controller_setup(self):
		print("show leg controller data")
		device = self._robot.get_leg_controller()
		self._leg_controller_data = LegControllerSetupView(device)
		self._leg_controller_data.draw()


	def show_leg_sensors_setup(self):
		pass
"""