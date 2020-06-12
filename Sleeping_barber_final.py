import threading
import random
from time import sleep,ctime
from threading import Event

waitingroom = [] # array to hold the people in the waiting room
loopname =  ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed", "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel", "Abhinav", "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James", "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan", "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman", "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram", "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec", "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro", "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred", "Alfy", "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair", "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally", "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh", "Ameer", "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit", "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel", "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony", "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan", "Aon", "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan", "Archibald", "Archie", "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria", "Arian", "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav", "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur", "Arturo", "Arun", "Arunas", "Arved", "Arya", "Aryan", "Aryankhan", "Aryian", "Aryn", "Asa", "Asfhan", "Ash", "Ashlee-jay", "Ashley", "Ashton", "Ashton-Lloyd", "Ashtyn", "Ashwin", "Asif", "Asim", "Aslam", "Asrar", "Ata", "Atal", "Atapattu", "Ateeq", "Athol", "Athon", "Athos-Carlos", "Atli", "Atom", "Attila", "Aulay", "Aun", "Austen", "Austin", "Avani", "Averon", "Avi", "Avinash", "Avraham", "Awais", "Awwal", "Axel", "Ayaan", "Ayan", "Aydan", "Ayden", "Aydin", "Aydon", "Ayman", "Ayomide", "Ayren", "Ayrton", "Aytug", "Ayub", "Ayyub", "Azaan", "Azedine", "Azeem", "Azim", "Aziz", "Azlan", "Azzam", "Azzedine", "Babatunmise", "Babur", "Bader", "Badr", "Badsha", "Bailee", "Bailey", "Bailie", "Bailley", "Baillie", "Baley", "Balian", "Banan", "Barath", "Barkley", "Barney", "Baron", "Barrie", "Barry", "Bartlomiej", "Bartosz", "Basher", "Basile", "Baxter", "Baye", "Bayley", "Beau", "Beinn", "Bekim", "Believe", "Ben", "Bendeguz", "Benedict", "Benjamin", "Benjamyn", "Benji", "Benn", "Bennett", "Benny", "Benoit", "Bentley", "Berkay", "Bernard", "Bertie", "Bevin", "Bezalel", "Bhaaldeen", "Bharath", "Bilal", "Bill", "Billy", "Binod", "Bjorn", "Blaike", "Blaine", "Blair", "Blaire", "Blake", "Blazej", "Blazey", "Blessing", "Blue", "Blyth", "Bo", "Boab", "Bob", "Bobby", "Bobby-Lee", "Bodhan", "Boedyn", "Bogdan", "Bohbi", "Bony", "Bowen", "Bowie", "Boyd", "Bracken", "Brad", "Bradan", "Braden", "Bradley", "Bradlie", "Bradly", "Brady", "Bradyn", "Braeden", "Braiden", "Brajan", "Brandan", "Branden", "Brandon", "Brandonlee", "Brandon-Lee", "Brandyn", "Brannan", "Brayden", "Braydon", "Braydyn", "Breandan", "Brehme", "Brendan", "Brendon", "Brendyn", "Breogan", "Bret", "Brett", "Briaddon", "Brian", "Brodi", "Brodie", "Brody", "Brogan", "Broghan", "Brooke", "Brooklin", "Brooklyn", "Bruce", "Bruin", "Bruno", "Brunon", "Bryan", "Bryce", "Bryden", "Brydon", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "Caiden-Paul", "Caidyn", "Caie", "Cailaen", "Cailean", "Caileb-John", "Cailin", "Cain", "Caine", "Cairn", "Cal", "Calan", "Calder", "Cale", "Calean", "Caleb", "Calen", "Caley", "Calib", "Calin", "Callahan", "Callan", "Callan-Adam", "Calley", "Callie", "Callin", "Callum", "Callun", "Callyn", "Calum", "Calum-James", "Calvin", "Cambell", "Camerin", "Cameron", "Campbel", "Campbell", "Camron", "Caolain", "Caolan", "Carl", "Carlo", "Carlos", "Carrich", "Carrick", "Carson", "Carter", "Carwyn", "Casey", "Casper", "Cassy", "Cathal", "Cator", "Cavan", "Cayden", "Cayden-Robert", "Cayden-Tiamo", "Ceejay", "Ceilan", "Ceiran", "Ceirin", "Ceiron", "Cejay", "Celik", "Cephas", "Cesar", "Cesare", "Chad", "Chaitanya", "Chang-Ha", "Charles", "Charley", "Charlie", "Charly", "Chase", "Che", "Chester", "Chevy", "Chi", "Chibudom", "Chidera", "Chimsom", "Chin", "Chintu", "Chiqal", "Chiron", "Chris", "Chris-Daniel", "Chrismedi", "Christian", "Christie", "Christoph", "Christopher", "Christopher-Lee", "Christy", "Chu", "Chukwuemeka", "Cian", "Ciann", "Ciar", "Ciaran", "Ciarian", "Cieran", "Cillian", "Cillin", "Cinar", "CJ"]
# array for all randomly generated names that could be assigned
loops = []
damn = False
ik = 0
EventArray = [Event()]  # an event array to trigger the barber to start the haircut.
triggerArray = [Event()] # another event array to trigger the barber to wake up.
SleepArray = [Event()] # another event array to signal that the barber is sleeping

