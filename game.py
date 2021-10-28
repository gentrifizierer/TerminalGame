# This is my first completely self-written piece of code, so please be gentle on me

# player inititalization
class Player:
    def __init__(self, name, powers, inventory):
        self.name = name
        self.powers = powers
        self.inventory = inventory

    def __add__(self, item, amount):
        self.inventory[item] += amount

    def __sub__(self, item, amount):
        self.inventory[item] -= amount

player = Player(input("Hey there, how may I call you?\n"), [], {})

# interface
print("\nHey {name}, welcome to our little adventure.\nThroughout the game, you will be making decisions and the game will adapt accordingly.\nHere is an example:\n".format(name = player.name))

# first user input test
test = input("Dogs or cats?\n")
dogs = "dogs"
cats = "cats"
if (dogs or dogs.upper() or dogs.title()) in test:
    print("""
                                ..,,,,,,,,,..
                     .,;%%%%%%%%%%%%%%%%%%%%;,.
                   %%%%%%%%%%%%%%%%%%%%////%%%%%%, .,;%%;,
            .,;%/,%%%%%/////%%%%%%%%%%%%%%////%%%%,%%//%%%,
        .,;%%%%/,%%%///%%%%%%%%%%%%%%%%%%%%%%%%%%%%,////%%%%;,
     .,%%%%%%//,%%%%%%%%%%%%%%%%@@%a%%%%%%%%%%%%%%%%,%%/%%%%%%%;,
   .,%//%%%%//,%%%%///////%%%%%%%@@@%%%%%%///////%%%%,%%//%%%%%%%%,
 ,%%%%%///%%//,%%//%%%%%///%%%%%@@@%%%%%////%%%%%%%%%,/%%%%%%%%%%%%%
.%%%%%%%%%////,%%%%%%%//%///%%%%@@@@%%%////%%/////%%%,/;%%%%%%%%/%%%
%/%%%%%%%/////,%%%%///%%////%%%@@@@@%%%///%%/%%%%%//%,////%%%%//%%%'
%//%%%%%//////,%/%a`  'a%///%%%@@@@@@%%////a`  'a%%%%,//%///%/%%%%%
%///%%%%%%///,%%%%@@aa@@%//%%%@@@@S@@@%%///@@aa@@%%%%%,/%////%%%%%
%%//%%%%%%%//,%%%%%///////%%%@S@@@@SS@@@%%/////%%%%%%%,%////%%%%%'
%%//%%%%%%%//,%%%%/////%%@%@SS@@@@@@@S@@@@%%%%/////%%%,////%%%%%'
`%/%%%%//%%//,%%%///%%%%@@@S@@@@@@@@@@@@@@@S%%%%////%%,///%%%%%'
  %%%%//%%%%/,%%%%%%%%@@@@@@@@@@@@@@@@@@@@@SS@%%%%%%%%,//%%%%%'
  `%%%//%%%%/,%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@S@@%%%%%,/////%%'
   `%%%//%%%/,%%%@@@SS@@SSs@@@@@@@@@@@@@sSS@@@@@@%%%,//%%//%'
    `%%%%%%/  %%S@@SS@@@@@Ss` .,,.    'sS@@@S@@@@%'  ///%/%'
      `%%%/    %SS@@@@SSS@@S.         .S@@SSS@@@@'    //%%'
               /`S@@@@@@SSSSSs,     ,sSSSSS@@@@@'
             %%//`@@@@@@@@@@@@@Ss,sS@@@@@@@@@@@'/
           %%%%@@00`@@@@@@@@@@@@@'@@@@@@@@@@@'//%%
       %%%%%%a%@@@@000aaaaaaaaa00a00aaaaaaa00%@%%%%%
    %%%%%%a%%@@@@@@@@@@000000000000000000@@@%@@%%%@%%%
 %%%%%%a%%@@@%@@@@@@@@@@@00000000000000@@@@@@@@@%@@%%@%%
%%%aa%@@@@@@@@@@@@@@0000000000000000000000@@@@@@@@%@@@%%%%
%%@@@@@@@@@@@@@@@00000000000000000000000000000@@@@@@@@@%%%%%

                            WOOF!

    """)
