points = 0

class PointsForPlace:
    def get_points_for_place(self, place):
        if place > 100:
            print('Баллы начисляются только первым 100 участникам')
        elif place < 1:
            print('Спортсмен не может занять нулевое или отрицательное место')
        else:
            points = 101 - place
            if points: ## Мне почему-то кажется, что это должно выглядеть проще, как будто у меня много кода для этой защиты
                return points
            else:
                return 0
        
        
class PointsForMeters:
    def get_points_for_meters(self,meters):
        if meters < 0:
            print('Количество метров не может быть отрицательным')
        else:
            points = meters * 0.5
            if points: ## Мне почему-то кажется, что это должно выглядеть проще, как будто у меня много кода для этой защиты
                return points
            else:
                return 0
           
class TotalPoints(PointsForPlace,PointsForMeters):
    def get_total_points(self, place, meters):
        return super().get_points_for_place(place) + super().get_points_for_meters(meters)

points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))           
        