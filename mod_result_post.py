from account_helpers import BattleResultsCache
from gui import SystemMessages
from gui.SystemMessages import SM_TYPE
from PlayerEvents import g_playerEvents
import requests
import json
import copy


def post_result_to_discord(isPlayerVehicle, results):
    if isPlayerVehicle:
        modifiedResults = copy.deepcopy(results)
        json.dumps(_JSON_Encode(modifiedResults))
    else:
        pass

def _JSON_Encode(obj):
    if isinstance(obj, dict):
        newDict = {}
        for key, value in obj.iteritems():
            if isinstance(key, tuple):
                newDict[str(key)] = _JSON_Encode(value)
            else:
                newDict[key] = _JSON_Encode(value)

        return newDict
    if isinstance(obj, list) or isinstance(obj, tuple) or isinstance(obj, set):
        newList = []
        for value in obj:
            newList.append(_JSON_Encode(value))

        return newList
    return obj


def __onAccountBecomePlayer():
    SystemMessages.pushMessage('Hello World', type=SM_TYPE.GameGreeting)
    post_to_discord()


def post_to_discord():
    url = 'https://discordapp.com/api/webhooks/452188196533436418/6AE7DIRLZ9VyNJ26z1VmikajVqO7ItQbr3wOKC2bLgMb_qjCeDexlSKb8E-rbzlZjcv_'
    method = 'POST'
    obj = {"username": "bot",
              "content": "launched world of tanks."}
    headers = {"Content-Type": "application/json"}
    json_data = json.dumps(obj)

    result = requests.post(url, data=json_data, headers=headers)
    print(result.status_code)


def init():
    g_playerEvents.onBattleResultsReceived += post_result_to_discord
    g_playerEvents.onAccountBecomePlayer += __onAccountBecomePlayer