elif (cats or cats.upper() or cats.title()) in test:
    print("""
    		M.					   .:M
		MMMM.					.:MMMM
		MMMMMMMM			     .:MMMMMMM
		:MMHHHMMMMHMM.	.:MMMMMMMMM:.	   .:MMHHMHMM:
		 :MMHHIIIHMMMM.:MMHHHHIIIHHMMMM. .:MMHIHIIHHM:
		  MMMHIIIIHHMMMIIHHMHHIIIIIHHMMMMMMHHHIIIIHHM:
		  :MMHIIIIIHMMMMMMMHHIIIIIIHHHMMMMMHHII:::IHM.
		   MH:I:::IHHMMMMMHHII:::IIHHMMMHHHMMM:I:IHMM
		   :MHI:HHIHMMHHIIHII::.::IIHMMHHIHHMMM::HMM:
		    MI::HHMMIIM:IIHII::..::HM:MHHII:::IHHMM:
		    MMMHII::..:::IHMMHHHMHHMMI:::...::IHM:
		    :MHHI::....::::HMMMMMMHHI::.. ..:::HM:
		     :MI:.:MH:.....:HMMMMHHMIHMMHHI:HH.:M
		     M:.I..MHHHHHMMMIHMMMMHMMHHHHHMMH:.:M.
		     M:.H..H  I:HM:MHMHI:IM:I:MM::  MMM:M:
		     :M:HM:.M I:MHMIIMMIIHM I:MM::.:MMI:M.
		     'M::MM:IMH:MMII MMHIMHI :M::IIHMM:MM
		      MH:HMMHIHMMMMMMHMMIMHIIHHHHIMMHHMM
		       MI:MMMMHI:::::IMM:MHI:::IMMMMHIM
			:IMHIHMMMMMM:MMMMMHHHHMMMHI:M
			 HI:IMIHMMMM:MMMMMMHHHMI:.:M	  .....
	     ............M::..:HMMMMIMHIIHMMMMHII:M:::''''
		 ....:::MHI:.:HMMMMMMMMHHHMHHI::M:::::::''''''
		''   ...:MHI:.::MMHHHMHMIHMMMMHH.MI..........
		   ''  ...MHI::.::MHHHHIHHMM:::IHM           '''
		      '  IMH.::..::HMMHMMMH::..:HM:
			:M:.H.IHMIIII::IIMHMMM:H.MH
			 IMMMH:HI:MMIMI:IHI:HIMIHM:
		       .MMI:.HIHMIMI:IHIHMMHIHI:MIM.
		      .MHI:::HHIIIIIHHI:IIII::::M:IM.
		     .MMHII:::IHIII::::::IIIIIIHMHIIM
		     MHHHI::.:IHHII:::.:::IIIIHMHIIHM:
		    MHHHII::..::MII::.. ..:IIIHHHII:IM.
		   .MHHII::....:MHII::.  .:IHHHI::IIHMM.
		   MMHHII::.....:IHMI:. ..:IHII::..:HHMM
		   MHHII:::......:IIHI...:IHI::.....::HM:
		  :MMH:::........ ...::..::....  ...:IHMM
		  IMHIII:::..........	  .........::IHMM.
		  :MHIII::::......	    .......::IHMM:
		   MHHIII::::...	     ......::IHMM:
		   IMHHIII:::...	     .....::IIHMM,
		   :MHHIII:::I:::...	 ....:::I:::IIHMM
		    MMHHIII::IHI:::...........:::IIH:IHMM
		    :MMHHII:IIHHI::::::.....:::::IH:IHMIM
		     MMMHHII:IIHHI:::::::::::::IHI:IIHM:M.
		     MMMHHIII::IHHII:::::::::IHI:IIIHMM:M:
		     :MMHHHIII::IIIHHII::::IHI..IIIHHM:MHM
		     :MMMHHII:..:::IHHMMHHHHI:IIIIHHMM:MIM
		     .MMMMHHII::.:IHHMM:::IIIIIIHHHMM:MI.M
		   .MMMMHHII::.:IHHMM:::IIIIIIHHHMM:MI.M
		 .MMMMHHMHHII:::IHHMM:::IIIIIHHHHMM:MI.IM.
		.MMHMMMHHHII::::IHHMM::I&&&IHHHHMM:MMH::IM.
	       .MMHHMHMHHII:::.::IHMM::IIIIHHHMMMM:MMH::IHM
	       :MHIIIHMMHHHII:::IIHMM::IIIHHMMMMM::MMMMHHHMM.
	       MMHI:IIHMMHHHI::::IHMM:IIIIHHHMMMM:MMMHI::IHMM.
	       MMH:::IHMMHHHHI:::IHMM:IIIHHHHMMMM:MMHI:.:IHHMM.
	       :MHI:::IHMHMHHII::IHMM:IIIHHHMMMMM:MHH::.::IHHM:
	       'MHHI::IHMMHMHHII:IHMM:IIHHHHMMMM:MMHI:...:IHHMM.
		:MHII:IIHMHIHHIIIIHMM:IIHHHHMMMM:MHHI:...:IIHMM:
		'MHIII:IHHMIHHHIIHHHMM:IHHHMMMMM:MHHI:..::IIHHM:
		 :MHHIIIHHMIIHHHIHHHMM:HHHHMMMMM:MHII::::IIIHHMM
		  MHHIIIIHMMIHHHIIHHMM:HHHHMMMM:MMHHIIHIIIIIHHMM.
		  'MHHIIIHHMIIHHIIIHMM:HHHMMMMH:MHHMHII:IIIHHHMM:
		   'MHHIIIHMMIHHHIHHMM:HHHMMMHH:MMIMMMHHHIIIHHMM:
		    'MHHIIHHMIHHHHHMMM:HHHMMMH:MIMMMMMMMMMMHIHHM:
		     'MHIIIHMMIHHHHHMM:HHHMMMH:IMMMMMHHIHHHMMHHM'
		      :MHHIIHMIHHHHHMM:HHHMMMM:MMHMMHIHMHI:IHHHM
		       MHHIIHM:HHHHHMM:HHHMMMM:MMMHIHHIHMM:HHIHM
			MHHIHM:IHHHHMM:HHHHMM:MMHMIIHMIMMMHMHIM:
			:MHIHMH:HHHHMM:HHHHMM:MMHIIHMIIHHMMHIHM:
			 MMHHMH:HHHHMM:HHHHMM:MHHIHMMIIIMMMIIHM'
			 'MMMMH:HHHHMM:HHHMM:MHHHIMMHIIII::IHM:
			  :MMHM:HHHHMM:HHHMM:MHIHIMMHHIIIIIHM:
			   MMMM:HHHHMM:HHHHM:MHHMIMMMHHHIHHM:MMMM.
			   :MMM:IHHHMM:HHHMM:MHHMIIMMMHHMM:MMMMMMM:
			   :MMM:IHHHM:HHHHMM:MMHHHIHHMMM:MMMMMMMMMM
			    MHM:IHHHM:HHHMMM:MMHHHHIIIMMIIMMMMMMMMM
			    MHM:HHHHM:HHHMMM:HMMHHHHHHHHHMMMMMMMMM:
			 .MI:MM:MHHMM:MHMMHMHHMMMMHHHHHHHMMMMMMMMM'
			:IM:MMIM:M:MM:MH:MM:MH:MMMMMHHHHHMMMMMMMM'
			:IM:M:IM:M:HM:IMIHM:IMI:MMMMMHHHMMMMMM:'
			 'M:MHM:HM:MN:HMIHM::M'   '::MMMMMMM:'
			    'M'HMM'M''M''HM'I'

                                    MEOW!

    """)
