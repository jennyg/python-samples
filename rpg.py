'''
Description:
This is a modified version of a homework assignment. It's a
simple fighting game that creates and uses a Fighter class,
and has two instances of that class battle against each, RPG-style.
The user of this program will press enter in between each round of the
fight to continue it, and the program will end when one of the
instances is "killed" by losing all of its hit points.
'''
 
import random
 
class Fighter:
    '''
    This class controls instances of Fighter characters, with methods
    including an __init__ that sets initial attributes, and __repr__
    that returns a string of the instance's name and hit points
    attributes. Its functions include take_damage and attack, which
    affect the instances' hit points and print outcomes of battles.
    '''
 
    def __init__(self, name):
        '''
        To initialize an instance of this class, it requires a string
        value to be passed to its name parameter. The instance variables
        it initializes are name (a string), hit points (starting at 10),
        sads, the numbers of tears that the fighter has cried, denoting
        each hit the instance has received, and luck, a bonus that will
        increase with every successful hit.
        '''
        self.name = name
        self.hit_points = 10
        self.sads = 0
        self.luck = 0
        return None
     
    def __repr__(self):
        '''
        When printing an instance of this class, this sets its return
        value to a string displaying the name and hit points attributes.
        '''
        return (self.name +' (HP: ' + str(self.hit_points) + ', crying ' +
           str(self.sads) + ' tears, and +' + str(self.luck) + ' luck.)')
     
    def take_damage(self, damage_amount):
        '''
        This function changes the value of an instance's hit points by
        subtracting a given integer damage amount. Then, it checks to
        see if the value of hit points indicates that the instance has
        "died." It then prints the status of the instance.
        '''
        self.hit_points = (self.hit_points - damage_amount)
        if self.hit_points <= 0:
            print('\tAlas, ' + self.name + ' has fallen!')
        else:
            print('\t' + self.name + ' has ' + str(self.hit_points)
                 + ' hit points remaining, has shed ' +
                 str(self.sads) + ' tears, and has +' + str(self.luck) + ' luck.')
        return None
         
    def attack(self, other):
        '''
        When given two instances of the Fighter class (self and the
        value of the "other" parameter), first generates a random
        integer between 1 and 20 inclusive to see if the hit lands.
        If the hit misses, print a message indicating that.
        If the hit lands, generates a random integer between 1 and 6
        inclusive that is the value of the damage.
        Then, calls the take_damage function.
        If a critical hit, the other fighter will die, and
        the first fighter will gain 100 luck, and the other
        fighter will have 100 sads added to their total.
        '''
        print(self.name + ' attacks ' + other.name + '!')
        hit = random.randrange(1, 21)
        if hit >= 12:
            damage = random.randrange(1, 11)
            if damage >= other.hit_points:
               print('\tCritical hit!')
               other.take_damage(damage)
               other.sads = 100
               self.luck = 100
            else:
               print('\tHits for ' + str(damage) + ' hit points!')
               other.take_damage(damage)
               other.sads += 1
        else:
            print('\t Misses!')
            other.luck += 1
        return None
 
#==================== END of Fighter class ====================
 
         
def combat_round(first_fighter, second_fighter):
    '''
    In this function, which is not part of the Fighter class, two
    instances of that class are passed to it, as the first_fighter and
    second_fighter parameters.
    A random number between 1 and 6 inclusive is generated to determine
    the order of their turns.
    The possibilities include either a simultaneous "roll" in which
    they both attack (meaning that the attacks will both occur even if
    one of the players has died in the other attack), or that either
    the first_fighter or second_fighter will be allowed to make the
    first attack of the round.
    If not simultaneous, the second attack of the round will only do so
    if still alive after the first attack of the round.
    '''
    #simulates each fighter rolling a 20-sided die
    first_fighter_roll = random.randrange(1, 7)
    second_fighter_roll = random.randrange(1, 7)
     
    #if/elif/else the three possible cases when comparing the rolls
    if first_fighter_roll == second_fighter_roll:
        print('Simultaneous!')
        first_fighter.attack(second_fighter)
        second_fighter.attack(first_fighter)
    elif first_fighter_roll < second_fighter_roll:
            first_fighter.attack(second_fighter)
            #second fighter only attacks if alive
            if second_fighter.hit_points > 0:
                second_fighter.attack(first_fighter)
    else:
        second_fighter.attack(first_fighter)
        #first fighter only attacks if alive
        if first_fighter.hit_points > 0:
            first_fighter.attack(second_fighter)
    return None
 
#==========================================================
def main():
    '''
    Creates two instances of the Fighter class, and uses a while loop
    to repeatedly use the various functions to simulate combat between
    the two instances, terminating when one or both instances have
    died. Requires the user to press enter between each round, but
    otherwise does not involve any user interaction.
    '''
    bonzo = Fighter('Bonzo')
    ender = Fighter('Ender')
     
    i = 1
    while bonzo.hit_points > 0 and ender.hit_points > 0:
        print('\n' + ('=' * 20).ljust(20) + ' Round ' +
            str(i) + (' '+'=' * 20).rjust(20))
        print(bonzo)
        print(ender)
        raw_input('Enter to Fight!')
        combat_round(bonzo, ender)
        i += 1
         
    print('\nThe battle is over!')
    print(bonzo)
    print(ender)
     
if __name__ == '__main__':
    main()
