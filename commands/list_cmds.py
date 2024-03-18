from commands.command import hello_command, bye_command, muoi_buon_command
from commands.crawl import crawl_bee_cost
from commands.tag import (
    petting,
    muoibuon,
    miss,
    luv,
    g9,
    lick,
    bc,
    touch_cheek,
)

# Add more commands as needed
command_dict = {
    "hello": hello_command,
    "bye": bye_command,
    "test": crawl_bee_cost,
    "muối_buồn": muoibuon,
    "miss": miss,
    "iu": luv,
    "g9": g9,
    "lick": lick,
    "bc": bc,
    "cụng_má": touch_cheek,
    "vuốt_ve": petting,
}
