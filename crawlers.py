

def all_games(page_soup):
    league=["arsenal",'manchester city','liverpool','man utd','tottenham hotspur','chelsea','burnley','leicester city','watford','brighton','everton','bournmouth','swansea','west ham united','huddersfield town','swansea city','newcastle united','southampton','west bromwich albion','crystal palace','afc bournemouth']
    # league=["arsenal",'manchester city','liverpool','man utd','tottenham','chelsea','burnley','leicester city','watford','brighton','everton','bournmouth','swansea','west ham united','huddersfield town','swansea city','newcastle united','southampton','west bromwich albion','crystal palace']
    li=page_soup.findAll("li",{"class":"gs-u-pb-"})
    # print(len(li))
    matches_list=[]
    for i in range(len(li)):
        col = li[i].findAll("span",{"class":"gs-u-display-none"})
        masaa = li[i].findAll("span", {"class":"sp-c-fixture__status"})
        start_time = li[i].findAll("span",{"class":"sp-c-fixture__number sp-c-fixture__number--time"})
        # print(masaa[0].text)
        if len(masaa)>0:
            rem = masaa[0].text
        else:
            rem = "not started"
        if len(start_time)>0:
            start_time = start_time[0].text
        else:
            start_time = None
        home=col[0].text
        away=col[1].text
        # print(home.lower(),away.lower())
        if home.lower() in league or away.lower() in league:
            matchDict = { "home": col[0].text, "away": col[1].text,"status":rem,"time":start_time }
            matches_list.append(matchDict)
            # print(matchDict)
    print("first game",matches_list)
    return matches_list

def check_games(all_games_dict,page_soup):
    league=["arsenal",'manchester city','liverpool','man utd','tottenham hotspur','chelsea','burnley','leicester city','watford','brighton','everton','bournmouth','swansea','west ham united','huddersfield town','swansea city','newcastle united','southampton','west bromwich albion','crystal palace','afc bournemouth']
    li=page_soup.findAll("li",{"class":"gs-u-pb-"})
    # print(len(li))
    status=False
    matches_list=[]
    for i in range(len(li)):
        col = li[i].findAll("span",{"class":"gs-u-display-none"})
        masaa = li[i].findAll("span", {"class":"sp-c-fixture__status"})
        start_time = li[i].findAll("span",{"class":"sp-c-fixture__number sp-c-fixture__number--time"})
        # print(masaa[0].text)
        if len(masaa)>0:
            rem = masaa[0].text
            status=True
        else:
            rem = "not started"
            status=False
        if len(start_time)>0:
            start_time = start_time[0].text
        else:
            start_time = None
        home=col[0].text
        away=col[1].text
        # print(home.lower(),away.lower())
        if home.lower() in league or away.lower() in league:
            matchDict = { "home": col[0].text, "away": col[1].text,"status":rem,"time":start_time }
            matches_list.append(matchDict)
            # print(matchDict)
    # print(matches_list,len(matches_list))
    print("second game",matches_list[0])
    
    return status,matches_list