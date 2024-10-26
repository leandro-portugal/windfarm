class YawMechanism:

    def __init__(self, tower_id, location, current_position):
        self.tower_id = tower_id
        self.location = location
        self.current_position = current_position

    def adjust_yaw(self, wind_direction):
        adjust = (wind_direction - self.current_position + 360) % 360

        if adjust > 180:
            adjust -= 360
      
        self.current_position = (self.current_position + adjust) % 360
        print(f"Tower {self.tower_id} ({self.location}): adjusting yaw in  {adjust} degrees.")
        print(f"New ship position: {self.current_position} degrees.")
        
        return self.current_position

