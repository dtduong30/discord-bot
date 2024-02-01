from commands.command import hello_command, bye_command, muoi_buon_command
from commands.crawl import crawl_bee_cost
from commands.tag import muoibuon, miss_duong, miss_pam, luv

# Add more commands as needed
command_dict = {
    "hello": hello_command,
    "bye": bye_command,
    "test": crawl_bee_cost,
    "muối_buồn": muoibuon,
    "miss_duong": miss_duong,
    "miss_pam": miss_pam,
    "iu": luv,
}
