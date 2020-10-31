import utils
import config
# https://drive.google.com/file/d/1-Fnm3tRx6zedcc-syHfms-yqZypByiIl/view?usp=sharing
if __name__ == "__main__":
    # TAKE ID FROM SHAREABLE LINK
    gdrive_file_id = '1-CdkbAmK_tPVANKSEaE_uMktcjiV44BR'
    # DESTINATION FILE ON YOUR DISK
    destination = config.model_path
    utils.download_file_from_google_drive(gdrive_file_id, destination)