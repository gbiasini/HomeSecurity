import glob, os, time, json, subprocess, datetime as dt

hasSettingsLoaded = False

# Location of Project Path
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) + os.sep

#Load SettingFile
try:
    with open(__location__ + 'settings.json', 'r') as settingsFile:
        settings = json.load(settingsFile)
        hasSettingsLoaded = True
except Exception as ex:
    hasSettingsLoaded = False

if hasSettingsLoaded:
    try:
        while True:
            fileList = glob.glob(settings['PathToNasRecordings'] + "*")
            currentDateTime = dt.datetime.now()

            if len(fileList) > 0:
                for file in fileList:
                    fileName = ''
                
                    if file.endswith('.mp4'):
                        fileName = file[:-4]

                    if fileName.startswith(settings['PathToNasRecordings']):
                        fileName = fileName.replace(settings['PathToNasRecordings'], '')

                    fileNameDateTime = dt.datetime.strptime(fileName, '%d-%m-%Y_%H-%M-%S')
                
                    if fileNameDateTime <= currentDateTime - dt.timedelta(hours = 24):
                        os.remove(file)
            
            # if os.path.ismount(settings['PathToNas']):
            #     fileList = glob.glob(settings['PathToLocalRecordings'] + '*')
                
            #     if len(fileList) > 0:
            #         fileList = sorted(fileList)
            #         del fileList[-1]
            #         for file in fileList:
            #             subprocess.Popen('mv' + settings['PathToLocalRecordings'] + file + ' ' + settings['PathToNasRecordings'], shell=True)

            time.sleep(3000)
    except Exception as ex:
        with open(settings['PathToLogs'] + 'Update_Overlay_Text.log', 'a') as logFile:
            logFile.write(str(ex) + '\n')
    finally:
        pass