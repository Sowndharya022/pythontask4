class Circle:
    def __init__(self,radii):
        self.radii=radii
        self.__pi=3.141
    def area_of_circle(self):
        areas=[]
        for radius in self.radii:
            area_of_circle=self.__pi*radius*radius
            areas.append(area_of_circle)
        return areas
    def perimeter_of_circle(self):
        perimeters=[]
        for raidus in self.radii:
            perimeter_of_circle=2*self.__pi*raidus
            perimeters.append(perimeter_of_circle)
        return perimeters
radii_list=[10,501,22,37,100,999,87,351]
circle=Circle(radii_list)
areas=circle.area_of_circle()
perimeters=circle.perimeter_of_circle()
print("PERIMETERS FOR GIVEN RADII ARE ",perimeters)
print("Areas for given radii are ",areas)