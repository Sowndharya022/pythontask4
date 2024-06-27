class TV:
    def __init__(self,brand,inches=None,price=None):
        self.brand=brand
        self.channel=1
        self.inches=inches
        self.price=price
        self.on_off=False
        self.volume=50
    def increase_volume(self):
        if self.volume<100:
            self.volume+=1
    def decrease_volume(self):
        if self.volume>0:
            self.volume-=1
    def set_channel(self,channel):
        if 1<=self.channel<=50:
            self.channel=channel
    def reset_TV(self):
        self.volume=50
        self.channel=1
    def status_TV(self):
        return f"{self.brand}at channel{self.channel},volume{self.volume}"

class LED(TV):
    def __init__(self,brand,price,inches,screen_thickness,
                 energy_usuage,life_span,refresh_rate):
        super().__init__(brand,inches,price)
        self.screen_thickness=screen_thickness
        self.energy_usage=energy_usuage
        self.refresh_rate=refresh_rate
        self.life_span=life_span
    def viewing_angle_LED(self):
        return f"wide view angle"
    def back_light(self):
        return"led back light"
    def display_details(self):
        return (f"Brand:{self.brand},Channel:{self.channel},VOLUME:{self.volume},"
                f"Screenthickness:{self.screen_thickness},"
                f""f"Energyusage:{self.energy_usage}"
                f"Refreshrate;{self.refresh_rate},Lifespan;{self.life_span}")

class Plasma(TV):
    def __init__(self,brand,price,inches,screen_thickness,energy_usuage,
                 life_span,refresh_rate):
        super().__init__(brand,inches,price)
        self.screen_thickness=screen_thickness
        self.energy_usage=energy_usuage
        self.refresh_rate=refresh_rate
        self.life_span=life_span
    def viewing_angle_Plasma(self):
        return f"narrow view angle"
    def back_light(self):
        return"Plasma back light"
    def display_details(self):
        return (f"Brand:{self.brand},Channel:{self.channel},VOLUME:{self.volume},"
                f"Screenthickness:{self.screen_thickness},"
                f""f"Energyusage:{self.energy_usage}"
                f"Refreshrate;{self.refresh_rate},Lifespan;{self.life_span}")

tv=TV("SONY",50,34000)
print(tv.status_TV())
tv.increase_volume()
print(tv.status_TV())
tv.set_channel(34)
print(tv.status_TV())
tv.reset_TV()
print(tv.status_TV())
led_tv=LED("onida",45000,55,"30cm",
           "90watt",'10years',"132Hz")
print(led_tv.display_details())
plasma_tv= Plasma("samsung",50000,60,"78mm",
                  "87watt","7years","110hz")
print(plasma_tv.display_details())

print(plasma_tv.viewing_angle_Plasma())
print(led_tv.viewing_angle_LED())
print(led_tv.back_light())
print(plasma_tv.back_light())