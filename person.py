SAME_YEAR_IDX = 5


# TODO: print out emails and message next to name for easier copy pasting

class Person:

    def __init__(self, info):
        self.info = info
        self.scores = {}

    def find_matches(self, people):
        same_year = self.info[SAME_YEAR_IDX] == "Yes"

        for person in people:
            self.scores[person.info[0]] = 0
            if same_year:
                if person.info[1] != self.info[1] and person.info[2] != self.info[2] and person.info[4] == self.info[4]:
                    for idx in range(len(self.info)):
                        if person.info[idx] == self.info[idx] and idx != SAME_YEAR_IDX:
                            self.scores[person.info[0]] += 1
            else:
                if person.info[1] != self.info[1] and person.info[2] != self.info[2]:
                    for idx in range(len(self.info)):
                        if person.info[idx] == self.info[idx] and idx != SAME_YEAR_IDX:
                            self.scores[person.info[0]] += 1

    def print_scores(self):
        self.sort_scores()
        count = 0
        for key, value in self.scores.items():
            print(key, value)
            count += 1
            if count == 5:
                break

    def sort_scores(self):
        self.scores = dict(sorted(self.scores.items(), key=lambda item: item[1], reverse=True))
