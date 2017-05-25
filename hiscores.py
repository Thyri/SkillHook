import requests 
import csv
from discordWebhooks import Webhook, Attachment, Field

class Player(object):
	username = ""
	total = 0
	attack = 0
	defence = 0
	strength = 0
	hitpoints = 0
	ranged = 0
	prayer = 0
	magic = 0
	cooking = 0
	woodcutting = 0
	fletching = 0
	fishing = 0
	firemaking = 0
	crafting = 0
	smithing = 0
	mining = 0
	herblore = 0
	agility = 0
	thieving = 0
	slayer = 0
	farming = 0
	runecrafting = 0
	hunter = 0
	construction = 0

	#Constructor
	def __init__(self, username, total, attack, defence, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecrafting, hunter, construction):
		self.username = username
		self.total = total
		self.attack = attack
		self.defence = defence
		self.strength = strength
		self.hitpoints = hitpoints
		self.ranged = ranged
		self.prayer = prayer
		self.magic = magic
		self.cooking = cooking
		self.woodcutting = woodcutting
		self.fletching = fletching
		self.fishing = fishing
		self.firemaking = firemaking
		self.crafting = crafting
		self.smithing = smithing
		self.mining = mining
		self.herblore = herblore
		self.agility = agility
		self.thieving = thieving
		self.slayer = slayer
		self.farming = farming
		self.runecrafting = runecrafting
		self.hunter = hunter
		self.construction = construction

	def get_total():
		return self.total

def makePlayer(username, total, attack, defence, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecrafting, hunter, construction):
	player = Player(username, total, attack, defence, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecrafting, hunter, construction)
	return player



def get_user_info(userName):
	#init skill values to 0 (will be left at 0 if Hiscore lookup fails)
	total = 0
	attack = 0
	defence = 0
	strength = 0
	hitpoints = 0
	ranged = 0
	prayer = 0
	magic = 0
	cooking = 0
	woodcutting = 0
	fletching = 0
	fishing = 0
	firemaking = 0
	crafting = 0
	smithing = 0
	mining = 0
	herblore = 0
	agility = 0
	thieving = 0
	slayer = 0
	farming = 0
	runecrafting = 0
	hunter = 0
	construction = 0

	total_index = 1
	attack_index = 4
	defence_index = 7
	strength_index = 10
	hitpoints_index = 13
	ranged_index = 16
	prayer_index = 19
	magic_index = 22
	cooking_index = 25
	woodcutting_index = 28
	fletching_index = 31
	fishing_index = 34
	firemaking_index = 37
	crafting_index = 40
	smithing_index = 43
	mining_index = 46
	herblore_index = 49
	agility_index = 52
	thieving_index = 55
	slayer_index = 58
	farming_index = 61
	runecrafting_index = 64
	hunter_index = 67
	construction_index = 70

	#create the HTTP request for player stats
	stats = requests.get("http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player=" + userName)

	results = stats.text.replace('\n', ',')

	i = 0 #start of word
	j = 0 #end of word
	l = 0 #index for lis

	stat_lst = [None] * 90 #90 is the size of a runescape hiscores lookup

	for element in results:
		if element == ',':
			stat_lst[l] = results[i:j]
			l+=1
			j += 1
			i = j
		else:
			j += 1

	username = userName
	total = stat_lst[total_index]
	attack = stat_lst[attack_index]
	defence = stat_lst[defence_index]
	strength = stat_lst[strength_index]
	hitpoints = stat_lst[hitpoints_index]
	ranged = stat_lst[ranged_index]
	prayer = stat_lst[prayer_index]
	magic = stat_lst[magic_index]
	cooking = stat_lst[cooking_index]
	woodcutting = stat_lst[woodcutting_index]
	fletching = stat_lst[fletching_index]
	fishing = stat_lst[fishing_index]
	firemaking = stat_lst[firemaking_index]
	crafting = stat_lst[crafting_index]
	smithing = stat_lst[smithing_index]
	mining = stat_lst[mining_index]
	herblore = stat_lst[herblore_index]
	agility = stat_lst[agility_index]
	thieving = stat_lst[thieving_index]
	slayer = stat_lst[slayer_index]
	farming = stat_lst[farming_index]
	runecrafting = stat_lst[runecrafting_index]
	hunter = stat_lst[hunter_index]
	construction = stat_lst[construction_index]

	return makePlayer(username, total, attack, defence, strength, hitpoints, ranged, prayer, magic, cooking, woodcutting, fletching, fishing, firemaking, crafting, smithing, mining, herblore, agility, thieving, slayer, farming, runecrafting, hunter, construction)






