from info import access_key_id, secret_access_key, bucket_name
from boto3.s3.transfer import S3Transfer
import boto3

#info zawiera informacja takie jak np. Klucz do AWS którego nie chciałem ujawniać gdyż skoro już założyłem konto to chciał bym z niego korzystać (:

client = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


def upload_file(file_path, folder_name):
    folder_name = folder_name
    file_name = file_path
    transfer = S3Transfer(client)
    transfer.upload_file(file_name, bucket_name, folder_name + "/" + file_name)


def download_file(file_name, folder_name, save_path):
    full_path = folder_name + "/" + file_name
    client.download_file(bucket_name, full_path, save_path)


#szybkie sprawdzenie czy wysłało się poprawnie
def test():
    test_3 = "before_upload.txt"
    test_f = "test_f"
    save_path = "after_download"
    before_upload = open(test_3)
    upload_file(file_path=test_3, folder_name=test_f)
    download_file(file_name=test_3, folder_name=test_f, save_path=save_path)
    after_download = open(save_path)
    before = ""
    after = ""
    for line in before_upload:
        before.join(line)
    for line in after_download:
        after.join(line)
    print(before == after)


if __name__ == '__main__':
    test_folder_name = "test_f"
    test_file_name = "test_1.txt"
    test_2_file_path = "test_2"
    upload_file(file_path=test_2_file_path, folder_name=test_folder_name)
    test()
