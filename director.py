Class Director:
    #Director roll is to control all the actions in the game.
    
    def _init_(self, keyboard_service, video_service):
        
        self.keyboard_service = keyboard_service
        self.video_service = video_service
    
    def start_game(self, cast):
        while self._video_service.is_window_open():
            self._video_service.open_window():
            
            self._get_input(cast)
            self._do_update(cast)
            self._do_output(cast)
        
        self._video_service.close_window()
        
    #get input from the user
    def _get_input(self, cast):
        
        robot = cast.get_actor_first("robots")
        vol = self._keyboard_service.get_direction()
        robot.set_vol(vol)
    
    #get update
    def _do_update(self, cast):
        
        banner = cast.get_actor_first("banners")
        robot = cast.get_actor_first("robots")
        artifact = cast.get_actor("artifacts")
        
        #set the banner for text
        banner.set_text_banner("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        for artifact in artifacts:
            if robot.get_position() == (artifact.get_position())
            display_message = artifact.get_display_message()
            banner.set_text(display_message)
    
    #set outputs for the user............
    def _do_output(self, cast):
        self._video_service.clear_buffer()
        actor = cast.get_all_actor()
        self.video_service.draw_actor(actor)
        self._video_service.flush_buffer()
        
        
        
    

