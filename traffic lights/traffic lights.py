# Traffic Light Control

import time

class TrafficLight:
    def __init__(self):
        self.state = "Red"

    def change_light(self):
        if self.state == "Red":
            self.state = "Green"
        elif self.state == "Green":
            self.state = "Yellow"
        elif self.state == "Yellow":
            self.state = "Red"

    def run(self):
        while True:
            print(f"Traffic Light is {self.state}")
            if self.state == "Red":
                time.sleep(5)  # Red light for 5 seconds
            elif self.state == "Green":
                time.sleep(5)  # Green light for 5 seconds
            elif self.state == "Yellow":
                time.sleep(2)  # Yellow light for 2 seconds
            self.change_light()

if __name__ == "__main__":
    traffic_light = TrafficLight()
    traffic_light.run()
