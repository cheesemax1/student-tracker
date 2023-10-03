from App.database import db
class Lecturer():

    def init(self, upvote):
        self.upvote = upvote
        self.give_upvote(upvote)

    def init(self, downvote):
        self.downvote = downvote
        self.give_downvote(downvote)

## the upvote and downvote functions affect the student karma, wait a moment for me to make that class

         