import pygame as pg


class Timer:
    def __init__(self,
                 font_path: str = "assets/fonts/first.ttf",
                 font_size: int = 39,
                 color: tuple = (255, 255, 255)
                 ):
        pg.font.init()

        self.text_color = color
        self.font = pg.font.Font(font_path, font_size)

        self.start_time_current_segment_ticks = pg.time.get_ticks()
        self.elapsed_time_when_paused_ms = 0
        self.elapsed_time_str = "00:00"
        self.last_displayed_second = -1
        self.running = True

    def get_current_total_elapsed_ms(self) -> int:
        if self.running:
            current_segment_elapsed_ms = pg.time.get_ticks() - self.start_time_current_segment_ticks
            return self.elapsed_time_when_paused_ms + current_segment_elapsed_ms
        else:
            return self.elapsed_time_when_paused_ms

    def update(self):
        total_elapsed_ms = self.get_current_total_elapsed_ms()
        total_seconds = total_elapsed_ms // 1000

        if total_seconds != self.last_displayed_second:
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            self.elapsed_time_str = f"{minutes:02d}:{seconds:02d}"
            self.last_displayed_second = total_seconds

    def draw(self, screen: pg.Surface, position: tuple):
        text_surface = self.font.render(self.elapsed_time_str, True, self.text_color)
        screen.blit(text_surface, position)

    def reset(self):
        self.start_time_current_segment_ticks = pg.time.get_ticks()
        self.elapsed_time_when_paused_ms = 0
        self.elapsed_time_str = "00:00"
        self.last_displayed_second = -1
        self.running = True

    def pause(self):
        if self.running:
            current_ticks = pg.time.get_ticks()
            self.elapsed_time_when_paused_ms += (current_ticks - self.start_time_current_segment_ticks)
            self.running = False

    def resume(self):
        if not self.running:
            self.start_time_current_segment_ticks = pg.time.get_ticks()
            self.running = True

    def get_time_string(self) -> str:
        return self.elapsed_time_str

    def get_total_seconds(self) -> int:
        total_elapsed_ms = self.get_current_total_elapsed_ms()
        return total_elapsed_ms // 1000