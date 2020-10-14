import requests
import sys

def download_file_from_google_drive(id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)

    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

# https://drive.google.com/file/d/1AshvpSDh8NJrpJemL7j7Dry97d71Jaog/view?usp=sharing
if __name__ == "__main__":
    # TAKE ID FROM SHAREABLE LINK
    file_id = '1AshvpSDh8NJrpJemL7j7Dry97d71Jaog'
    # DESTINATION FILE ON YOUR DISK
    destination = '/workspace/OSAM2020_4GB/model_epoch_10.pth'
    download_file_from_google_drive(file_id, destination)