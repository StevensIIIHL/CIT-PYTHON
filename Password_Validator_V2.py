
# Functions for validation
def validate_password( sPassword, sName ):

    result = ''

    sPWR = password_occurrences( sPassword )
    print( " sPWR: ", sPWR )
    sPWL = password_length( sPassword )
    print( " sPWL: ", sPWL )
    #sPWS = password_check_special_character( sPassword )
    sPWInit = password_check_initials( sPassword, sName )
    sPWCaseChkUp = password_check_upper_case( sPassword )
    print( " sPWCaseChkUp: ", sPWCaseChkUp )
    sPWCaseChkLow = password_check_lower_case( sPassword )
    print( " sPWCaseChkLow: ", sPWCaseChkLow )
    sPWNumChk = password_check_number( sPassword )
    sPWPassChk = password_check_pass( sPassword )
    print( " sPWPassChk: ", sPWPassChk )
    
    if sPWL == 'p' and sPWPassChk == 'p' and sPWR == 'p' and sPWCaseChkUp == 'p' and sPWCaseChkLow == 'p':
        print( "Password is valid and ok to use" )
        result = 'p'
        return result
    
    else:
        result = 'f'
        return result

# Function to check inclusion of a number
def password_check_number( sPassword ):

    print( " password_check_number " )
    result = ''
    x = 1
    for i in sPassword:
        print( "password_check_number for loop" )
        while x <= 9:
            print( "password_check_number while loop" )
            sNum = str(x)
            print( sNum + " num" )
            print( i )
            if sNum == i:
                print( " is a number " )
                result = 'p'
            x += 1
    return result

# Function to check upper case
def password_check_upper_case( sPassword ):

    result = 'f'
    upperExist = ''
    #print( " is upper function " )
    for char in sPassword:
        #print( " is upper loop " )
        if char.isupper():
            #print( " is upper " )
            result = 'p'
            upperExist = 'y'
    if upperExist != 'y':
        print( "Password must contain at least 1 uppercase letter" )
    #print( result )
    return result

# Function to check lower case
def password_check_lower_case( sPassword ):

    result = 'f'
    lowerExist = ''
    
    #print( " is upper function " )
    for char in sPassword:
        #print( " is upper loop " )
        if char.islower():
            #print( " is upper " )
            result = 'p'
            lowerExist = 'y'
    if lowerExist != 'y':
        print( "Password must contain at least 1 lowercase letter" )
    #print( result )

    return result

# Function to check is password starts with "Pass"
def password_check_pass( sPassword ):

    result = ''

    if sPassword[0:4].lower() == "pass":
        print( "Password can not start with Pass" )
        result = 'f'
    else:
        result = 'p'

    return result

# Function to check special characters
def password_check_special_character( sPassword ):

    result = ''

    return result

# Function to check Length, between 8 and 12 characters long
def password_length( sPassword ):

    result = ''

    if len( sPassword ) < 8 or len( sPassword ) > 12:
        print( "Password must be between 8 and 12 characters" )
        result = 'f'
    else:
        result = 'p'

    return result

# Function to check occurrences
def password_occurrences( sPassword ):

    result = 'p'

    sPassword = sPassword.lower()
    bMultiOcc = False
    char_count = {}
    for char in sPassword:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    char_repeats = { char: count for char, count in char_count.items() if count > 1 }
    #print( char_repeats )
    for value in char_repeats.values():
        if value > 1:
            bMultiOcc = True
    if bMultiOcc == True:
        result = 'f'
        print( "These characters appear more than once: " )
        for char, count in char_repeats.items():
            print( f"{char}: {count} times" )
    else:
        result = 'p'
    return result

# Function to get Initials
def password_check_initials( sPassword, sName ):

    sInput = 'f'

    sFirstInit = sName[0]
    sIndex = sName.find(' ')+1
    sLastInit = sName[ sIndex ]
    sInitials = sFirstInit + sLastInit
    print( sInitials )
    for i in sPassword:
        if i == sInitials[0]:
            print( " Initials in Password " )

    return sInput

# Function to get input
def get_password():

    sInput = ''

    print( "Pleast enter a new password to validate: " )
    sInput = input( sInput )

    return sInput

# Function to get name
def get_name():

    sName = ''

    print( "Please enter your name: " )
    sName = input( sName )

    return sName

# Main Function
def Main():

    print( "Welcome to the Password Validator!" )
    sName = get_name()
    again = 'y'
    while again == "y":
        sPassword = get_password()
        sPWGood = validate_password( sPassword, sName )
        if sPWGood == 'p':
            again = 'n'
            
# Main Call
Main()
