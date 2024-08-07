
# find month and it's season


def find_season(month):

    match month:
        
        case "January":
            print("Winter season")
        
        case "February":    
             print("Spring season")

        case "March":    
             print("Spring season")   

        case "April":    
             print("Spring season")          
        
        case "May":    
             print("Summer season")   

        case "June":    
             print("Summer season")   
        
        case "July":    
             print("Summer season")   
        
        case "August":    
             print("Autumn season")   

        case "September":    
             print("Autumn season")  

        case "October":    
             print("Autumn season")    

        case "November":
              print("Winter season")     

        case "December":
              print("Winter season")     

find_season("January".capitalize())
find_season("August".capitalize())
find_season("November".capitalize())