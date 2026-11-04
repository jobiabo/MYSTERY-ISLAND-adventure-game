PLAYER_STATE = {
    "player_name": "",
    "health": 5,
    "has_map": False,
    "current_location": "beach",
    "puzzle_solved": False,
    "has_rope": False,
    "has_lantern": False,
    "score": 0
}

MAIN_MENU ="""
    ################################################
    #                                              #
    #          MYSTERY ISLAND ADVENTURE            #
    #                                              #
    #              THE LOST TRAVELLER              #
    #                                              #
    ################################################

                  [  PRESS ENTER  ]

             >>> YOUR ADVENTURE BEGINS <<<
    """


START_MESSAGE = """Welcome, brave traveller!

Are you ready to test your courage, intelligence and survival instincts? Welcome to Mystery Island, an adventure where every decision matters, every clue hides a secret, and one wrong move could cost you everything.

Your journey begins after a terrible storm leaves you stranded on a mysterious island, far away from civilisation. With no one around to help, you must explore the unknown, solve puzzles, overcome dangerous obstacles and find a way to escape.

But be warned: the island is not as empty as it seems. Hidden dangers lurk in the jungle, ancient secrets lie beneath its surface, and survival depends entirely on the choices you make.

Your mission is simple: SURVIVE, EXPLORE AND ESCAPE!

Keep an eye on your energy and health.
Collect useful items along your journey.
Solve scrambled-word challenges to overcome obstacles.
Make wise decisions because every choice has consequences.
Do you have what it takes to escape Mystery Island?"""

GAME_INTRO = """STORY MODE: THE BEGINNING
Chapter 1: The Awakening
Crash!

The sound of waves crashing against the shore slowly brings you back to consciousness.

You open your eyes and find yourself lying on a deserted beach. Your clothes are soaked, your body is exhausted, and pieces of broken wood are scattered across the sand.

You struggle to remember what happened.

The last thing you recall is being aboard a ship when a violent storm suddenly struck. The waves grew stronger, the ship began to break apart, and everything went dark.

Now, you are alone.

As you slowly get to your feet, you notice something unusual nearby. Partially buried beneath the wet sand is an old piece of parchment.

You move closer, pick it up and carefully unfold it.

It's a map!

Although some of its markings have faded, it appears to show several locations across the island, including a dense jungle, an ancient bridge and an abandoned lighthouse.

Perhaps this map is your only chance of finding a way off the island.

Your first challenge: Save the map!
A sudden wave approaches, and the parchment is about to be washed away.

You must act quickly!

Will you reach the map in time, risk slipping on the wet sand, or manage to secure it safely?

Your adventure begins now. Good luck, traveller!"""


THE_LOST_MAP = """THE FADING MAP: A RACE AGAINST THE TIDE!
As you reach for the old parchment, a sudden wave rushes towards the shore!

The map is lying dangerously close to the water. You have only a few moments to save it before the ocean swallows its secrets.

What will you do, traveller?

Three choices lie before you. Choose wisely, because your decision will determine your fate!

1. Drowned Secrets: Let the waters decide.
2. Treacherous Steps: Trust the uncertain ground.
3. Sealed Fortune: Seize what the storm left behind.
Make your choice and let fate decide your next move!"""

PHASE_JUNGLE = """🌴 PHASE II: THE HEART OF THE JUNGLE
Chapter 2: Into the Unknown
Congratulations, traveller! You have secured the mysterious map!

With the map safely in your possession, you finally have a sense of direction. You carefully examine its faded markings and discover a route leading away from the beach and deep into the island's dense jungle.

You gather your strength and begin your journey.

As you approach the jungle, towering trees surround you, their branches blocking out most of the sunlight. Strange sounds echo through the wilderness. Birds scatter overhead, leaves rustle mysteriously, and unfamiliar creatures seem to be watching your every move.

The deeper you venture, the narrower the pathway becomes.

After walking for some time, you arrive at a junction where the path splits into two directions: LEFT and RIGHT.

You pause and examine both routes.

The left path appears quiet, but something about the ground seems unusual. The right path disappears into thick vegetation, where strange noises emerge from the shadows.

Your map offers no clear explanation of what lies ahead.

Remember, traveller: the jungle holds many secrets, but not every path leads to safety. Your next decision could determine whether you survive or become another forgotten mystery of the island.

YOUR NEXT CHALLENGE: CHOOSE YOUR PATH!
Two directions. Two different dangers. One chance to move forward.

LEFT: The Hollow's Embrace : A silent path conceals a potentially deadly secret.
RIGHT: The Predator's Trial: Something dangerous may be waiting among the shadows.
Choose wisely. Your survival depends on it.

The jungle awaits..."""




HOLLOW_EMBRACE = """💀 THE HOLLOW'S EMBRACE – FATAL MISTAKE!

You take the left path, hoping to find a safer route through the jungle.

Suddenly, the ground beneath your feet collapses!

CRACK!

You fall into a deep, hidden ditch and cannot escape.

Your journey ends here.

YOU FAILED!

⚠️ SURVIVAL FEEDBACK

Not every quiet path is safe, traveller. Always observe your surroundings before making decisions.

Lesson learned: Never mistake silence for safety!"""


