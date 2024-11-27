class Athlete:
    def __init__(self, first_name, last_name, age, nationality, medals):
        self.first_name = first_name  
        self.last_name = last_name    
        self.age = age                
        self.nationality = nationality 
        self.medals = medals          

    def get_info(self):
        return f"Ism: {self.first_name} {self.last_name}, Yosh: {self.age}, Millat: {self.nationality}, Medallar soni: {self.medals}"

    def introduce(self):
        return f"Salom, men {self.first_name} {self.last_name}. Men {self.nationality} millatiga mansub sportchiman."


class FootballPlayer(Athlete):
    def __init__(self, first_name, last_name, age, nationality, medals, league, goals, position):
        super().__init__(first_name, last_name, age, nationality, medals)
        self.league = league         
        self.goals = goals            
        self.position = position      

    def get_info(self):
        athlete_info = super().get_info()
        return f"{athlete_info}, Liga: {self.league}, Gollar soni: {self.goals}, Pozitsiya: {self.position}"

    def introduce(self):
        return super().introduce() + f" Men {self.position} pozitsiyasida {self.league} ligasida o'ynayman."


class BasketballPlayer(Athlete):
    def __init__(self, first_name, last_name, age, nationality, medals, team, points_per_game, position):
        super().__init__(first_name, last_name, age, nationality, medals)
        self.team = team            
        self.points_per_game = points_per_game  
        self.position = position      

    def get_info(self):
        athlete_info = super().get_info()
        return f"{athlete_info}, Jamoa: {self.team}, O'rtacha ballar soni: {self.points_per_game}, Pozitsiya: {self.position}"

    def introduce(self):
        return super().introduce() + f" Men {self.team} jamoasining {self.position} pozitsiyasida o'ynayman."


class TennisPlayer(Athlete):
    def __init__(self, first_name, last_name, age, nationality, medals, ranking, tournaments_won):
        super().__init__(first_name, last_name, age, nationality, medals)
        self.ranking = ranking                    
        self.tournaments_won = tournaments_won    

    def get_info(self):
        athlete_info = super().get_info()
        return f"{athlete_info}, Jahon reytingi: {self.ranking}, Yutuqlar soni: {self.tournaments_won}"

    def introduce(self):
        return super().introduce() + f" Men {self.ranking}-o'rinda turib, {self.tournaments_won} ta turnir yutganman."


class Swimmer(Athlete):
    def __init__(self, first_name, last_name, age, nationality, medals, style, records_broken):
        super().__init__(first_name, last_name, age, nationality, medals)
        self.style = style                
        self.records_broken = records_broken 

    def get_info(self):
        athlete_info = super().get_info()
        return f"{athlete_info}, Stil: {self.style}, Sindirilgan rekordlar soni: {self.records_broken}"

    def introduce(self):
        return super().introduce() + f" Men {self.style} stilida suzaman va {self.records_broken} ta rekordni sindirdim."


class TrackAthlete(Athlete):
    def __init__(self, first_name, last_name, age, nationality, medals, distance, personal_best):
        super().__init__(first_name, last_name, age, nationality, medals)
        self.distance = distance               
        self.personal_best = personal_best     

    def get_info(self):
        athlete_info = super().get_info()
        return f"{athlete_info}, Masofa: {self.distance}, Eng yaxshi natija: {self.personal_best}"

    def introduce(self):
        return super().introduce() + f" Men {self.distance} metr masofada yuguraman va eng yaxshi natijam {self.personal_best}."

athlete = Athlete("Tamerlan", "Azizov", 28, "O'zbek", 5)
print(athlete.get_info())
print(athlete.introduce())


football_player = FootballPlayer("Jasur", "Rahmatov", 25, "O'zbek", 3, "Premier Liga", 15, "Forvard")
print(football_player.get_info())
print(football_player.introduce())


basketball_player = BasketballPlayer("Daler", "Shukurov", 22, "O'zbek", 2, "Samarqand Team", 25.4, "Guard")
print(basketball_player.get_info())
print(basketball_player.introduce())


tennis_player = TennisPlayer("Sanjar", "Kamilov", 30, "O'zbek", 8, 5, 10)
print(tennis_player.get_info())
print(tennis_player.introduce())

swimmer = Swimmer("Olim", "Xoshimov", 23, "O'zbek", 6, "Erkin usul", 3)
print(swimmer.get_info())
print(swimmer.introduce())

track_athlete = TrackAthlete("Rustam", "Maqsudov", 26, "O'zbek", 4, "100m", "10.3s")
print(track_athlete.get_info())
print(track_athlete.introduce())
