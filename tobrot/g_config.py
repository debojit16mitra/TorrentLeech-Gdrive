from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "1581011965:AAEy7O3dQwbgs-v5gvraHpQ5AAJ3GaVrH08"
    APP_ID = 1733305
    API_HASH = "f423cffca6b5b7247b31b5b0df61f48d"
    OWNER_ID = 1156597097
    AUTH_CHANNEL = [-1001377338298]
    DESTINATION_FOLDER = "Download" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
[kmac]
type = drive
client_id = 24644445636-le8qtpevii1jf672k7seeg0u1ru5vp3j.apps.googleusercontent.com
client_secret = 7129Wg4PYqfTgOqJZDVWyS2I
scope = drive
root_folder_id =
token = {"access_token":"ya29.a0AfH6SMBGancUBWLmfF2MODJpNhyRg5hHM0JmzGaVf5kHlN_HGfisP-EYvQoyliKysbvKBvonmMeWy981Fb5C_cJXp7w0_L22OYrveuQg_rLyGWXzr1VQe05oHRee8UnmVyBijEvNJRkSTGYltOPeS_8EqZPZfOBQCk6obbwnbzA","token_type":"Bearer","refresh_token":"1//0g-ByVm7cD9_eCgYIARAAGBASNwF-L9IrnQVGb5UdfeMdrH1JjL93Z89sQwBtxlUKSk1eSuKQXcSxPfNRTegxif6jylpUyuh0dTg","expiry":"2021-01-22T09:38:19.9912246-08:00"}
team_drive = 0ALyFD2RofrpdUk9PVA
"""
