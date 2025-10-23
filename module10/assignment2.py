class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print("The elevator is at floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("The elevator is at floor", self.current_floor)

    def go_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.floor_up()
            elif self.current_floor > target_floor:
                self.floor_down()
        return


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevator):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevator):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, target_floor):
        self.elevators[elevator_number].go_to_floor(target_floor)