PREDATOR_WELCOME = """THE PREDATOR'S TRIAL: FACE THE BEAST!
                    Congratulations, traveller! You have chosen the right path and ventured deeper into the jungle.
                    
                    Suddenly, bushes begin to shake, and a terrifying roar echoes through the trees!
                    
                    A fierce beast emerges from the shadows, blocking your way. Before you can escape, it launches an attack!
                    
                    But there is hope. You notice that the beast's movements follow certain patterns.
                    
                    ⚔️ YOUR CHALLENGE: SURVIVE THE ATTACK!
                    The beast will strike, and you must prove your quick thinking and survival instincts.
                    
                    Instructions:
                    
                    Scrambled words will appear on your screen.
                    Rearrange the letters to form the correct survival or combat action.
                    Enter the correct word to dodge or counter the beast's attack.
                    Incorrect answers will cost you energy.
                    Survive the encounter and defeat the beast to earn a rope as your reward!
                    Remember, traveller: Think fast, act wisely and fight for your survival!
                    
                    The predator is watching. Are you ready?"""

OLD_BRIDGE_WELCOME = """🌉 PHASE III: THE ANCIENT BRIDGE Chapter 3: The Forgotten Crossing

                        Congratulations, traveller! You have defeated the beast and secured the rope!
                        
                        Following the route marked on your map, you venture deeper into the island until you encounter an enormous ancient bridge.
                        
                        The bridge looks extremely old, with broken wooden planks and a rusted mechanical wheel. It appears to have been abandoned for millions of years.
                        
                        There is no other way across.
                        
                        As you examine the bridge, you notice that its mechanism is still connected to a large wheel. Your rope might be the only thing capable of bringing it back to life.
                        
                        YOUR NEXT CHALLENGE: RESTORE THE BRIDGE!
                        
                        You must use your rope to secure the wheel and operate the ancient mechanism.
                        
                        Instructions:
                        
                        Three scrambled words will appear on your screen.
                        Rearrange the letters to form the correct words.
                        Each correct answer helps you operate the bridge mechanism.
                        Solve all three challenges to lower the bridge and continue your journey.
                        
                        Be careful, traveller! One wrong move could leave you stranded.
                        
                        The ancient bridge awaits. Are you ready to cross?"""

BRIDGE_SUCCESS = """🎉 THE ANCIENT BRIDGE – SUCCESSFUL CROSSING!

                    Excellent work, traveller!

                    You successfully secured the rope and operated the ancient mechanism.

                    With a loud creaking sound, the rusted wheel begins to turn, and the ancient bridge slowly lowers into position.

                    At last, the path across is clear!

                    You carefully cross the bridge and continue your journey deeper into the mysterious island.

                    🏆 CHALLENGE COMPLETED!

                    ⚠️ SURVIVAL FEEDBACK

                    Well done! Your patience and problem-solving skills have helped you overcome another obstacle.

                    Remember, traveller: Sometimes survival requires more than strength; it requires intelligence and resourcefulness.

                    Your adventure continues..."""

LIGHT_HOUSE_WELCOME = """🏚️ PHASE IV: THE ABANDONED LIGHTHOUSE Chapter 4: The Key to Survival

                        Congratulations, traveller! You have successfully crossed the ancient bridge!
                        
                        Following the markings on your map, you continue exploring the island until you discover an old lighthouse standing near the rocky coastline.
                        
                        It looks abandoned, with broken windows, rusty walls and overgrown grass surrounding its entrance.
                        
                        As you approach, something catches your attention. Half-hidden in the grass is an old, rusted key.
                        
                        Could this be the key to unlocking the lighthouse?
                        
                        You carefully examine your surroundings, but the island has taught you that danger can hide in unexpected places.
                        
                        YOUR NEXT CHALLENGE: FIND THE KEY!
                        
                        You must make the right decision to retrieve and keep the mysterious key.
                        
                        Three choices lie ahead, but not all of them will lead to success.
                        
                        Remember, traveller: Every decision matters, and one careless move could end your journey.
                        
                        The lighthouse holds the secret to your escape. Are you ready to discover it?"""

FIND_KEY_PUZZLE = """🔑 THE FORGOTTEN KEY – A TEST OF SURVIVAL!

As you approach the abandoned lighthouse, something shiny catches your attention in the overgrown grass.

You move closer and discover an old, rusted key lying on the ground.

It might be the key to unlocking the lighthouse door!

However, something feels unusual about the area. The grass is thick, and you cannot clearly see what might be hiding beneath it.

You must decide how to retrieve the key.

YOUR CHALLENGE: CHOOSE WISELY!

1. The Silent Guardian 
2. The Brittle Relic 
3. The Keeper's Fortune

Choose wisely, traveller. Your next decision could determine your fate!"""

FIND_KEY_SUCCESS = """🔑 THE KEEPER'S FORTUNE – KEY SECURED!

                        Excellent work, traveller!
                        
                        You carefully inspect the grass and successfully retrieve the old rusted key without disturbing anything dangerous.
                        
                        You now have the key that could unlock the abandoned lighthouse.
                        
                        With hope renewed, you approach the massive lighthouse door, ready to discover what lies beyond.
                        
                        🏆 CHALLENGE COMPLETED!
                        
                        Your journey continues..."""