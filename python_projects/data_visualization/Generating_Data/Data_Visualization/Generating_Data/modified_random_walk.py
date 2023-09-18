from random import choice

class MdifiedRandomWalk:
    def __init__(self, num_points = 5000):
        # Defining the points in the walk
        self.num_points = num_points
        # Stating the initial point of walk
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        direction = choice([-1,1])
        distance = choice([1,2,3,4,5,6,7,8])
        return(direction*distance)

    def fill_walk(self):
        while len(self.x_values) < self.num_points :
            x_step = self.get_step()
            y_step = self.get_step()
            # Determination of new X/Y values
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # Appending the value generated in the list of values
            self.x_values.append(x)
            self.y_values.append(y)