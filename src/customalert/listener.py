from endstone.event import event_handler, PlayerJoinEvent, PlayerQuitEvent, PlayerLoginEvent, PlayerDeathEvent, PlayerTeleportEvent
#from endstone.network import LoginPacket, ProtocolInfo

class EventListener:
  
    def __init__(self, plugin):
        self.plugin = plugin
    
    @event_handler
    def on_join(self, event: PlayerJoinEvent):
        player = event.player
        if self.plugin.is_type_hidden("join"):
            event.join_message = ""
        elif self.plugin.is_type_custom("join"):
            event.join_message = self.plugin.get_message(player, "join")
           
    @event_handler
    def on_quit(self, event: PlayerQuitEvent):
        player = event.player
        if self.plugin.is_type_hidden("quit"):
            event.quit_message = ""
        elif self.plugin.is_type_custom("quit"):
            event.quit_message = self.plugin.get_message(player, "quit")
    
    @event_handler
    def on_teleport(self, event: PlayerTeleportEvent):
        player = event.player
        to_loc = event.to_location
        from_loc = event.from_location
        if to_loc.dimension.name != from_loc.dimension.name:
            replace = {
              "FROM": from_loc.dimension.level.name,
              "TO": to_loc.dimension.level.name
            }
            if self.plugin.is_type_custom("world-change"):
                msg = self.plugin.get_message(player, "world-change", replace)
                self.plugin.server.broadcast_message(msg)
        else:
            replace = {
              "FROM": f"{int(from_loc.x)}:{int(from_loc.y)}:{int(from_loc.z)}",
              "TO": f"{int(to_loc.x)}:{int(to_loc.y)}:{int(to_loc.z)}"
            }
            if self.plugin.is_type_custom("teleport-change"):
                msg = self.plugin.get_message(player, "teleport-change", replace)
                self.plugin.server.broadcast_message(msg)
  
    @event_handler
    def on_login(self, event: PlayerLoginEvent):
        player = event.player
        total_player = len(self.plugin.server.online_players)
        max_player = self.plugin.server.max_players
        
        if total_player >= max_player:
            if self.plugin.is_type_custom("server-full"):
                event.kick_message = self.plugin.get_message(player, "server-full")
    
    @event_handler
    def on_death(self, event: PlayerDeathEvent):
        player = event.player
        source = event.damage_source
        cause = source.type.lower()
        if self.plugin.is_death_hidden(source):
            event.death_message = ""
        elif self.plugin.is_death_custom(source):
            event.death_message = self.plugin.get_death_message(player, source)
            self.plugin.server.broadcast_message(event.death_message)