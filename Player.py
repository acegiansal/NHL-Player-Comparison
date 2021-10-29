class Player:

    name: str
    age: int
    num: str
    team: str
    pos: str
    gp: int
    a: int
    p: int
    pm: int
    pim: int

    def __init__(self, name, age, num, team, pos, gp, a, p, pm, pim):
        self.name = name
        self.age = age
        self.num = num
        self.team = team
        self.pos = pos
        self.gp = gp
        self.a = a
        self.p = p
        self.pm = pm
        self.pim = pim

    def __str__(self) -> str:
        print(f"Player: {self.name}, Team: {self.team}")
