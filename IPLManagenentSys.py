class Player:
    def __init__(self, name, role):
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_role(self):
        return self.__role

    def set_role(self, role):
        self.__role = role

    def __str__(self):
        return f"{self.__name} ({self.__role})"

class Batsman(Player):
    def __init__(self, name, runs):
        super().__init__(name, "Batsman")
        self.__runs = runs

    def get_runs(self):
        return self.__runs

    def set_runs(self, runs):
        self.__runs = runs

    def __str__(self):
        return f"{self.get_name()} (Batsman) - Runs: {self.__runs}"

class WicketKeeperBatsman(Batsman):
    def __init__(self, name, runs, stumpings):
        super().__init__(name, runs)
        self.__stumpings = stumpings
        self.set_role("WicketKeeper Batsman")

    def get_stumpings(self):
        return self.__stumpings

    def set_stumpings(self, stumpings):
        self.__stumpings = stumpings

    def __str__(self):
        return f"{self.get_name()} (WicketKeeper Batsman) - Runs: {self.get_runs()}, Stumpings: {self.__stumpings}"

class Bowler(Player):
    def __init__(self, name, wickets):
        super().__init__(name, "Bowler")
        self.__wickets = wickets

    def get_wickets(self):
        return self.__wickets

    def set_wickets(self, wickets):
        self.__wickets = wickets

    def __str__(self):
        return f"{self.get_name()} (Bowler) - Wickets: {self.__wickets}"

class AllRounder(Player):
    def __init__(self, name, runs, wickets):
        super().__init__(name, "AllRounder")
        self.__runs = runs
        self.__wickets = wickets

    def get_runs(self):
        return self.__runs

    def set_runs(self, runs):
        self.__runs = runs

    def get_wickets(self):
        return self.__wickets

    def set_wickets(self, wickets):
        self.__wickets = wickets

    def __str__(self):
        return f"{self.get_name()} (AllRounder) - Runs: {self.__runs}, Wickets: {self.__wickets}"

class Team:
    def __init__(self, name):
        self.__name = name
        self.__players = []

    def add_player(self, player):
        self.__players.append(player)

    def get_players(self):
        return self.__players

    def get_name(self):
        return self.__name

    def __str__(self):
        return f"Team: {self.__name}"

# Example usage
if __name__ == "__main__":
    # Create 5 IPL teams in order: CSK, MI, KKR, SRH, RCB
    csk = Team("Chennai Super Kings")
    mi = Team("Mumbai Indians")
    kkr = Team("Kolkata Knight Riders")
    srh = Team("Sunrisers Hyderabad")
    rcb = Team("Royal Challengers Bangalore")

    # Add players to CSK
    csk.add_player(WicketKeeperBatsman("MS Dhoni", 5000, 120))
    csk.add_player(Batsman("Ruturaj Gaikwad", 1800))
    csk.add_player(Bowler("Deepak Chahar", 80))
    csk.add_player(AllRounder("Ravindra Jadeja", 2500, 120))

    # Add players to MI
    mi.add_player(Batsman("Rohit Sharma", 6000))
    mi.add_player(WicketKeeperBatsman("Ishan Kishan", 2000, 30))
    mi.add_player(Bowler("Jasprit Bumrah", 145))
    mi.add_player(AllRounder("Hardik Pandya", 1700, 60))

    # Add players to KKR
    kkr.add_player(Batsman("Shreyas Iyer", 2200))
    kkr.add_player(WicketKeeperBatsman("Rahmanullah Gurbaz", 800, 10))
    kkr.add_player(Bowler("Sunil Narine", 150))
    kkr.add_player(AllRounder("Andre Russell", 1800, 90))

    # Add players to SRH
    srh.add_player(Batsman("Abhishek Sharma", 1200))
    srh.add_player(WicketKeeperBatsman("Heinrich Klaasen", 900, 15))
    srh.add_player(Bowler("Bhuvneshwar Kumar", 160))
    srh.add_player(AllRounder("Washington Sundar", 600, 40))

    # Add players to RCB
    rcb.add_player(Batsman("Virat Kohli", 7000))
    rcb.add_player(WicketKeeperBatsman("Dinesh Karthik", 4000, 100))
    rcb.add_player(Bowler("Mohammed Siraj", 70))
    rcb.add_player(AllRounder("Glenn Maxwell", 2500, 50))

    # Store all teams
    teams = [csk, mi, kkr, srh, rcb]

    # Iterate and display all teams and their players
    for team in teams:
        print(team)
        for player in team.get_players():
            print("  -", player)

#OUTPUT🫡:
Team: Chennai Super Kings
  - MS Dhoni (WicketKeeper Batsman) - Runs: 5000, Stumpings: 120
  - Ruturaj Gaikwad (Batsman) - Runs: 1800
  - Deepak Chahar (Bowler) - Wickets: 80
  - Ravindra Jadeja (AllRounder) - Runs: 2500, Wickets: 120
Team: Mumbai Indians
  - Rohit Sharma (Batsman) - Runs: 6000
  - Ishan Kishan (WicketKeeper Batsman) - Runs: 2000, Stumpings: 30
  - Jasprit Bumrah (Bowler) - Wickets: 145
  - Hardik Pandya (AllRounder) - Runs: 1700, Wickets: 60
Team: Kolkata Knight Riders
  - Shreyas Iyer (Batsman) - Runs: 2200
  - Rahmanullah Gurbaz (WicketKeeper Batsman) - Runs: 800, Stumpings: 10
  - Sunil Narine (Bowler) - Wickets: 150
  - Andre Russell (AllRounder) - Runs: 1800, Wickets: 90
Team: Sunrisers Hyderabad
  - Abhishek Sharma (Batsman) - Runs: 1200
  - Heinrich Klaasen (WicketKeeper Batsman) - Runs: 900, Stumpings: 15
  - Bhuvneshwar Kumar (Bowler) - Wickets: 160
  - Washington Sundar (AllRounder) - Runs: 600, Wickets: 40
Team: Royal Challengers Bangalore
  - Virat Kohli (Batsman) - Runs: 7000
  - Dinesh Karthik (WicketKeeper Batsman) - Runs: 4000, Stumpings: 100
  - Mohammed Siraj (Bowler) - Wickets: 70
  - Glenn Maxwell (AllRounder) - Runs: 2500, Wickets: 50
