from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Color, Port, Direction
from pybricks.hubs import PrimeHub
from pybricks.parameters import Button, Stop
from pybricks.tools import multitask, run_task
from pybricks.tools import hub_menu

#AXLE_DIST = 110
#WHEEL_DIAMETER = 88

AXLE_DIST = 112
WHEEL_DIAMETER = 56

class Robot:
    def __init__(self):
        self.hub = PrimeHub()
        self.hub.system.set_stop_button(Button.BLUETOOTH)
        self.hub.imu.up(True)

        left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        right_motor = Motor(Port.C)

        self.wiper = Motor(Port.E)
        self.wiper.run_target(-120, 0)
                            
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

    def arc_left(self, radius, angle):
        self.drive_base.arc(radius=-radius, angle=angle)

    def arc_right(self, radius, angle):
        self.drive_base.turn(radius=radius, angle=angle)

    RUNS = ["F", "B", "C"]
    def show_menu(self, next_run):
        ordered_runs = self.RUNS
        ordered_runs.remove(next_run)
        ordered_runs.insert(0, next_run)
        
        selection = hub_menu(*ordered_runs)
        wait(500)

        if selection == "F":
            run_forge(self)
        elif selection == "B":
            pass
        

def do_silo(robot:Robot):
    pass

def run_forge(robot:Robot):
    robot.drive(600)
    robot.arc_left(200, 30)
    robot.wiper.run_angle(120, 90)
    robot.arc_left(200, 60)
    robot.wiper.run_target(120, 0)
    robot.drive(-300)

    do_silo(robot)
    robot.drive(-600)

if __name__=="__main__":
    robot = Robot()
    
    robot.show_menu("F")    
    #robot.show_menu("B")

    