from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# 测试数据库使用下面这个
# from db import Repo 
# Repo.selectshopping()
# Repo.buygoods("towel")
# Repo.selectgoods("towel")
# Repo.selectshopping()
# Repo.deleteshopping("towel")
# Repo.clean()
# Repo.delete("john")
# 测试rasa使用下面这个
from . import Repo 
# Repo.buygoods("towel")
# Repo.initDb()


# Repo.select()
class ActionAskName(Action):

    def name(self) -> Text:
        return "action_ask_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_name")

        return []


class ActionAskAddress(Action):

    def name(self) -> Text:
        return "action_ask_address"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_address")

        return []


class ActionAskEmail(Action):

    def name(self) -> Text:
        return "action_ask_phone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_phone")

        return []


class ActionSaveDetails(Action):
    #  save address
    def name(self) -> Text:
        return "action_save_customer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        Repo.insert(tracker.get_slot('Name'), tracker.get_slot('Address'), tracker.get_slot('Phone'))

        dispatcher.utter_message(response="utter_display_details")

        return []

class ActionAskGoodsName(Action):
    # query goods pre
    def name(self) -> Text:
        return "action_ask_goodsname"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_goods")

        return []
class ActionSelectSpecifyGoods(Action):
    # query goods
    def name(self) -> Text:
        return "action_select_goods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Select goods due to name
        rows = Repo.selectgoods(tracker.get_slot('GoodsName'))

        dispatcher.utter_message(text="query successfully: "+ rows)
        # dispatcher.utter_message(text="query successfully")

        return []

class ActionBuyGoodsPre(Action):
    # buy goods pre
    def name(self) -> Text:
        return "action_buypre_goods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(response="utter_ask_goodsname")

        return []

class ActionBuyGoods(Action):
    # buy goods
    def name(self) -> Text:
        # print("adasdasdads")  test
        return "action_buy_goods"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Select goods due to name
        # rows = Repo.buygoods(tracker.get_slot('GoodsNameBuy'))
        Repo.buygoods(tracker.get_slot('GoodsNameBuy'))
        # dispatcher.utter_message(text=rows)
        dispatcher.utter_message(response="utter_display_details_buy")
        # dispatcher.utter_message(text="buy successfully")
        return []
class CheckOut(Action):
    def name(self) -> Text:
        # print("adasdasdads")  test
        return "action_checkout"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Select goods due to name
        rows = Repo.count()
        row = str(rows)
        dispatcher.utter_message(text="Master, you need to pay "+ row + " dollors")
        return []
class ActionSelectAll(Action):
    # show address
    def name(self) -> Text:
        return "action_select_all"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Select all infor
        rows = Repo.select()

        dispatcher.utter_message(text=rows)

        return []

class ActionSelectShoppingAll(Action):
    # show card
    def name(self) -> Text:
        return "action_select_allshopping"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Select all infor
        rows = Repo.selectshopping()

        dispatcher.utter_message(text=rows)

        return []
class ActionDeleteAddress(Action):
    # delete address
    def name(self) -> Text:
        return "action_delete_customer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Delete infor due to name
        # value = tracker.latest_message['entities'][0]['value']

        Repo.delete(tracker.get_slot('Name'))

        dispatcher.utter_message(text="Deleted successfully address")

        return []

class ActionDeleteShopping(Action):
    # delete goods from card
    def name(self) -> Text:
        return "action_delete_shopping"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        Repo.deleteshopping(tracker.get_slot('GoodsNameBuy'))

        dispatcher.utter_message(text="Deleted successfully from shopping card")

        return []

class ActionDeleteCard(Action):
    # delete goods from card
    def name(self) -> Text:
        return "action_delete_card"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        Repo.clean()
        dispatcher.utter_message(text="Your card has been cleaned")

        return []