ChairsWR = 15  # variable to define how many chairs are in the waiting room
barbers = 1 # variable to define how many barbers there are

ts = threading.Thread()
threads = []    # create an array of threads for barber function
threadsCB = []   # create an array of threads for check_barber function

barbernumber = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight" ,"ninth", "tenth"] # array for when you print which barber it is.

adre = Event()
malibu = [Event(),Event()]

ue = Event()

z = 0

def barber(bnum, loopname,nsec):
    u = waitingroom.index(loopname)     # get the index of the person in the waitingroom.
    triggerArray[bnum].set()
    waitingroom.pop(u)  # remove the person from the index and therefore from the waiting room
    print("barber", bnum, "is cutting" , loopname , "'s hair at:'", ctime())
    sleep(random.randint(2,5))      # how much time it takes to cut the hair
    print("barber", bnum, "is finished cutting", loopname, "'s hair at:", ctime())
    damn = False
    triggerArray[bnum].clear()      # reset the event function for the next haircut
def waitingroomfunc():
    ze = 0
    while (not adre.is_set()):
        sleep(1)    # random event time for person to come into the waiting room
        x = random.randint(0,1)     # random event based on whether person comes into the waiting room or not
        if(len(waitingroom) < ChairsWR):    # people in waiting room cannot exceed the defined variable at the start. 
            name = random.choice(loopname)      # give a random name to a customer
            waitingroom.append(name)    # add the person to the waiting room array(therefore waiting room)
            v = random.randint(3,9)
            print(name + " has arrived")
            loops.append(v)
            if(not triggerArray[1].is_set()):   # if the first barber is not working condition will succeed
                print(name + " has arrived and is waking up the first barber")
                EventArray[1].set()     # set the event function to wake the first barber and begin the thread for haircut
            if(barbers > 1):
                if(triggerArray[1].is_set() and not triggerArray[2].is_set()): # if the first barber is working and the second one isn't
                    print(name + " has arrived and is waking up the second barber")
                    EventArray[2].set()     # set the event function to wake the second barber and begin the thread for a haircut by barber two
                    SleepArray[2].set()     # an event function to signal the second barber to stop sleeping
            ir = 3
            while(ir <= barbers):   # loop through all the barbers to check to see who is working and who is not
                if(triggerArray[ir - 2].is_set() and triggerArray[ir - 1].is_set() and not triggerArray[ir].is_set()): # determine if the two barbers before the current barber are working
                    print(name + " has arrived and is waking up the " + barbernumber[ir - 1 ] + "barber")
                    EventArray[ir].set() # set the event function to begin the thread for a haircut by the current barber in the loop
                    SleepArray[ir].set()   # set an event function to signal the current barber to stop sleeping
                ir += 1

