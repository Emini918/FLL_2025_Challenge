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

        self.party = Motor(Port.B)
        self.party.run_target(-120, 0)
                            
        self.drive_base = DriveBase(
            left_motor, 
            right_motor, 
            wheel_diameter  = WHEEL_DIAMETER, 
            axle_track      = AXLE_DIST)
        self.drive_base.use_gyro(True)
        self.reset_drivebase()

        self.runs = []

        #sensor
        self.sensor = ColorSensor(Port.D)

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
        self.drive_base.arc(radius=radius, angle=angle)

    def drive_to_line(self, speed):
        self.drive_base.drive(speed, 0)
        while self.sensor.hsv().v > 30:
            #color = sensor.hsv()
            wait(5)
        self.drive_base.stop()


    RUNS = ["F", "M", "C", "T"]
    def show_menu(self, next_run):
        ordered_runs = self.RUNS
        ordered_runs.remove(next_run)
        ordered_runs.insert(0, next_run)
        
        selection = hub_menu(*ordered_runs)
        wait(500)

        if selection == "F":
            run_forge(self)
        elif selection == "M":
            run_mine(self)
        elif selection == "C":
            run_crane(self)
        elif selection == "T":
            run_test(self)
        

def do_silo(robot:Robot):
    for _ in range(4): 
        robot.wiper.run_target(600, -105, then=Stop.COAST)
        robot.wiper.run_target(600, 0)
        wait(500)
    

def run_forge(robot:Robot):

    #drive to forge
    robot.drive(600)

    #solve forge and inhabitants
    robot.arc_left(200, 30)
    robot.wiper.run_angle(120, 90)
    robot.arc_left(160, 33)
    robot.wiper.run_target(120, 95)
    robot.arc_left(200, 25)
    robot.wiper.run_target(120, 0)

    robot.drive(-500)
    robot.drive(30)
    #grab stuff
    wait(2000)

    #align at border
    robot.drive(-200)

    #do silo
    robot.drive(345)
    do_silo(robot)
    robot.drive(-300)

    #rotate to grindstone
    robot.arc_right(70, 70)
    robot.drive(30)
    robot.party.run_target(120, 90)
    robot.arc_right(70, 15)
    robot.party.run_target(120, 0)
    
    
    #drive home
    robot.turn_left(10)
    robot.drive(-150)
    robot.turn_right(10)
    robot.drive(-1500)


def run_mine(robot:Robot):
    
    #drive to brush
    robot.wiper.run_target(120, -90)
    robot.drive(770)
    robot.drive(-280)
    
    #drive to mine
    robot.arc_right(300, 90)
    robot.wiper.run_target(120, -110)
    robot.drive(160)

    #release mine
    robot.wiper.run_target(120, -45)
    wait(1000)
    robot.wiper.run_target(120, 0)

    #drive to flag position
    robot.drive(-310)
    robot.turn_left(90)
    robot.drive(-100)
    
    #return to 0 position
    wait(1000)
    robot.party.run_target(120, 0)
    robot.wiper.run_target(120, 0)

def dance():    
    robot.party.run_target(120, 90)
    robot.party.run_target(120, 0)
    robot.party.run_target(120, 90)
    robot.party.run_target(120, 0)
    robot.party.run_target(120, 90)
    robot.party.run_target(120, 0)
    robot.party.run_target(120, 90)
    robot.party.run_target(120, 0)
    wait(1000)
    

def run_crane(robot:Robot):
    robot.party.run_target(120, 0)

    #drive to black line
    robot.arc_left(260, 90)
    robot.drive_to_line(400)

    #lift statue
    robot.drive(230)
    robot.turn_right(45)
    robot.drive(120)

    robot.party.run_target(120, -90)

    #drive to crane
    
    robot.drive(-30)
    robot.arc_right(200, -45)
    robot.drive(-80)
    robot.turn_right(90)
    robot.drive(-180)
    robot.turn_left(15)

    #lift crane
    robot.wiper.run_angle(300, 720)
    robot.wiper.reset_angle(None)
    
    #drive to other home zone
    robot.turn_right(15)
    robot.drive(50)
    robot.arc_left(100, 90)
    robot.drive(1000)


def run_test(robot:Robot):
    robot.drive(800)
    robot.party.run_target(120, -45)
    robot.drive(-800)
    
if __name__=="__main__":
    robot = Robot()
    
    robot.show_menu("C")    
    #robot.show_menu("B")

    