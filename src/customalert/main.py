from typing import Any
from datetime import datetime

from endstone.event import ActorDamageEvent
from endstone.damage import DamageSource
from endstone import Player
from endstone.plugin import Plugin
from endstone import ColorFormat

from customalert.listener import EventListener

class CustomAlert(Plugin):
    api_version = "0.5"
    prefix = "CustomAlert"

    cfg: dict[str, Any]
    def on_enable(self) -> None:
        self.register_events(EventListener(self))
        self.logger.info("CustomAlerts has enable!")
        self.save_default_config()
        self.cfg = dict(self.config)

    def default_array(self, player: Player) -> dict:
        now = datetime.now()
        date_format = self.cfg["date-format"]
        return {
          "PLAYER": player.name,
          "MAX_PLAYER": str(self.server.max_players),
          "ONLINE_PLAYER": str(len(self.server.online_players)),
          "TIME": now.strftime(date_format)
        }
    
    def is_type_custom(self, type: str) -> bool:
        return self.cfg[type]["custom"]
    
    def is_type_hidden(self, type: str) -> bool:
        return self.cfg[type]["hiden"]
    
    def get_message(self, player: Player, type: str, args: dict[str, Any] = None) -> str:
        data = self.cfg
        for key in type.split("."):
          data = data.get(key, {})
        
        if not data or "message" not in data:
            return ""
        default_args = self.default_array(player)
        if args is not None:
           default_args.update(args)
           
        msg = data.get("message")

        for key, value in default_args.items():
            msg = msg.replace("{" + str(key) + "}", str(value))
        return msg.replace("&", "§")

    def is_death_hidden(self, event: DamageSource = None):
        if event is None:
            return self.cfg["death"]["hiden"]
            
        match str(event.type):
            case "contact": 
                return self.cfg["death"]["contact"]["hiden"]
              
            case "entity_attack":
                return self.cfg["death"]["kill"]["hiden"]
              
            case "projectile":
                return self.cfg["death"]["projectile"]["hiden"]
            
            case "fall":
                return self.cfg["death"]["fall"]["hiden"]
            
            case "suffocation":
                return self.cfg["death"]["suffocation"]["hiden"]
              
            case "fire":
                return self.cfg["death"]["fire"]["hiden"]
            
            case "firetick":
                return self.cfg["death"]["on-fire"]["hiden"]
            
            case "lava":
                return self.cfg["death"]["lava"]["hiden"]
            
            case "drowning":
                return self.cfg["death"]["drowning"]["hiden"]
            
            case "block_explosion" | "entity_explosion":
                return self.cfg["death"]["explosion"]["hiden"]
            
            case "void":
                return self.cfg["death"]["void"]["hiden"]
            
            case "magic":
                return self.cfg["death"]["magic"]["hiden"]
            
            case "suicide":
                return self.cfg["death"]["suicide"]["hiden"]
            
            case _:
                return self.cfg["death"]["hiden"]
    
    def is_death_custom(self, event: DamageSource = None):
        if event is None:
            return self.cfg["death"]["custom"]
            
        match event.type:
            case "contact":
                return self.cfg["death"]["contact"]["custom"]
              
            case "entity_attack":
                return self.cfg["death"]["kill"]["custom"]
              
            case "projectile":
                return self.cfg["death"]["projectile"]["custom"]
            
            case "fall":
                return self.cfg["death"]["fall"]["custom"]
            
            case "suffocation":
                return self.cfg["death"]["suffocation"]["custom"]
              
            case "fire":
                return self.cfg["death"]["fire"]["custom"]
            
            case "firetick":
                return self.cfg["death"]["on-fire"]["custom"]
            
            case "lava":
                return self.cfg["death"]["lava"]["custom"]
            
            case "drowning":
                return self.cfg["death"]["drowning"]["custom"]
            
            case "block_explosion" | "entity_explosion":
                return self.cfg["death"]["explosion"]["custom"]
            
            case "void":
                return self.cfg["death"]["void"]["custom"]
            
            case "magic":
                return self.cfg["death"]["magic"]["custom"]
            
            case "suicide":
                return self.cfg["death"]["suicide"]["custom"]
            
            case _:
                return self.cfg["death"]["custom"]
               
    def get_death_message(self, player: Player, event: DamageSource) -> str:
        replace = self.default_array(player)
        message = self.cfg["death"]["message"]
        if event is not None:
            source = event
            damage_type = event.type
            match str(damage_type):
                case "contact":
                    message = self.cfg["death"]["contact"]["message"]
                    if source.actor is not None:
                        replace["BLOCK"] = source.actor.name
                    else:
                        replace["BLOCK"] = "UNKNOWN"
                
                case "entity_attack":
                    message = self.cfg["death"]["kill"]["message"]
                    killer = source.damaging_actor
                    if killer is not None:
                        if isinstance(killer, Player):
                            replace["KILLER"] = killer.name
                            item_in_hand = getattr(killer.inventory, "item_in_main_hand", None) or killer.inventory.item_in_main_hand
                            replace["ITEM"] = (item_in_hand.type.replace("minecraft:", "").replace("_", "").upper()) if (item_in_hand and item_in_hand.type != "minecraft:air") else "hand"
                        else:
                            replace["KILLER"] = getattr(killer, "name", "UNKNOWN")
                            replace["ITEM"] = "hand"
                    else:
                        replace["KILLER"] = "UNKNOWN"
                        replace["ITEM"] = "UNKNOWN"
                        
                case "projectile":
                    message = self.cfg["death"]["projectile"]["message"]
                    killer = source.actor
                    if killer is not None:
                        if isinstance(killer, Player):
                      
                            replace["KILLER"] = killer.name
                            item_in_hand = killer.inventory.item_in_main_hand
                        
                            replace["BOW"] = (item_in_hand.type.replace("minecraft:", "").replace("_", "").upper()) if item_in_hand else "Bow"
                        else:
                            replace["KILLER"] = killer.name
                            replace["BOW"] = "Bow"
                    else:
                        replace["KILLER"] = "UNKNOWN"
                        replace["BOW"] = "UNKNOWN"
                  
                case "suffocation":
                    message = self.cfg["death"]["suffocation"]["message"]
                
                case "fall":
                    message = self.cfg["death"]["fall"]["message"]
                
                case "fire":
                    message = self.cfg["death"]["fire"]["message"]
                
                case "firetick":
                    message = self.cfg["death"]["on-fire"]["message"]
                
                case "lava":
                    message = self.cfg["death"]["lava"]["message"]
                    
                case "drowning":
                    message = self.cfg["death"]["drowning"]["message"]
                
                case "block_explosion" | "entity_explosion":
                    message = self.cfg["death"]["explosion"]["message"]
                    
                case "void":
                    message = self.cfg["death"]["void"]["message"]
                    
                case "magic":
                    message = self.cfg["death"]["magic"]["message"]
                
                case "suicide":
                    message = self.cfg["death"]["suicide"]["message"]
                
                case _:
                    message = self.cfg["death"]["message"]
                    
        for key, value in replace.items():
            message = message.replace("{" + str(key) + "}", str(value))
        return message.replace("&", "§")