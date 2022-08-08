import os
from time import sleep
import random
import sys
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from pygame import mixer
import pygame




class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()
class inventory:
    def __init__(self,invet):
        self.invet=invet
    def displayitems(self):
        for i,c in self.invet.items():
            print(i,':',c)
def scenario():
    # os.system('clear')
    # scenario_1 = ["Your plane was struck by lightning.You Got Escaped From The Plane Crash with Puncture wounds ",
    # "The pilot and your companions were killed in the crash,unfortunately The Plane stuck in the Deep Ocean,",
    # "with help plane parts you reached sea shore , Now You are in the end of the shore. and began of the forest "]
    # location_details=["The Weather Is Cold. I should Check What Items I have here to survive"]
    # for line in scenario_1:          
    #     for c in line:          
    #         print(c, end='')   
    #         sys.stdout.flush()  
    #         sleep(0.1)          
    #     print('') 
    # input("\n\nPress Enter to Continue..")
    # os.system('clear')
    # for line in location_details:          
    #     for c in line:          
    #         print(c, end='')   
    #         sys.stdout.flush()  
    #         sleep(0.1)          
    #     print('') 
    return "Coast"
class _dict(dict):
  def __init__(self):
    self = dict()
  def add(self, key, value):
    self[key] = value

def location_generate():
    choice_arr=_dict()
    counter=1
    for i in random.sample(list(_locations.keys()),random.randint(1,4)):
        print(f"\n[{counter}]Location :{_locations[i]}")
        choice_arr.add(counter,random.sample(_areas,random.randint(1,4)))
        if(i == "Valley" or i=="River"):
            choice_arr[counter].pop()
            choice_arr[counter].append(_special_peark[1])
        elif(i=="Hill-top" and random.randint(0,3)==0):
            choice_arr[counter].append(_special_peark[0])
        elif(random.randint(0,6)==0):
            choice_arr[counter].append(_special_peark[2])
        print("Location Bounus: "+",".join(choice_arr[counter]))
        choice_arr[counter].append(str(i))
        counter+=1
    print("")
    return choice_arr

def avail_location(current_area):
    # input("\nAssess the situation.......")
    os.system('clear')
    print(f"You are in the {current_area}. You can Navigate to")
    dict_cp=location_generate()
    print("Type Index like 1,2 of the location to go")
    choose=input("Type h for help option.\n:")
    print("\n\n")
    print("Location Bouns :")
    for i in dict_cp[int(choose)]:
        if i.isnumeric():
            current_area=_locations[int(i)]
            dict_cp[int(choose)].remove(i)
    return dict_cp[int(choose)],current_area
def Load(f_w,s_w,t_w):
    with Loader(f_w):
        for i in range(10):
            sleep(0.25)

    loader = Loader(s_w,t_w, 0.05).start()
    for i in range(10):
        sleep(0.25)
    loader.stop()

def body(bodytemp):
    if bodytemp>80:
        return "Good"
    elif bodytemp>35 and bodytemp<80:
        return "Normal"
    else:
        return "You attacked by Diease"

def avail_option(body_temp,stamina,health,rest,food,day,km,des,_arr,current_area):
    stat='Loding...'
    counter=0
    for i in _arr:
        print(f'   [{counter}]{i}')
        counter+=1
    print("n for next location")
    choice=input("Choice: ")
    if choice=='n':
            if(stamina<15):
                print("You have Low Stamina You Need Rest....")
                pass
            elif (rest<20):
                print("You have Low Quality of Sleep You Need Rest....")
                pass
            elif (body_temp<10):
                print("Your are Dead...")
                pass
            else:
                stamina-=random.randint(10,15)
                body_temp-=10
                rest-=10
                day+=random.randint(5,8)
                food-=random.randint(10,16)
                Load(f"Moving...",f"Your stats restoring..",f"Day {round(day/24)} /  [Body Condition :{body(body_temp)} ,Calories :{food},Health :{health},Restness :{rest},Food :{stamina}]\n")    
                _arr,current_area=avail_location(current_area)
                avail_option(body_temp,stamina,health,rest,food,day,km,des,_arr,current_area)
    elif choice.isnumeric:
       
       
        if(_arr[int(choice)]=="Cave"):
            if(stamina<100 and rest<100 and body_temp<100):
                stamina+=5
                body_temp-=4
                rest+=4
            day+=random.randint(5,8)
            food-=300
            Load(f"Sleeping...",f"Your stats restoring..",f"Day {round(day/24)} / [Body Condition :{body(body_temp)} ,Calories :{food},Health :{health},Restness :{rest},Food :{stamina}]\n")
      
      
      
        if(_arr[int(choice)]=="Pure-water"):
            p_c=int(input("[1] Drink the water\n[2] Collect water\n[3] Wash Bod\n:"))
            if( p_c==1):
                stat="Drinking..."
                if(stamina<100 and rest<100 and body_temp<100):
                    stamina+=5
                    body_temp+=2
                    day+=random.randint(1,3)
                    food-=100
            elif( p_c==3):
                stat="Washing..."
                if(stamina<100 and rest<100 and body_temp<100):
                    body_temp+=10
                    day+=random.randint(1,3)
                    food-=100
                    
            Load(f"{stat}",f"Your stats restoring..",f"Day {round(day/24)} /  [Body Condition :{body(body_temp)} ,Calories :{food},Health :{health},Restness :{rest},Food :{stamina}]\n")
        if(_arr[int(choice)]=="wet-wood"):
            print("Cutting the Wood......")
        if(_arr[int(choice)]=="Dirty-Water"):
            p_c=int(input("[1] Drink the water\n[2] Collect water\n[3] Wash Bod\n:"))
            if( p_c==1):
                stat="Drinking..."
                if(stamina<100 and rest<100 and body_temp<100):
                    stamina+=5
                    body_temp-=8
                    day+=random.randint(1,3)
                    food-=200
            elif( p_c==3):
                stat="Washing..."
                if(stamina<100 and rest<100 and body_temp<100):
                    body_temp+=4
                    day+=random.randint(1,3)
                    food-=100
        if(_arr[int(choice)]=="Plants"):
            print("you can ")
        if(_arr[int(choice)]=="Fire-wood"):
            print("Cutting the Wood......")
        if(_arr[int(choice)]=="Medicine-Plants"):
            print("you can ")
        if(_arr[int(choice)]=="Fishing"):
            print("you can ")
        if(_arr[int(choice)]=="Animals"):
            print("you can ")
        avail_option(Body_temp,stamina,health,rest,food,day,km,des,_arr,current_area)
if __name__== '__main__':
    Body_temp=100
    stamina=100
    rest=100
    health=100
    food=3000
    Day=0
    km=0
    des=500
    # pygame.mixer.init()
    # pygame.mixer.music.load("music.mp3") # Paste The audio file location 
    # pygame.mixer.music.play(-1) 
    _locations={1:"Hill-top",2:"Sparse-Forest",3:"Creek",4:"Forest",5:"Thick-Forest",6:"Mud-Area",7:"Old-campsite",8:"Valley",9:"River"}
    _areas=["Cave","Pure-water","wet-wood","Dirty-Water","Plants","Fire-wood"]
    _special_peark=["Medicine-Plants","Fishing","Animals"]
    _arr,current_area=avail_location(scenario())
    avail_option(Body_temp,stamina,health,rest,food,Day,km,des,_arr,current_area)
    invet={'BOTTLE [SAFE WATER]':1}
    

    # inventory(invet).displayitems()