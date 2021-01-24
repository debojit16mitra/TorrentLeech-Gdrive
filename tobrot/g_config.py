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
