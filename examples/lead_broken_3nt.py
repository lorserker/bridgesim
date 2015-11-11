from redeal import *

predeal = {'S': H('T98 KJ84 KJ2 865')}



def accept(deal):
    if not semibalanced(deal.east):
        return False
    if not semibalanced(deal.west):
        return False
    if len(deal.east.spades) != 5:
        return False
    if len(deal.east.hearts) >= 4:
        return False
    if len(deal.west.diamonds) < 4:
        return False
    if len(deal.west.clubs) > len(deal.west.diamonds) or len(deal.west.hearts) > len(deal.west.diamonds):
        return False
    if deal.west.hcp < 12 or deal.west.hcp > 14:
        return False
    if deal.east.hcp < 11 or deal.east.hcp > 15:
        return False

    return True


simulation = OpeningLeadSim(accept, "3NE", matchpoints)

