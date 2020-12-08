import sys
import os
import requests
import json

def mykwargs(argv):
    '''
    Processes argv list into plain args (list) and kwargs (dict).
    Just easier than using a library like argparse for small things.
    Example:
        python file.py arg1 arg2 arg3=val1 arg4=val2 -arg5 -arg6 --arg7
        Would create:
            args[arg1, arg2, -arg5, -arg6, --arg7]
            kargs{arg3 : val1, arg4 : val2}
        Params with dashes (flags) can now be processed seperately
    Shortfalls:
        spaces between k=v would result in bad params
        Flags aren't handled at all. Maybe in the future but this function
            is meant to be simple.
    Returns:
        tuple  (args,kargs)
    '''
    args = []
    kargs = {}

    for arg in argv:
        if '=' in arg:
            key,val = arg.split('=')
            kargs[key] = val
        else:
            args.append(arg)
    return args,kargs

def usage(message=None):
    if message:
        print(message)
    name = os.path.basename(__file__)
    print(f"Usage: python {name} [userid=id] [token=string]")
    print(f"Example:\n\t python {name} userid=id token=string \n")
    sys.exit()

def help():
  print("getActive: gets members in order of activity.")
  print("getMessage: gets messages.")
  print("getPubKey: gets the public key.")
  print("getUser: gets user information")
  print("postMessage: posts a message to the backend (requires user id)")
  print("postPubKey: posts your public key")
  print("postUser: posts your user information")
  print("exit: terminate the program.")
  print("Gets all members active within so much time")

def getActive(limit = None, token = None, userid = None):
  getUrl = "http://msubackend.xyz/api/?route=getActive&token=" + token + "&uid=" + userid
  if(limit != None):
    getUrl += "&limit="
    getUrl += limit
  r = requests.get(getUrl)
  active = json.loads(r.text)
  print(json.dumps(active, indent = 4, sort_keys = True))

def getMessages(count = None, token = None, userid = None):
  getUrl = "http://msubackend.xyz/api/?route=getMessage&token=" + token + "&uid=" + userid
  if(count == 1):
    getUrl += "&latest=true"
  elif(count > 0):
    getUrl += "&count="
    getUrl += str(count)
  r = requests.get(getUrl)
  messages = json.loads(r.text)
  print(json.dumps(messages, indent = 4, sort_keys = True))

def getPubKey(pid = None, token = None, userid = None):
  getUrl = "http://msubackend.xyz/api/?route=getPubKey&token=" + token + "&uid=" + userid
  if(pid != None):
    getUrl += "&user_id="
    getUrl += pid
  r = requests.get(getUrl)
  pubkey = json.loads(r.text)
  print(json.dumps(pubkey, indent = 4, sort_keys = True))

def getUser(email = None, fname = None, lname = None, token = None, userid = None):
  getUrl = "http://msubackend.xyz/api/?route=getUser&token=" + token + "&uid=" + userid
  if(email != None):
    getUrl += "&email="
    getUrl += email
  elif(fname != None):
    getUrl += "&fname="
    getUrl += fname
    getUrl += "&lname="
    getUrl += lname
  r = requests.get(getUrl)
  user = json.loads(r.text)
  print(json.dumps(user, indent = 4, sort_keys = True))

def postMessage(recipient = None, message = None, token = None, userid = None):
  posturl = "http://msubackend.xyz/api/?route=postMessage"
  payload = {
    'uid':userid,
    'to_uid':recipient,
    'message':message,
    'token':token
  }
  headers = {
  'Content-Type': 'application/json'
  }
  r = requests.post(posturl, headers=headers, json=payload)


