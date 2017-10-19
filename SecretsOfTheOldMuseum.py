#!/usr/bin/env python3

'''This is a python script that will print the pages from the CYOA Secrets of the Old Museum.  The "pages" are actually modules and there
will be an attempt at ascii art in the near future.  
'''

import os,sys
import pg1,pg3,pg4,pg5,pg6,pg7,pg9
import pg10,pg11,pg12,pg13,pg14,pg16,pg17,pg18
import pg20,pg21,pg22,pg23,pg25,pg26,pg27,pg28,pg29
import pg30,pg32,pg33,pg34,pg35,pg37,pg38,pg39
import pg40,pg41,pg43,pg44,pg45,pg47,pg48,pg49
import pg50,pg51,pg53,pg54,pg55,pg56,pg58,pg59
import pg60,pg61,pg63,pg64,pg65,pg66,pg67,pg69
import pg70,pg71,pg72,pg73,pg74,pg76,pg77,pg78,pg79
import pg81,pg82,pg83,pg84,pg85,pg86,pg88,pg89
import pg90,pg91,pg92,pg94,pg95,pg96,pg97,pg99


error = "please enter the correct number next time"
prev = "press Enter to go back to the previous page"
end = "Press any key to Exit"

os.system('clear')
os.system('cat title')
print('        ++++++++++ Press Enter to Continue ++++++++++')
answer = input()

os.system('clear')
pg1.text()
answer = input()


