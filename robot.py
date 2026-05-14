from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Color, Port, Direction
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task
from pybricks.tools import hub_menu

AXLE_DIST = 110
WHEEL_DIAMETER = 88

class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.hub.system.set_stop_button(Button.BLUETOOTH)

        left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        right_motor = Motor(Port.B)

        #arm_motor = Motor(Port.E)
        #arm_motor.run_target(-120, 0)
                            
        self.drive_base = DriveBase(
            left_motor, 
            right_motor, 
            wheel_diameter  = WHEEL_DIAMETER, 
            axle_track      = AXLE_DIST)
        self.drive_base.use_gyro(True)
        self.reset_drivebase()

        self.runs = []

    def reset_drivebase(self): 
        self.drive_base.settings(400, 500, 300, 500)

    def drive(self, distance):
        self.drive_base.straight(distance)

    def turn_left(self, angle):
        self.drive_base.turn(-angle)

    def turn_right(self, angle):
        self.drive_base.turn(angle)

    RUNS = ["A", "B", "C"]
    def show_menu(self, next_run):
        ordered_runs = self.RUNS
        ordered_runs.remove(next_run)
        ordered_runs.insert(0, next_run)
        
        selection = hub_menu(*ordered_runs)

        if selection == "A":
            run1(self)
        elif selection == "B":
            run1(self)
        


def run1(robot:Robot):
    robot.drive(200)
    robot.turn_left(90)
    robot.drive(200)
    
if __name__=="__main__":
    robot = Robot()
    
    robot.show_menu("A")
    robot.show_menu("B")

    