def postPubKey(token = None, userid = None):
  posturl = "http://msubackend.xyz/api/?route=postPubKey"
  payload = {
    'pub_key':"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvI2QjAT3naoP8ZGFwKmc\n9b01//L0uUVKOZHRpnPGFgGklrFtqtljLcWlHnpzyq8SuI+4o8pPoDKLDLIREmbe\nfyiLTxs/nKFoOBUOOsY9PqdIruZU5oZDUgzg8wy5ODQIAR4SuxtnbSmy3IFp2zJB\nbNK1X4BLe/DsC+Xloc/R08EgKGUukXgMryhIKYCkrAyT/9YV5mxJzGvqYekqg0SL\nVGHkpH7UO7TQu9UpTCTasPjwePLKAb0PsmIDkjuBgkJo35hwK8HfIiYtwQxCdDWi\nINA7XYoy5/D11GauZN0a2/7mZU4uDY6iw2Js7wNlm6job93JVGTq4Fc9QGEZz6Pk\nTwIDAQAB\n-----END PUBLIC KEY-----",
    'uid':userid,
    'token':token
  }
  headers = {
  'Content-Type': 'application/json'
  }
  r = requests.post(posturl, headers=headers, json=payload)


def postUser(fname = None, lname = None, email = None, screen_name = None, token = None, userid = None):
  posturl = "http://msubackend.xyz/api/?route=postUser"
  payload = {}
  if(fname != None):
    payload['fname'] = fname
    payload['lname'] = lname
  if(email != None):
    payload['email'] = email
  if(screen_name != None):
    payload['screen_name'] = screen_name
  payload['token'] = token
  payload['uid'] = userid
  headers = {
  'Content-Type': 'application/json'
  }
  r = requests.post(posturl, headers=headers, json=payload)


def messaging(**kwargs):
  userid = kwargs.get('userid', None)
  token = kwargs.get('token', None)
  route = ""
  while(route != "exit"):
    route = input("What do you wish to do? (type in help for list of commands):")
    if(route == "help"):
      help()
    elif(route == "getActive"):
      limit = input("Please input how far back, in seconds, you want to search (type 0 for no limit):")
      if(limit == 0):
        getActive(None, token, userid)
      else:
        getActive(limit, token, userid)
    elif(route == "getMessage"):
      count = int(input("How many messages do you want to see? (type 0 for all messages):"))
      if(count == 1):
        getMessages(1, token, userid)
      elif(count <= 0):
        getMessages(0, token, userid)
      elif(count > 0):
        getMessages(count, token, userid)
    elif(route == "getPubKey"):
      pid = input("Please enter a specific user, or n if you want all public keys:")
      if (pid == "n"):
        getPubKey(None, token, userid)
      else:
        getPubKey(pid, token, userid)
    elif(route == "getUser"):
      choice = input("Do you want a specific user? Press y if yes, n if no:")
      if(choice == "n"):
        getUser(None, None, None, token, userid)
      elif(choice == "y"):
        fname = input("If you do not have their email, please input their name. Input their first name, or n if you don't have it:")
        if(fname != "n"):
          lname = input("Please input their last name:")
          getUser(None, fname, lname, token, userid)
        if(fname == "n"):
          email = input("Do you have their email? Enter email, or n if you do not have it:")
          if(email == "n"):
            getUser(None, None, None, token, userid)
          else:
            getUser(email, None, None, token, userid)
    elif(route == "postMessage"):
      recipient = input("Please provide the id of the user you are sending a message to:")
      message = input("Please enter your message:")
      postMessage(recipient, message, token, userid)
    elif(route == "postPubKey"):
      postPubKey(token, userid)
    elif(route == "postUser"):
      fname = input("Please enter your name, or n if you do not wish to provide one:")
      if(fname != "n"):
        lname = input("Please enter your last name:")
        postUser(fname, lname, None, None, token, userid)
      else:
        email = input("Please enter your email, or n if you do not wish to provide one:")
        if(email != "n"):
          postUser(None, None, email, None, token, userid)
        else:
          screen_name = input("Please enter your screen name, or n if you do not wish to provide one:")
          if(screen_name != "n"):
            postUser(None, None, None, screen_name, token, userid)
          else:
            postUser(None, None, None, None, token, userid)
      
    
  

if __name__=='__main__':
    """
    Change the required params value below accordingly.
    """

    required_params = 2 # adjust accordingly

    # get processed command line arguments 
    _,params = mykwargs(sys.argv[1:])

    # print usage if not called correctly
    if len(params) < required_params:
      usage()

    infile = params.get('userid', None)
    infile = params.get('token', None)

    if not infile: 
      usage()

    messaging(**params)

