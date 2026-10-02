print("="*25,"Cricket game program","="*25)
def indian_players():
    print(
"rohitshrama-->Batter\n",
"shubmangill-->Batter\n",
"shreyasiyer-->Batter\n ",
"suryakumaryadav-->Batter\n",
"klrahul-->Wicketkeeper\n",
"rishabpant->Wicketkeeper\n",
"jaspritbumrah-->Bowler\n",
"mohammedsiraj-->Bowler\n",
"arshdeepsingh-->Bowler\n",
"kuldeepyadav-->Bowler\n",
"ravindrajadeja-->Allrounder\n",
"axarpatel-->Allrounder\n",
"hardikpandiya-->Allrounder\n",
"yashasvijaiswal-->Batter"
    )
def indian_player_details():
    name=input("Enter the indian player name(11members): ")
    if name=="viratkoli":
        team="INDIA"
        run=9000
        straikerate=234.8
        print("Team in:",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="rohitsharma":
        team="INDIA"
        run=8800
        straikerate=245.9
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="klrahul":
        team="INDIA"
        run=6700
        straikerate=234.6
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="dhoni":
        team="INDIA"
        run=7500
        straikerate=256.9
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="shubmangill":
        team="INDIA"
        run=7600
        straikerate=254.7
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="shreyasiyer":
        team="INDIA"
        run=8500
        straikerate=267.2
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="suryakumaryadav":
        team="INDIA"
        run=8300
        straikerate=254.4
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="jaspritbumrah":
        team="INDIA"
        run=6500
        straikerate=222.4
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="hardikpandiya":
        team="INDIA"
        run=8500
        straikerate=243.8
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="kuldeepyadav":
        team="INDIA"
        run=7677
        straikerate=242.9
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="ravindrajadeja":
        team="INDIA"
        run=8599
        straikerate=239.4
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="axarpatel":
        team="INDIA"
        run=8500
        straikerate=243.6
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="arshdeepsingh":
        team="INDIA"
        run=7553
        straikerate=237.0
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="yashasvijaiswal":
        team="INDIA"
        run=8500
        straikerate=243.8
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    elif name=="mohammedsiraj":
        team="INDIA"
        run=7888
        straikerate=233.9
        print("Team is :",team)
        print("Total Run is:",run)
        print("straike rate is :",straikerate)
    
    else:
        print("Player not found..!!")
def world_cup_win_years():
      print("---world cup win year list----")
      year=int(input("Enter the year (2020-2026): "))
      if year==2020:
          print(f"Won the match cup for Australia in {year}")
      elif year==2021:
          print(f"Won the match cup for India in {year}")
      elif year==2022:
          print(f"Won the match cup for New Zealand in {year}")
      elif year==2023:   
          print(f"Won the match cup for Pakisthan in {year}")
      elif year==2024:
          print(f"Won the match cup for South Africa in {year}")
      elif year==2025:
          print(f"Won the match cup for Sri Lanka in {year}")
      elif year==2026:
          print(f"Won the match cup for Afkanisthan in {year}")
      else:
          print("Not found year...!!!")
def indian_cup_win_details():
        team=input("Enter the team name (csk/rcb/pkbs/kkr/rr/dc/srh/lsg/mi/)")
        if team=="csk":
            print("Total cup of wins in 5cups")
        elif team=="rcb":
            print("Total cup of wins in 2cups")
        elif team=="pbks":
            print("Total cup of wins in 0 cups")
            print("Trying for next year")
        elif team=="kkr":
            print("Total cup of wins in 3cups")
        elif team=="rr":
            print("Total cup of wins in 2cups")
        elif team=="dc":
            print("Total cup of wins in 0cups")
            print("Trying for next year")
        elif team=="srh":
            print("Total cup of wins in 2cups")
        elif team=="lsg":
            print("Total cup of wins in 0cups")
            print("Trying for next year")
        elif team=="mi":
            print("Total cup of wins in 5cups")
        elif team=="gt":
            print("Total cup of wins in 1cups")
        else:
            print("Team not found!!!!")
indian_players()
indian_player_details()
world_cup_win_years()
indian_cup_win_details()
