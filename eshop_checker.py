try:
    import datetime, os, requests, time

    if os.name == 'nt':
        x_clear = "cls"
        x_os = 'win'
        try:
            from winsound import Beep
        except:
            print("There was an issue importing the winsound Beep function. "
                  "The program may not beep when a new item has been uploaded.")
            x_os = 'na'
    elif os.name == 'posix':
        x_clear = "clear"
        x_os = 'na'
    else:
        x_clear = ""
        x_os = 'na'

    #YELLOW = '\033[33m'
    #BLUE = '\033[96m'
    #RESET = '\033[m'
    #VAR_COLOUR = RESET
    ad_list = []

    def beep(x):
        if x == 'win':
            Beep(4000,300)
            Beep(4000,300)
            Beep(4000,300)

    u_input = 0
    print("eShop Checker\n-------------\n"
          "Which website would you like to query?"
          "\n1 - eBay"
          "\n2 - Gumtree"
          "\nExit (Enter)\n")
    while u_input != "" and u_input != "1" and u_input != "2":
        u_input = input()
        if u_input != "" and u_input != "1" and u_input != "2":
            print("Please enter either 1 or 2. Otherwise press enter to exit.")

    if x_os != 'na':
        os.system(x_clear)

    if u_input == "1":
        s_url = input("Enter the eBay web address you would like to monitor.\n"
                      "Example: https://www.ebay.com/sch/i.html?_nkw=teapot+cozy&_sop=10\n"
                      "Or: https://www.ebay.com/b/Watches-Parts-Accessories/260324/bn_2408535?rt=nc&_sop=10\n\n"
                      "(Note: '&_sop=10' is required at the end of the web address to sort ads by new.)\n\n")
        if "i.html?_" in s_url:
            delim = 'img alt="'
        else:
            delim = 'img" alt="'
        snip = 70
    elif u_input == "2":
        s_url = input("Enter the Gumtree web address you would like to monitor.\n" 
                               "Example: https://www.gumtree.com.au/s-plants/cactus/k0c20102\n\n")
        delim = '"","title":"'
        snip = 90
    else:
        exit()

    s_get = str(requests.get(s_url).content)
    ads_on_page = s_get.count(delim)
    if ads_on_page >= 10:
        ads_on_page = 10
    for ad_position in range(1,ads_on_page+1):
        ad_list.append(s_get.split(delim)[ad_position][0:snip])

    last_change = "n/a"
    # run indefinitely
    while 1 == 1:
        try:
            s_get = str(requests.get(s_url).content).split(delim)[1][0:snip]
        except:
            print ("An error has occurred.")
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        if x_os != 'na':
            os.system(x_clear)
        print ("Querying: " + s_url + "\nSnippet of top item: " + s_get + ".\n")
        if s_get not in ad_list:
            ad_list.append(s_get)
            if len(ad_list) > 1:
                last_change = time_now
        print("Time of last query: {}".format(time_now))
        print("New listing detected: {}\n\nCtrl + C to exit program.\n".format(last_change))
        if last_change == time_now and len(ad_list) > 1:
            beep(x_os)
        if len(ad_list) > 20:
            ad_list = ad_list[10:]
        time.sleep(10)
except Exception as e:
    input(e)
