script = 'function doGet(e){'+'return'+'ContentService.createTextOutput(''"Method GET not allowed");}'+' function doPost(e){'+'var send = GsenderV2.sendGmail(e);'+'return ContentService.createTextOutput(send);}'
print(script)