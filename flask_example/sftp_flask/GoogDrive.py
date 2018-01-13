#clent_id.json required.
#wlink - console.developers.google.com/apis/credentials


import os
import flask
import httplib2
from apiclient import discovery
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from flask import Flask, redirect, url_for, session, request, jsonify, render_template
from __init__ import app


@app.route('/goog_drive_auth/<name>')
def goog_drive_auth(name):
    credentials = get_credentials()
    if credentials == False:
        return flask.redirect(flask.url_for('oauth2callback'))
    elif credentials.access_token_expired:
        return flask.redirect(flask.url_for('oauth2callback'))
    else:
        #return "Hello World"
        return render_template("DriveTemp.html",Drive_name = "Google", path="Data\\"+name)


        #####fetch code #############
        #print('now calling fetch')
        # instead of root u will also give folder ID
        #all_files = fetch("'root' in parents and (mimeType = 'application/vnd.google-apps.folder' or mimeType != 'application/vnd.google-apps.folder')",
        #                  sort='modifiedTime desc')
        #all_files += fetch("'root' in parents and mimeType != 'application/vnd.google-apps.folder'",
         #                 sort='modifiedTime desc')
        #s = ""
        #for file in all_files:
        #    s += "%s, %s<br>" % (file['name'], file['id'])
        #return s

        #########fetch code end#############33


@app.route('/oauth2callback')
def oauth2callback():
    flow = client.flow_from_clientsecrets('client_id.json',
                                          scope='https://www.googleapis.com/auth/drive',
                                          redirect_uri=flask.url_for('oauth2callback',
                                                                     _external=True))
    # access drive api using developer credentials
    flow.params['include_granted_scopes'] = 'true'
    if 'code' not in flask.request.args:
        auth_uri = flow.step1_get_authorize_url()
        return flask.redirect(auth_uri)
    else:
        auth_code = flask.request.args.get('code')
        credentials = flow.step2_exchange(auth_code)
        open('Credentials\\'+session[request.environ['REMOTE_ADDR'] + 'username']+'credentials.json', 'w').write(credentials.to_json())  # write access token to credentials.json locally
        return flask.redirect(flask.url_for('goog_drive_auth',name=session[request.environ['REMOTE_ADDR'] + 'username']))


def get_credentials():
    #file_name = session[request.environ['REMOTE_ADDR'] + 'username']+'credentials.json'
    file_name = 'Credentials\\'+session[request.environ['REMOTE_ADDR'] + 'username']+'credentials.json'
    credential_path = file_name

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print("Credentials not found.")
        return False
    else:
        print("Credentials fetched successfully.")
        return credentials


def fetch(query, sort='modifiedTime desc' , name=None):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    results = service.files().list(
        q=query, orderBy=sort, pageSize=10, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    return items


def download_drive_file(file_id, output_file , name=None):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    # file_id = '0BwwA4oUTeiV1UVNwOHItT0xfa2M'
    #request = service.files().export_media(fileId=file_id,
     #                                      mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    request = service.files().get_media(fileId=file_id)

    fh = open(output_file, 'wb')
    #io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print ("Download %d%%." % int(status.progress() * 100))
    fh.close()



"""def upload():
    file_metadata = {'name': 'photo.jpg'}
    media = MediaFileUpload('files/photo.jpg',
                            mimetype='image/jpeg')
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print ('File ID: %s' % file.get('id'))"""







# return fh

def update_drive_file(file_id, local_file, name=None):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    # First retrieve the file from the API.
    file = service.files().get(fileId=file_id).execute()
    # File's new content.
    media_body = MediaFileUpload(local_file, resumable=True)
    # Send the request to the API.
    updated_file = service.files().update(
        fileId=file_id,
        # body=file,
        # newRevision=True,
        media_body=media_body).execute()
