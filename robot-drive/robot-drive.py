""" robot-drive.py: code to drive a robot

Code to be used to drive the robots for the GWC robot project. It will use the Adafruit library that pairs with our
motor driver circuits.

Students should be empowered to changes code in this lesson. Most changes will go between the following comments. This
is not to say students cannot change things outside of those regions.

### STUDENT SECTION ###

### END STUDENT SECTION ###
"""
import time # Used for sleeping between steps
from adafruit_motorkit import MotorKit, stepper # Used to help drive the motors

MOTOR_KIT = MotorKit()


def drive():
    """ Function used to drive the robot, called once
    
    This function will use the MOTOR_KIT created above to drive the robot. Since our motors are steppers (they turn one
    step or increment at a time) we need to control the motors based on steps.
    
    In this code we will have several tasks:
      1. Determine left and right motors.  For this we can look at the circuit and determine which is which or we can
         turn the motors and see what happens.  Once this is known, fill it in.
      2. Make the robot drive forward
      3. Make the robot drive backward
      4. Make the robot turn left and right
    """
    test_motor = MOTOR_KIT.stepper1

    left_motor = None # Replace 'None' with MOTOR_KIT.stepper1 or MOTOR_KIT.stepper2 depending on your test.
    right_motor = None # Replace 'None' with MOTOR_KIT.stepper1 or MOTOR_KIT.stepper2 depending on your test.

    try:
        # Run forever taking one step at a time
        while True:
            test_motor.onestep(direction=stepper.FORWARD)
            time.sleep(0.1)
    except Exceptions as exc:
        print("[ERROR] An exception occurred spinning the motor. Stopping.", exc)

def main():
    """ Main python function. This is where our code should start. """
    drive()

# Python code will start executing here. It is standard practice to guard the main function call with this check to see
# if we are running the main program.
if __name__ == "__main__":
    main()