if answer == '3':
    os.system('clear')
    pg3.text()
    answer = input()
    os.system('clear')
    pg41.text()
    answer = input()
    
    if answer == '6':
        os.system('clear')
        pg6.text()
        answer = input()
        os.system('clear')
        pg14.text()
        answer = input()
        os.system('clear')
        pg26.text()
        answer = input()
        os.system('clear')
        pg45.text()
        answer = input()
        
        if answer == '56':
            os.system('clear')
            pg56.text()
            answer = input()
            
            if answer == '64':
                os.system('clear')
                pg64.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            elif answer == '60':
                os.system('clear')
                pg60.text()
                answer = input()
                
                if answer == '65':
                    os.system('clear')
                    pg65.text()
                    answer = input()
                       
                    if answer == '78':
                        os.system('clear')
                        pg78.text()
                        answer = input()
                        os.system('clear')
                        pg81.text()
                        answer = input()
                           
                        if answer == '61':
                            os.system('clear')
                            pg61.text()
                            answer = input()
                            os.system('clear')
                            pg96.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                                                        
                        elif answer == '73':
                            os.system('clear')
                            pg73.text()    
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                                
                        elif answer == '77':
                            os.system('clear')
                            pg77.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                            
                        else:
                            print(error)
                            #print(prev)
                            #answer = input()
                            sys.exit()
                            
                    elif answer == '59':
                        os.system('clear')
                        pg59.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                            
                    elif answer == '85':
                        os.system('clear')
                        pg85.text()
                        answer = input()
                        
                        if answer == '58':
                            os.system('clear')
                            pg58.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                                
                        elif answer == '71':
                            os.system('clear')
                            pg71.text()
                            answer = input()
                            
                            if answer == '63':
                                os.system('clear')
                                pg63.text()
                                answer = input()
                                
                                if answer == '78':
                                    os.system('clear')
                                    pg78.text()
                                    answer = input()
                                    os.system('clear')
                                    pg81.text()
                                    answer = input()
                                    
                                    if answer == '61':
                                        os.system('clear')
                                        pg61.text()
                                        answer = input()
                                        os.system('clear')
                                        pg96.text()
                                        print('')
                                        print(end)
                                        answer = input()
                                        sys.exit()
                                        
                                    elif answer == '73':
                                        os.system('clear')
                                        pg73.text
                                        print('')
                                        print(end)
                                        answer = input()
                                        sys.exit()
                                        
                                    elif answer == '77':
                                        os.system('clear')
                                        pg77.text
                                        print('')
                                        print(end)
                                        answer = input()
                                        sys.exit()
                                        
                                    else:
                                        print(error)
                                        #print(prev)
                                        #answer = input()
                                        sys.exit()
                                    
                                elif answer == '59':
                                    os.system('clear')
                                    pg59.text()
                                    print('')
                                    print(end)
                                    answer = input()
                                    sys.exit()
                                    
                                else:
                                    print(error)
                                    #print(prev)
                                    #answer = input()
                                    sys.exit()
                                
                            elif answer == '67':
                                os.system('clear')
                                pg67.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                
                            else:
                                print(error)
                                #print(prev)
                                #answer = input()
                                sys.exit()
                                
                        else:
                            print(error)
                            #print(prev)
                            #answer = input()
                            sys.exit()
                            
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                                                    
                elif answer == '67':
                    os.system('clear')
                    pg67.text()
                    print('')
                    print(end)
                    answer = input()
                    sys.exit()
                    
                else:
                    print(error)
                    #print(prev)
                    #answer = input()
                    sys.exit()
            
            else:
                print(error)
                #print(prev)
                #answer = input()
                sys.exit()
                    
        elif answer == '51':
            os.system('clear')
            pg51.text()
            answer = input()
            
            if answer == '63':
                os.system('clear')
                pg63.text()
                answer = input()
                
                if answer == '78':
                    os.system('clear')
                    pg78.text()
                    answer = input()
                    os.system('clear')
                    pg81.text()
                    answer = input()
                    
                    if answer == '61':
                        os.system('clear')
                        pg61.text()
                        answer = input()
                        os.system('clear')
                        pg96.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '73':
                        os.system('clear')
                        pg73.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '77':
                        os.system('clear')
                        pg77.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                    
                elif answer == '59':
                    os.system('clear')
                    pg59.text()
                    print('')
                    print(end)
                    answer = input()
                    sys.exit()
                    
                else:
                    print(error)
                    #print(prev)
                    #answer = input()
                    sys.exit()
                
            elif answer == '85':
                os.system('clear')
                pg85.text()
                answer = input()
                
                if answer == '58':
                    os.system('clear')
                    pg58.text()
                    print('')
                    print(end)
                    answer = input()
                    sys.exit()
                    
                elif answer == '71':
                    os.system('clear')
                    pg71.text()
                    answer = input()
                    
                    if answer == '63':
                        os.system('clear')
                        pg63.text()
                        answer = input()
                        
                        if answer == '78':
                            os.system('clear')
                            pg78.text()
                            answer = input()
                            os.system('clear')
                            pg81.text()
                            answer = input()
                            
                            if answer == '61':
                                os.system('clear')
                                pg61.text()
                                answer = input()
                                os.system('clear')
                                pg96.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                                                
                            elif answer == '73':
                                os.system('clear')
                                pg73.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                
                            elif answer == '77':
                                os.system('clear')
                                pg77.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                
                            else:
                                print(error)
                                #print(prev)
                                #answer = input()
                                sys.exit()
                            
                        elif answer == '59':
                            os.system('clear')
                            pg59.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                            
                        else:
                            print(error)
                            #print(prev)
                            #answer = input()
                            sys.exit()
                        
                    elif answer == '67':
                        os.system('clear')
                        pg67.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                
                else:
                    print(error)
                    #print(prev)
                    #answer = input()
                    sys.exit()
                
            else:
                print(error)
                #print(prev)   
                #answer = input()
                sys.exit()
            
        else:
            print(error)
            #print(prev)
            #answer = input()
            sys.exit()    
            
    elif answer == '11':
        os.system('clear')
        pg11.text()
        answer = input()
        
        if answer == '13':
            os.system('clear')
            pg13.text()
            answer = input()
           
            if answer == '18':
                os.system('clear')
                pg18.text()
                answer = input()
                os.system('clear')
                pg79.text()
                answer = input()
               
                if answer == '12':
                    os.system('clear')
                    pg12.text()
                    print('')
                    print(end)
                    answer = input()
                    sys.exit()
              
                elif answer == '16':
                    os.system('clear')
                    pg16.text()
                    answer = input()
                    os.system('clear')
                    pg69.text()
                    answer = input()
                  
                    if answer == '49':
                        os.system('clear')
                        pg49.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '55':
                        os.system('clear')
                        pg55.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                        
                else:
                    print(error)
                    #print(prev)   
                    #answer = input()
                    sys.exit()
                
            elif answer == '21':
                os.system('clear')
                pg21.text()
                answer = input()
                                
                if answer == '70':
                    os.system('clear')
                    pg70.text()
                    answer = input()
                   
                    if answer == '86':
                        os.system('clear')
                        pg86.text()
                        answer = input()
                        os.system('clear')
                        pg54.text()
                        answer = input()
                        os.system('clear')
                        pg66.text()
                        answer = input()
                       
                        if answer == '99':
                            os.system('clear')
                            pg99.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                           
                        elif answer == '92':
                            os.system('clear')
                            pg92.text()
                            answer = input()
                          
                            if answer == '72':
                                os.system('clear')
                                pg72.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                               
                            elif answer == '76':
                                os.system('clear')
                                pg76.text()
                                answer = input()
                                
                                if answer == '91':
                                    os.system('clear')
                                    pg91.text()
                                    print('')
                                    print(end)
                                    answer = input()
                                    sys.exit()
                                    
                                elif answer == '95':
                                    os.system('clear')
                                    pg95.text()
                                    print('')
                                    print(end)
                                    answer = input()
                                    sys.exit()
                                    
                                else:
                                    print(error)
                                    #print(prev)
                                    #answer = input()
                                    sys.exit()
                                                                   
                            else:
                                print(error)
                                #print(prev)
                                #answer = input()
                                sys.exit()
                            
                        else:
                            print(error)
                            #print(prev)
                            #answer = input()
                            sys.exit()
                        
                    elif answer == '84':
                        os.system('clear')
                        pg84.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                
                elif answer == '74':
                    os.system('clear')
                    pg74.text()
                    answer = input()
                    
                    if answer == '83':
                        os.system('clear')
                        pg83.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '89':
                        os.system('clear')
                        pg89.text()
                        answer = input()
                        
                        if answer == '94':
                            os.system('clear')
                            pg94.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                            
                        elif answer == '97':
                            os.system('clear')
                            pg97.text()
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                            
                        else:
                            print(error)
                            #print(prev)
                            #answer = input()
                            sys.exit()
                        
                    else:
                        print(error)
                        #print(prev)
                        #answer = input()
                        sys.exit()
                
                else:
                    print(error)
                    #print(prev)
                    #answer = input()
                    sys.exit()
                
            else:
                print(error)
                #print(prev)
                #answer = input()
                sys.exit()
        
        elif answer == '17':
            os.system('clear')
            pg17.text()
            answer = input()
            os.system('clear')
            pg25.text()
            answer = input()
            
            if answer == '33':
                os.system('clear')
                pg33.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            elif answer == '38':
                os.system('clear')
                pg38.text()
                answer = input()
                os.system('clear')
                pg90.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            else:
                print(error)
                #print(prev)
                #answer = input()
                sys.exit()
        else:
            print(error)
            #print(prev)
            #answer = input()
            sys.exit()
    
    else:
        print(error)
        #print(prev)
        #answer = input()
        sys.exit()
            