def check_barber(dnum, barbername):
    f = 0
    threads1 = []   # make an array for all the threads in this function
    global z
    while(not malibu[dnum].is_set()):
        print(True, dnum)
        if(EventArray[dnum].is_set()):  # if the barber defined by bnum has been told to begin a haircut
            t1 = threading.Thread(target=barber,args=(dnum ,waitingroom[0],loops[0])) # begin the barber thread based on the number defined by bnum(which barber is it)
            threads1.append(t1) # add thread to the array
            threads1[f].start() # start the thread
            threads1[f].join() # wait for the thread to finish
            EventArray[dnum].clear() # reset the event based on the index defined by bnum for barber to begin haircut 
            f += 1
        if(not EventArray[dnum].is_set()):  # if barber defined by bnum has yet to be told to begin a haircut
            print(barbernumber[dnum - 1] + " barber is sleeping")
            while(not SleepArray[dnum].is_set()): # if barber has yet to been told to wake up 
                SleepArray[dnum].wait(6) # barber goes to sleep
                if(malibu[dnum].is_set()):
                    SleepArray[dnum].set()
            SleepArray[dnum].clear() # reset the sleep event
def close_barber():
    sleep(180) # how long you want the barber shop to be open(here it's 3 minutes)
    ue.set() # close down the barber shop by triggering event in main function
def main():
    time_1 = ctime()
    print(time_1)
    nloops = range(len(loops)) 
    ik = 1
    while(ik <= barbers): # loop through all barbers 
        triggerArray.append(Event()) # assign an event for every barber for when they are doing the haircut
        EventArray.append(Event()) # assign an event for every barber to begin the thread for a haircut
        SleepArray.append(Event()) # assign an event for every barber to stop sleeping
        ik += 1
    ts = threading.Thread(target=waitingroomfunc)   # make the thread for the waitingroom so that customers can enter the barber
    ts.start()  # begin the waitingroom thread
    ri = threading.Thread(target = close_barber)
    ri.start()
    iz = 2
    pu = 0
    while(iz <= barbers):   #loop through all the barbers
        malibu.append(Event()) # will be used to signal the join method of the thread
        hu = threading.Thread(target=check_barber, args=(iz, "Jim")) # make thread for check_barber, this thread is for cases where there are barbers not working and customers waiting
        threadsCB.append(hu) # add the thread to the check_barber array thread
        threadsCB[pu].start() # start the check_barber thread
        pu += 1
        iz += 1
    z = 0
    while(not ue.is_set()): # will run until ue is not set
        x = len(waitingroom)
        if(x >= 1 and not triggerArray[1].is_set()):    # if the first barber is not working
            t = threading.Thread(target=barber,args=(1, waitingroom[0],loops[0])) # make the barber thread for the first barber
            threads.append(t)   # add barber thread to barber array thread
            threads[z].start() # start the barber thread
            threads[z].join()  #  wait for barber thread to finish
            z += 1
        if(x == 0):
            print("first barber is sleeping")
            while not EventArray[1].is_set():   # if the barber has yet to be told he has to work
                EventArray[1].wait(6) # barber can go to sleep
            EventArray[1].clear()  # reset the barber working event
            i = 0
        print("z is ", z)
        if(z == 15):
            EventArray[1].set()
    adre.set()  # set this event to signal the waiting room thread to stop
    ts.join() # wait for the waiting room thread to finish
    ri.join() # wait for close_barber thread to finish
    iq = 2
    jr = 0
    while(iq <= barbers): # loop through all barbers 
        malibu[iq].set() # set this event for each check_barber thread to stop
        threadsCB[jr].join() # stop the check_barber thread
        iq += 1
        jr += 1
    print("barber is closed at", ctime())
    




if __name__ == "__main__":
    main()
