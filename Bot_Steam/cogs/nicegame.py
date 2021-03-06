import discord
import random 
from discord.ext import commands


class User(commands.Cog):

	def _int_(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		print("Nicegame has loaded...") #Displaying text that means the command is working

	@commands.command()
	async def nice_game (self, ctx ):
		game = ['https://store.steampowered.com/app/298630/The_Escapists/', 
				'https://store.steampowered.com/app/641990/The_Escapists_2/', 
				'https://store.steampowered.com/app/1016120/PGA_TOUR_2K21/', 
				'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/', 
				'https://store.steampowered.com/app/12120/Grand_Theft_Auto_San_Andreas/',
				'https://store.steampowered.com/app/12110/Grand_Theft_Auto_Vice_City/',
				'https://store.steampowered.com/app/12100/Grand_Theft_Auto_III/',
				'https://store.steampowered.com/app/12180/Grand_Theft_Auto_2/',
				'https://store.steampowered.com/app/12170/Grand_Theft_Auto/',
				'https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/',
				'https://store.steampowered.com/app/1250410/Microsoft_Flight_Simulator/',
				'https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/',
				'https://store.steampowered.com/app/617290/Remnant_From_the_Ashes/',
				'https://store.steampowered.com/app/440/Team_Fortress_2/',
				'https://store.steampowered.com/app/39210/FINAL_FANTASY_XIV_Online/',
				'https://store.steampowered.com/app/252490/Rust/',
				'https://store.steampowered.com/app/1089350/NBA_2K20/',
				'https://store.steampowered.com/app/227300/Euro_Truck_Simulator_2/',
				'https://store.steampowered.com/app/1151640/Horizon_Zero_Dawn_Complete_Edition/',
				'https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/',
				'https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/',
				'https://store.steampowered.com/app/236390/War_Thunder/',
				'https://store.steampowered.com/app/976730/Halo_The_Master_Chief_Collection/',
				'https://store.steampowered.com/app/1222680/Need_for_Speed_Heat/',
				'https://store.steampowered.com/app/346110/ARK_Survival_Evolved/',
				'https://store.steampowered.com/app/1190460/DEATH_STRANDING/',
				'https://store.steampowered.com/app/648800/Raft/',
				'https://store.steampowered.com/app/1222670/The_Sims_4/',
				'https://store.steampowered.com/app/1080110/F1_2020/',
				'https://store.steampowered.com/app/620980/Beat_Saber/',
				'https://store.steampowered.com/app/489830/The_Elder_Scrolls_V_Skyrim_Special_Edition/',
				'https://store.steampowered.com/app/242760/The_Forest/',
				'https://store.steampowered.com/app/270880/American_Truck_Simulator/',
				'https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/',
				'https://store.steampowered.com/app/546560/HalfLife_Alyx/',
				'https://store.steampowered.com/app/253960/Jack_Orlando_Directors_Cut/',
				'https://store.steampowered.com/app/434170/The_Jackbox_Party_Pack_3/',
				'https://store.steampowered.com/app/610180/The_Jackbox_Party_Pack_4/',
				'https://store.steampowered.com/app/703080/Planet_Zoo/',
				'https://store.steampowered.com/app/292030/The_Witcher_3_Wild_Hunt/',
				'https://store.steampowered.com/app/208650/Batman_Arkham_Knight/',
				'https://store.steampowered.com/app/105600/Terraria/',
				'https://store.steampowered.com/app/397540/Borderlands_3/',
				'https://store.steampowered.com/app/782330/DOOM_Eternal/',
				'https://store.steampowered.com/app/812140/Assassins_Creed_Odyssey/',
				'https://store.steampowered.com/app/787860/Farming_Simulator_19/',
				'https://store.steampowered.com/app/377160/Fallout_4/',
				'https://store.steampowered.com/app/322330/Dont_Starve_Together/',
				'https://store.steampowered.com/app/311210/Call_of_Duty_Black_Ops_III/',
				'https://store.steampowered.com/app/107410/Arma_3/',
				'https://store.steampowered.com/app/251570/7_Days_to_Die/',
				'https://store.steampowered.com/app/218620/PAYDAY_2/',
				'https://store.steampowered.com/app/1222140/Detroit_Become_Human/',
				'https://store.steampowered.com/app/803330/Destroy_All_Humans/',
				'https://store.steampowered.com/app/4000/Garrys_Mod/',
				'https://store.steampowered.com/app/220/HalfLife_2/',
				'https://store.steampowered.com/app/70/HalfLife/',
				'https://store.steampowered.com/app/380/HalfLife_2_Episode_One/',
				'https://store.steampowered.com/app/420/HalfLife_2_Episode_Two/',
				'https://store.steampowered.com/app/320/HalfLife_2_Deathmatch/',
				'https://store.steampowered.com/app/264710/Subnautica/',
				'https://store.steampowered.com/app/1091500/Cyberpunk_2077/',
				'https://store.steampowered.com/app/732690/FIVE_NIGHTS_AT_FREDDYS_HELP_WANTED/',
				'https://store.steampowered.com/app/506610/Five_Nights_at_Freddys_Sister_Location/',
				'https://store.steampowered.com/app/871720/Ultimate_Custom_Night/',
				'https://store.steampowered.com/app/722960/CASE_2_Animatronics_Survival/',
				'https://store.steampowered.com/app/489360/CASE_Animatronics/',
				'https://store.steampowered.com/app/412020/Metro_Exodus/',
				'https://store.steampowered.com/app/418370/Resident_Evil_7_Biohazard/',
				'https://store.steampowered.com/app/414700/Outlast_2/',
				'https://store.steampowered.com/app/883710/Resident_Evil_2/',
				'https://store.steampowered.com/app/214490/Alien_Isolation/',
				'https://store.steampowered.com/app/240720/Getting_Over_It_with_Bennett_Foddy/',
				'https://store.steampowered.com/app/480490/Prey/',
				'https://store.steampowered.com/app/572430/Party_Hard_2/',
				'https://store.steampowered.com/app/356570/Party_Hard/',
				'https://store.steampowered.com/app/1029090/Party_Hard_2_DLC_Alien_Butt_Form/',
				'https://store.steampowered.com/app/47890/The_Sims_3/',
				'https://store.steampowered.com/app/1172380/_/?curator_clanid=36135791'
				'https://store.steampowered.com/app/1262540/Need_for_Speed/?curator_clanid=36135791',
				'https://store.steampowered.com/app/1262560/Need_for_Speed_Most_Wanted/?curator_clanid=36135791',
				'https://store.steampowered.com/app/47920/Shift_2_Unleashed/?curator_clanid=36135791',
				'https://store.steampowered.com/app/1237970/Titanfall_2/?curator_clanid=36135791',
				'https://store.steampowered.com/app/1238840/Battlefield_1/?curator_clanid=36135791',
				'https://store.steampowered.com/app/1222700/A_Way_Out/?curator_clanid=36135791',
				'https://store.steampowered.com/app/1238060/Dead_Space_3/?curator_clanid=36135791',
				'https://store.steampowered.com/app/24780/SimCity_4_Deluxe_Edition/?curator_clanid=36135791',
				'https://store.steampowered.com/app/24720/SPORE_Galactic_Adventures/?curator_clanid=36135791',
				'https://store.steampowered.com/app/3590/Plants_vs_Zombies_GOTY_Edition/?curator_clanid=36135791',
				'https://store.steampowered.com/app/17410/Mirrors_Edge/?curator_clanid=36135791',
				'https://store.steampowered.com/app/17440/SPORE_Creepy__Cute_Parts_Pack/?curator_clanid=36135791',
				'https://store.steampowered.com/app/17390/SPORE/?curator_clanid=36135791',
				'https://store.steampowered.com/app/17300/Crysis/?curator_clanid=36135791',
				'https://store.steampowered.com/app/17330/Crysis_Warhead/?curator_clanid=36135791',
				'https://store.steampowered.com/app/332800/Five_Nights_at_Freddys_2/',
				'https://store.steampowered.com/app/388090/Five_Nights_at_Freddys_4/',
				'https://store.steampowered.com/app/354140/Five_Nights_at_Freddys_3/',
				'https://store.steampowered.com/app/952060/Resident_Evil_3/?curator_clanid=33273264',
				'https://store.steampowered.com/app/310950/Street_Fighter_V/?curator_clanid=33273264',
				'https://store.steampowered.com/app/601150/Devil_May_Cry_5/?curator_clanid=33273264',
				'https://store.steampowered.com/app/999020/Mega_Man_ZeroZX_Legacy_Collection/?curator_clanid=33273264',
				'https://store.steampowered.com/app/738060/Freddy_Fazbears_Pizzeria_Simulator/',
				'https://store.steampowered.com/app/8500/EVE_Online/',
				'https://store.steampowered.com/app/493340/Planet_Coaster/',
				'https://store.steampowered.com/app/621060/PC_Building_Simulator/',
				'https://store.steampowered.com/app/1214420/Tom_Clancys_Rainbow_Six_Siege__Year_5_Pass/',
				'https://store.steampowered.com/app/555160/Pavlov_VR/',
				'https://store.steampowered.com/app/1238860/Battlefield_4/',
				'https://store.steampowered.com/app/457140/Oxygen_Not_Included/',
				'https://store.steampowered.com/app/1225330/NBA_2K21/',
				'Halo_The_Master_Chief_Collectiontps://store.steampowered.com/app/269950/XPlane_11/',
				'https://store.steampowered.com/app/883710/Resident_Evil_2/',
				'https://store.steampowered.com/app/938560/INMOST/',
				'https://store.steampowered.com/app/221100/DayZ/',
				'https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/',
				'https://store.steampowered.com/app/332950/Dark_Deception/',
				'https://store.steampowered.com/app/57300/Amnesia_The_Dark_Descent/',
				'https://store.steampowered.com/app/319510/Five_Nights_at_Freddys/',
				'https://store.steampowered.com/app/209000/Batman_Arkham_Origins/',
				'https://store.steampowered.com/app/379720/DOOM/?snr=1_7_7_230_150_7',
				'https://store.steampowered.com/app/447040/Watch_Dogs_2/',
				'https://store.steampowered.com/app/939960/Far_Cry_New_Dawn/?snr=1_7_7_230_150_8',
				'https://store.steampowered.com/app/307780/Mortal_Kombat_X/?snr=1_7_7_151_150_1',
				'https://store.steampowered.com/app/550/Left_4_Dead_2/',
				'https://store.steampowered.com/app/500/Left_4_Dead/',
				'https://store.steampowered.com/app/294100/RimWorld/',
				'https://store.steampowered.com/app/49520/Borderlands_2/?snr=1_7_7_151_150_1',
				'https://store.steampowered.com/app/221040/Resident_Evil_6/',
				'https://store.steampowered.com/app/400/Portal/',
				'https://store.steampowered.com/app/620/Portal_2/',
				'https://store.steampowered.com/app/240/CounterStrike_Source/?snr=1_7_7_151_150_1',
				'https://store.steampowered.com/app/10/CounterStrike/',
				'https://store.steampowered.com/app/80/CounterStrike_Condition_Zero/',
				'https://store.steampowered.com/app/230410/Warframe/?snr=1_7_7_230_150_1',
				'https://store.steampowered.com/app/239140/Dying_Light/',
				'https://store.steampowered.com/app/496640/Strange_Night/',
				'https://store.steampowered.com/app/220240/Far_Cry_3/',
				'https://store.steampowered.com/app/298110/Far_Cry_4/',
				'https://store.steampowered.com/app/1013310/Peaky_Blinders_Mastermind/',
				'https://store.steampowered.com/app/19900/Far_Cry_2_Fortunes_Edition/',
				'https://store.steampowered.com/app/1172620/Sea_of_Thieves/',
				'https://store.steampowered.com/bundle/15308/Dead_by_Daylight__Silent_Hill_Edition/',
				'https://store.steampowered.com/app/46370/Rig_n_Roll/?l=russian',
				'https://store.steampowered.com/app/945360/Among_Us/',
				'https://store.steampowered.com/app/632360/Risk_of_Rain_2/',
				'https://store.steampowered.com/app/342180/Arizona_Sunshine/',
				'https://store.steampowered.com/app/21130/LEGO_Harry_Potter_Years_14/',
				'https://store.steampowered.com/app/204120/LEGO_Harry_Potter_Years_57/',
				'https://store.steampowered.com/app/243470/Watch_Dogs/',
				'https://store.steampowered.com/app/281990/Stellaris/',
				'https://store.steampowered.com/app/1085660/Destiny_2/',
				'https://store.steampowered.com/bundle/10410/Mortal_Kombat_11_and_X_Bundle/',
				'https://store.steampowered.com/app/627270/Injustice_2/',
				'https://store.steampowered.com/app/242700/Injustice_Gods_Among_Us_Ultimate_Edition/',
				'https://store.steampowered.com/app/389730/TEKKEN_7/',
				'https://store.steampowered.com/app/460930/Tom_Clancys_Ghost_Recon_Wildlands/',
				'https://store.steampowered.com/app/728880/Overcooked_2/',
				'https://store.steampowered.com/app/448510/Overcooked/',
				'https://store.steampowered.com/app/221910/The_Stanley_Parable/?l=russian',
				]
		nicegame = random.choice(game)	
		await ctx.send(  "Your game: " f" { nicegame }"    )
		print("Your game - ", (nicegame))

def setup(client):
	client.add_cog(User(client))