elif answer == '4':
    os.system('clear')
    pg4.text()
    answer = input()
    os.system('clear')
    pg9.text()
    answer = input()
    os.system('clear')
    pg10.text()
    answer = input()
    
    if answer == '5':
        os.system('clear')
        pg5.text()
        answer = input()
       
        if answer == '27':
            os.system('clear')
            pg27.text()
            answer = input()
            os.system('clear')
            pg28.text()
            answer = input()
            os.system('clear')
            pg29.text()
            answer = input()
            os.system('clear')
            pg30.text()
            answer = input()
          
            if answer == '44':
                os.system('clear')
                pg44.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
               
            elif answer == '48':
                os.system('clear')
                pg48.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            else:
                os.system('clear')
                print(error)
                #print(prev)
                sys.exit()
                            
        elif answer == '23':
            os.system('clear')
            pg23.text()
            answer = input()
            
            if answer == '37':
                os.system('clear')
                pg37.text()
                answer = input()
                os.system('clear')
                pg7.text()
                answer = input()
                
                if answer == '22':
                    os.system('clear')
                    pg22.text()
                    answer = input()
                    
                    if answer == '40':
                        os.system('clear')
                        pg40.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                    
                    elif answer == '50':
                        os.system('clear')
                        pg50.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '53':
                        os.system('clear')
                        pg53.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()   
                        
                    else:
                        os.system('clear')
                        print(error)
                        #print(prev)
                        sys.exit()
                    
                elif answer == '20':
                    os.system('clear')
                    pg20.text()
                    answer = input()
                    
                    if answer == '32':
                        os.system('clear')
                        pg32.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    elif answer == '35':
                        os.system('clear')
                        pg35.text()
                        answer = input()
                        os.system('clear')
                        pg43.text()
                        answer = input()
                        
                        if answer == '47':
                            os.system('clear')
                            pg47.text()
                            answer = input()
                            
                            if answer == '82':
                                os.system('clear')
                                pg82.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                                                
                            elif answer == '88':
                                os.system('clear')
                                pg88.text()
                                print('')
                                print(end)
                                answer = input()
                                sys.exit()
                                
                            else:
                                os.system('clear')
                                print(error)
                                #print(prev)
                                sys.exit()
                                
                        elif answer == '39':
                            os.system('clear')
                            pg39.text
                            print('')
                            print(end)
                            answer = input()
                            sys.exit()
                            
                        else:
                            os.system('clear')
                            print(error)
                            #print(prev)
                            sys.exit
                        
                    else:
                        os.system('clear')
                        print(error)
                        #print(prev)
                        sys.exit()
                else:
                    os.system('clear')
                    print(error)
                    #print(prev)
                    sys.exit()
                
            elif answer == '34':
                os.system('clear')
                pg34.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                           
            else:
                os.system('clear')
                print(error)
                #print(prev)
                sys.exit()
                
        else:
            os.system('clear')
            print(error)
            #print(prev)
            sys.exit()   
    
    elif answer == '7':
        os.system('clear')
        pg7.text()
        answer = input()
        
        if answer == '22':
            os.system('clear')
            pg22.text()
            answer = input()
            
            if answer == '40':
                os.system('clear')
                pg40.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            elif answer == '50':
                os.system('clear')
                pg50.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            elif answer == '53':
                os.system('clear')
                pg53.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
                
            else:
                os.system('clear')
                print(error)
                #print(prev)
                sys.exit()
            
        elif answer == '20':
            os.system('clear')
            pg20.text()
            answer = input()
            
            if answer == '32':
                os.system('clear')
                pg32.text()
                print('')
                print(end)
                answer = input()
                sys.exit()
               
            elif answer == '35':
                os.system('clear')
                pg35.text()
                answer = input()
                os.system('clear')
                pg43.text()
                answer = input()
                
                if answer == '47':
                    os.system('clear')
                    pg47.text()
                    answer = input()
                   
                    if answer == '82':
                        os.system('clear')
                        pg82.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                
                    elif answer == '88':
                        os.system('clear')
                        pg88.text()
                        print('')
                        print(end)
                        answer = input()
                        sys.exit()
                        
                    else:
                        os.system('clear')
                        print(error)
                        #print(prev)
                        sys.exit()
                    
                elif answer == '39':
                    os.system('clear')
                    pg39.text()
                    print('')
                    print(end)
                    answer = input()
                    sys.exit()

                else:
                    os.system('clear')
                    print(error)
                    #print(prev)
                    sys.exit()
                
            else:
                os.system('clear')
                print(error)
                #print(prev)
                sys.exit()
            
        else:
            os.system('clear')
            print(error)
            #print(prev)
            sys.exit()
            
    else:
        os.system('clear')
        print(error)
        #print(prev)
        sys.exit()
            
else:
    os.system('clear')
    print(error)
    #print(prev)
    sys.exit()
