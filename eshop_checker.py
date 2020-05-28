import datetime,os,requests,time,winsound

error = "\nAn error has occurred. Please ensure that the web address matches the syntax detailed above. "\
        "Otherwise check to make sure that the website is reachable. Press enter to exit."
banner = "eShop Checker\n-------------\n"
test_error = 0

def validate_num(u_input,upper_limit):
    while u_input.isdigit() == False or int(u_input) < 1 or int(u_input) > upper_limit:
        u_input = input("Please enter a number between 1 and " + str(upper_limit) + ": ")
        
    return u_input

def beep(ditty):
    if ditty == 1:
        winsound.Beep(4000,300)
        winsound.Beep(4000,300)
        winsound.Beep(4000,300)
    elif ditty == 2:
        winsound.Beep(3000,300)
        winsound.Beep(3000,300)
        winsound.Beep(3000,300)
    elif ditty == 3:
        winsound.Beep(2000,300)
        winsound.Beep(2000,300)
        winsound.Beep(2000,300)
    else:
        winsound.Beep(1000,400)

def main(banner,delim,snip,web):
    YELLOW = '\033[33m'
    BLUE = '\033[96m'
    RESET = '\033[m'
    VAR_COLOUR = RESET
    colour_count = 0
    stop = "can't"
    last_change = "Nothing yet."
    ad_list = []
    errors = 0

    s_get = str(requests.get(s_url).content)
    ads_on_page = s_get.count(delim)
    if ads_on_page >= 10:
        ads_on_page = 10
    for ad_position in range(1,ads_on_page+1):
        ad_list.append(s_get.split(delim)[ad_position][0:snip])
            
    while stop == "can't":
        retry_query = 0
        try:
            s_get = str(requests.get(s_url).content).split(delim)[1][0:snip]
        except:
            if errors < 3:
                print ("An error has occurred. Retrying query.")
                beep(10)
                errors += 1
                retry_query = 1
                time.sleep(3)
            else:
                beep(10)
                beep(10)
                input ("\nToo many errors have occurred in succession. Check that the site you are querying is still reachable. Press enter to exit.")
                sys.exit()
        if retry_query == 0:
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            if colour_count > 0:
                colour_count -= 1
            os.system('cls')
            print (banner + "Querying: " + s_url + "\nSnippet of top item: " + s_get + ".\n")
            if s_get in ad_list:
                pass            
            else:
                ad_list.append(s_get)
                if len(ad_list) > 1:
                    last_change = time_now
                    colour_count = 40
            if colour_count != 40:
                VAR_COLOUR = RESET
            else:
                VAR_COLOUR = YELLOW
            print("Time of last query: " + VAR_COLOUR + time_now + RESET)
            if colour_count > 25:
                VAR_COLOUR = YELLOW
            elif colour_count > 0:
                VAR_COLOUR = BLUE
            else:
                VAR_COLOUR = RESET
            print("New listing detected: " + VAR_COLOUR + last_change + RESET + "\n\nCtrl + C to exit program.\n")
            if last_change == time_now and len(ad_list) > 1:
                beep(web)
            if len(ad_list) > 20:
                ad_list = ad_list[10:]
            time.sleep(10)
            if errors != 0:
                errors -= 1

s_website = int(validate_num(input(banner + "Which website would you like to query?"\
                                   "\n1 - eBay"\
                                   "\n2 - Gumtree"\
                                   "\n3 - Custom search"\
                                   "\n4 - Exit"\
                                   "\n\nPlease enter a number between 1 and 4: "),4))

if s_website == 1:
    os.system('cls')
    s_url = input(banner + "Enter the eBay web address you would like to monitor.\n"\
                  "Example: https://www.ebay.com/sch/i.html?_nkw=teapot+cozy&_sop=10\n"\
                  "Or: https://www.ebay.com/b/Watches-Parts-Accessories/260324/bn_2408535?rt=nc&_sop=10\n\n"\
                  "(Note: '&_sop=10' is required at the end of the web address to sort ads by new.)\n\n")
    if "i.html?_" in s_url:
        s_delimiter = 'img alt="'    
    else:
        s_delimiter = 'img" alt="'
    s_snippet = 70

if s_website == 2:
    s_delimiter = '"","title":"'
    s_snippet = 90
    os.system('cls')
    s_url = input(banner + "Enter the Gumtree web address you would like to monitor.\n"\
                  "Example: https://www.gumtree.com.au/s-plants/cactus/k0c20102\n\n")
elif s_website == 3:
    os.system('cls')
    s_url = input(banner + "Enter the web address of the page that you would like to monitor.\n"\
                  "For example, to search for boots on Gumtree, enter \"https://www.gumtree.com.au/s-clothing-jewellery/boots/k0c18308\"\n\n")
    os.system('cls')
    s_delimiter = input(banner + "Enter the section of html code on the page that signals the start of each ad.\n"
                        "For example, on a Gumtree page, if you look at the source code of the entire page,\n"\
                        "before each ad there is the html code \'\"\",\"title\":\"\'. This is what is required to detect new ads.\n"\
                        "To get the source code of a webpage, right click on a blank section of the page and select 'View Page Source'.\n\n")
    s_snippet = 90

if s_website != 4:
    try:
        print ("\nTesting queries with website. Please wait.")
        test = str(requests.get(s_url).content).split(s_delimiter)[1]
    except:
        input(error)
        test_error = 1
    if test_error == 0:
        main(banner,s_delimiter,s_snippet,s_website)
