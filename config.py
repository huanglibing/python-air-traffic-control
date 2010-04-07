#   File: config.py
#   Author: Tom Woolfrey

class Config:

    GAMETIME = 180000;                  #Game length in milliseconds
    NUMBEROFAIRCRAFT = 20;              #Number of aircraft spawning during the game
    NUMBEROFDESTINATIONS = 6;           #Number of destinations spawning during the game
    FRAMERATE = 40                      #Framerate of the main game loop

    MAX_WAYPOINTS = 6;                  #Max user-selectable waypoints per a/c
    
    COLOR_DEST = (192, 192, 192)        #Destination colour
    COLOR_SCORETIME = (20, 193, 236)    #Score/time counter colour

    #Difficulty HARD
    DH_AIRCRAFT = 50;                   #Num aircraft
    DH_DEST = 12;                       #Num destinations

    #Difficulty MEDIUM
    DM_AIRCRAFT = 25;                   #Num aircraft
    DM_DEST = 8;                        #Num destinations

    #Difficulty EASY
    DE_AIRCRAFT = 15;                   #Num aircraft
    DE_DEST = 2;                        #Num destinations

    SCORE_REACHDEST = 100               #Score for reaching destination
    SCORE_OBS_COLLIDE = -25             #Score for hitting obstacle
    SCORE_AC_COLLIDE = -25              #Score for hitting aircraft

    AC_SPEED_DEFAULT = 0.5              #Aircraft starting speed
    AC_COLLISION_RADIUS = 30            #Aircraft collision radius (pixels)
    AC_DRAW_COLLISION_RADIUS = True    #Draw collision radius?
