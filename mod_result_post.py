from account_helpters import BattleResultsCache
from gui import SystemMessages
from gui.SYstemMessages import SM_TYPE
import json
import copy


def post_result_to_discord(isPlayerVehicle, results):
    if isPlayerVehicle:
        modifiedResults = copy.deepcopy(results)
        json.dumps(_JSON_Encode(modifiedResults))

def _JSON_Encode(obj):
    if isinstance(obj, dict):
        newDict = {}
        for key, value in obj.iteritems():
            if isinstance(key, tuple):
                newDict[str(key)] = _JSON_Encode(value)
            else:
                newDict[key] = _JSON_Encode(value)

def __onAccountBecomePlayer():
    SystemMessages.pushMessage('Hello World', type=SM_TYPE.GameGreeting)

def init():
    g_playerEvents.onBattleResultsReceived += post_result_to_discord
    g_playerEvents.onAccountBecomePlayer += __onAccountBecomePlayer
