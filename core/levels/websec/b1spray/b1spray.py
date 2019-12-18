import random
import os

import google.auth
from googleapiclient import discovery
from google.cloud import storage

from core.framework import levels
from core.framework.cloudhelpers import deployments, iam, gcstorage, cloudfunctions

LEVEL_PATH = 'websec/b1spray'
RESOURCE_PREFIX = 'b1'
INSTANCE_ZONE = 'us-west1-b'


def create():
    print("Level initialization started for: " + LEVEL_PATH)
    # Create randomized nonce name to avoid namespace conflicts
    nonce = str(random.randint(100000000000, 999999999999))
    bucket_name = f'{RESOURCE_PREFIX}-bucket-{nonce}'
    print("Level initialization finished for: " + LEVEL_PATH)
    
    source = 'scripts/'+RESOURCE_PREFIX+'/'
    user_r, pass_r = gen_credentials(source)
    # Insert deployment
    config_template_args = {'nonce': nonce, 'user_r': user_r, 'pass_r': pass_r}
    template_files = [
        'core/framework/templates/container_vm.jinja','core/framework/templates/ubuntu_vm.jinja']
    deployments.insert(LEVEL_PATH, template_files=template_files,
                       config_template_args=config_template_args)

    print("Level setup started for: " + LEVEL_PATH)
    # Insert secret into bucket
    #storage_client = storage.Client()
    #bucket = storage_client.get_bucket(bucket_name)
    #secret_blob = storage.Blob('secret.txt', bucket)
    #secret = levels.make_secret(LEVEL_PATH)
    #secret_blob.upload_from_string(secret)

    # Create service account key file
    #sa_key = iam.generate_service_account_key(f'{RESOURCE_PREFIX}-access')

    print(f'Level creation complete for: {LEVEL_PATH}')
    start_message = (
        f'Use attack.py, unames.txt and passwords.txt to find valid credential of the vulnerable website.')
    levels.write_start_info(LEVEL_PATH, start_message)
    print(
        f'Instruction for the level can be accessed at thunder-ctf.cloud/levels/{LEVEL_PATH}.html')
    
    #move helper scripts to thunder-ctf/start
    #will fail if dicrectory start/ not being created in previous steps--examples levels.write_start_info
    #to be continue....
    
    #dest = 'start/'
    #for f in os.listdir(source):
    #    cmd='cp '+ source+f +' '+ dest+f
    #    os.popen(cmd)
        #os.replace(source+f, dest+f)
    #change permission
    #for f in os.listdir(dest):
    #    os.chmod(dest+f, 0o700)
    #remove empty helper directory
    #os.rmdir(source)

def gen_credentials(source):
    
    #possible usernames
    u_srouce=source+'unames.txt'
    names=[uname.rstrip('\n') for uname in open(u_srouce,'r')]
    #most commanly used passwords
    p_srouce=source+'passwords.txt'
    passwords=[password.rstrip('\n').strip() for password in open(p_srouce,'r')]
    #randomly generate valid credientials
    rcreds={}
    random.shuffle(names)
    random.shuffle(passwords)
    return names[0],passwords[0]

def destroy():
    # Delete starting files
    levels.delete_start_files()
    # Delete deployment
    deployments.delete()
