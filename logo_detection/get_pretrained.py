import utils
import config
# https://drive.google.com/file/d/1AshvpSDh8NJrpJemL7j7Dry97d71Jaog/view?usp=sharing
if __name__ == "__main__":
    # TAKE ID FROM SHAREABLE LINK
    gdrive_file_id = '1AshvpSDh8NJrpJemL7j7Dry97d71Jaog'
    # DESTINATION FILE ON YOUR DISK
    destination = config.weights_path
    utils.download_file_from_google_drive(gdrive_file_id, destination)