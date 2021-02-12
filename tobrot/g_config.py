from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1622073183:AAFEVcuHUpMQk7TzpcI1imadeq8YC4WyIY8"
    APP_ID = 2776597
    API_HASH = "2c0b3f7d9e283b9c6f5e60bcf063fdb4"
    OWNER_ID = 998646192
    AUTH_CHANNEL = [-1001305859685]
    DESTINATION_FOLDER = "DOWNLOAD" #Name of your folder read readme(not id of the folder)
    INDEX_LINK = "https://testing.bunny.workers.dev/0:/Download"
    RCLONE_CONFIG = """
[BunnyDrive]
type = drive
client_id = 1075453807926-4lo134sht0k6tkieusfcd73c0gk7jb3g.apps.googleusercontent.com
client_secret = Oj8bcI-W6GR6xKQiWeaYi_q_
scope = drive
root_folder_id = 
token = {"access_token":"ya29.a0AfH6SMB6yHaTQ2nOOi7EW1QK4J734MCxdKoyspm-LZb1ri-1WqaiM0K75Dh2WJ3TOP5gdBOQyabhBfOSY3lB0oZYBUFzysVv5vlkbt7UR3cAcl-nzsF-kfshwpsj9KrXKmGz-iDzwKYB-Nlbhv3os84sH5l4MQMLCd4UjjYPLKk","token_type":"Bearer","refresh_token":"1//0gN38hjDQ_TMPCgYIARAAGBASNwF-L9IrTsoIIPsnV7PoiCNvxq4ndj5QsRFQbcZ231OUXH-thTEUj2agfTZug-4chDOpYudRNXI","expiry":"2021-02-11T11:40:00.9146405+05:30"}
team_drive = 0AAoPf0BluNRqUk9PVA 
"""
