from dataclasses import dataclass ,field
@dataclass 
class Player:
    name: str
    player_id :str
    games_played :int = 0
    points: list[int] = field(default_factory=list)
    
    def record_game(self, pts: int):
        self.games_played += 1
        self.points.append(pts)

    def  avg_points(self) -> float:
        if self.games_played== 0:
            return 0.0
        return sum(self.points)/self.games_played
    
@dataclass            
class Team:
    team_name:str
    coach:str
    max_roster: int
    players :list[Player] = field(default_factory=list)
    roster_size: int = field(init=False)


    def __post_init__(self):
        self._refresh()

    def _refresh(self):
        self.roster_size = len(self.players)


    def sign(self, player: Player) -> bool :
        if self.roster_size >= self.max_roster:
            return False
        self.players.append(player)
        self._refresh()
        return True
    
    def mvp(self) -> str:
        if self.roster_size ==0 :
            return "No data"
        
        the_highest_avg = 0.0
        best_player = None

        for player in self.players:
            avg = player.avg_points()
            if avg > the_highest_avg:
                the_highest_avg = avg
                best_player= player.name
        if best_player is None or the_highest_avg == 0.0:
            return "No data"
        
        return best_player
    
    def team_stats(self) -> str:
        lines = [f"{self.team_name} ({self.coach}):"]
    
        for i, player in enumerate(self.players, start=1):
            lines.append(
                f"  {player.name} - {player.games_played} games, avg {player.avg_points():.1f} pts"
            )
        
        lines.append(f"Roster: {self.roster_size}/{self.max_roster}")
        return "\n".join(lines) 
p1 = Player("Alex", "P01")
p2 = Player("Jordan", "P02")
p3 = Player("Sam", "P03")

p1.record_game(18)
p1.record_game(24)
p1.record_game(21)
p2.record_game(30)
p2.record_game(27)
p3.record_game(12)

t = Team("Thunder", "Coach Rivers", 3)
print(t.sign(p1))
print(t.sign(p2))
print(t.sign(p3))
print(t.sign(Player("Taylor", "P04")))
print(t.roster_size)
print(t.mvp())
print(t.team_stats())
       
