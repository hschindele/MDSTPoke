from tensorflow import keras
from poke_env.player_configuration import PlayerConfiguration
from poke_env.server_configuration import ShowdownServerConfiguration
from greedy import Greedy
from model_player import ModelPlayer
from docs_rl import SimpleRLPlayer
import asyncio

async def main():
    modplayer  = keras.models.load_model("/Users/hschindele/Pokemon-Showdown/mdst-poke-starter-main/model_80000")
    env_player = SimpleRLPlayer(battle_format="gen8randombattle")
    player = ModelPlayer(modplayer, env_player, player_configuration=PlayerConfiguration('a very greedy bot', 'password'),
                    server_configuration=ShowdownServerConfiguration
                    )
                    
    await player.accept_challenges(None, 10)

if __name__=='__main__':
    asyncio.get_event_loop().run_until_complete(main())
