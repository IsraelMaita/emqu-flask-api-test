#Imports
from firebase import firebase
from flask import Flask, json, jsonify, request
import names
import random
from random import randrange

#Firebase Database Connection
firebase = firebase.FirebaseApplication('https://emqutest-7c261-default-rtdb.firebaseio.com/',None)

#Flask Server
app = Flask(__name__)


##GET METHODS##
#Get all surveys
@app.route('/api/get-all-surveys', methods = ['GET'])
def getSurveys():
  result = firebase.get('/surveys','')
  return jsonify(result)

#Get surveys total
@app.route('/api/get-surveys-total', methods = ['GET'])
def getSurveysTotal():
  result = firebase.get('/surveys','')
  
  if (not result):
    return jsonify(0)
  
  return jsonify(len(result))

#Get social network popularity
@app.route('/api/social-network-popularity', methods = ['GET'])
def getPopular():
  result = firebase.get('/surveys','')

  if (not result):
    return ( {'MOST': 'FACEBOOK', 'LESS': 'FACEBOOK'} )

  facebook = 0
  whatsapp = 0
  twitter = 0
  instagram = 0
  tiktok = 0

  for key in result:
    value = result[key]

    if (value['favoriteNetwork'] == 'FACEBOOK'):
      facebook = facebook + 1
    elif (value['favoriteNetwork'] == 'WHATSAPP'):
      whatsapp = whatsapp + 1
    elif (value['favoriteNetwork'] == 'TWITTER'):
      twitter = twitter + 1
    elif (value['favoriteNetwork'] == 'INSTAGRAM'):
      instagram = instagram + 1
    elif (value['favoriteNetwork'] == 'TIKTOK'):
      tiktok = tiktok + 1
  
  
  popular = {
    'FACEBOOK': facebook,
    'WHATSAPP': whatsapp,
    'TWITTER': twitter,
    'INSTAGRAM': instagram,
    'TIKTOK': tiktok
  }

  popularNetwork = max(popular, key = popular.get)
  unpopularNetwork = min(popular, key = popular.get)

  return ( {'MOST': popularNetwork, 'LESS': unpopularNetwork} )

#Get Average Time per Social Network
@app.route('/api/average-time-per-social-network', methods = ['GET'])
def averageTime():
  result = firebase.get('/surveys','')

  if (not result):
    return ( {'FACEBOOK': 0.0, 'WHATSAPP': 0.0, 'TWITTER': 0.0, 'INSTAGRAM': 0.0, 'TIKTOK': 0.0} )

  facebook = 0.0
  facebookTotal = 0
  whatsapp = 0.0
  whatsappTotal = 0
  twitter = 0.0
  twitterTotal = 0
  instagram = 0.0
  instagramTotal = 0
  tiktok = 0.0
  tiktokTotal = 0

  total = int((len(result)))

  for key in result:
    value = result[key]
    facebookTotal = facebookTotal + value['averageTime']['facebook']
    whatsappTotal = whatsappTotal + value['averageTime']['whatsapp']
    twitterTotal = twitterTotal + value['averageTime']['twitter']
    instagramTotal = instagramTotal + value['averageTime']['instagram']
    tiktokTotal = tiktokTotal + value['averageTime']['tiktok']

  facebook = facebookTotal / total
  whatsapp = whatsappTotal / total
  twitter = twitterTotal / total
  instagram = instagramTotal / total
  tiktok = tiktokTotal / total

  return ( {'FACEBOOK': facebook, 'WHATSAPP': whatsapp, 'TWITTER': twitter, 'INSTAGRAM': instagram, 'TIKTOK': tiktok} )


#Get Demographic Distribution
@app.route('/api/demographic-distribution', methods = ['GET'])
def demographicDistribution():
  result = firebase.get('/surveys','')

  ageRange1 = {
    'FACEBOOK': 0,
    'WHATSAPP': 0,
    'TWITTER': 0,
    'INSTAGRAM': 0,
    'TIKTOK': 0
  }
  ageRange2 = {
    'FACEBOOK': 0,
    'WHATSAPP': 0,
    'TWITTER': 0,
    'INSTAGRAM': 0,
    'TIKTOK': 0
  }
  ageRange3 = {
    'FACEBOOK': 0,
    'WHATSAPP': 0,
    'TWITTER': 0,
    'INSTAGRAM': 0,
    'TIKTOK': 0
  }
  ageRange4 = {
    'FACEBOOK': 0,
    'WHATSAPP': 0,
    'TWITTER': 0,
    'INSTAGRAM': 0,
    'TIKTOK': 0
  }

  if (not result):
    return ({'AGE_RANGE_1': ageRange1, 'AGE_RANGE_2': ageRange2, 'AGE_RANGE_3': ageRange3, 'AGE_RANGE_4': ageRange4})

  for key in result:
    value = result[key]
    if (value['ageRange'] == 'AGE_RANGE_1'):
      ageRange1['FACEBOOK'] = ageRange1['FACEBOOK'] + value['averageTime']['facebook']
      ageRange1['WHATSAPP'] = ageRange1['WHATSAPP'] + value['averageTime']['whatsapp']
      ageRange1['TWITTER'] = ageRange1['TWITTER'] + value['averageTime']['twitter']
      ageRange1['INSTAGRAM'] = ageRange1['INSTAGRAM'] + value['averageTime']['instagram']
      ageRange1['TIKTOK'] = ageRange1['TIKTOK'] + value['averageTime']['tiktok']
    elif (value['ageRange'] == 'AGE_RANGE_2'):
      ageRange2['FACEBOOK'] = ageRange2['FACEBOOK'] + value['averageTime']['facebook']
      ageRange2['WHATSAPP'] = ageRange2['WHATSAPP'] + value['averageTime']['whatsapp']
      ageRange2['TWITTER'] = ageRange2['TWITTER'] + value['averageTime']['twitter']
      ageRange2['INSTAGRAM'] = ageRange2['INSTAGRAM'] + value['averageTime']['instagram']
      ageRange2['TIKTOK'] = ageRange2['TIKTOK'] + value['averageTime']['tiktok']
    elif (value['ageRange'] == 'AGE_RANGE_3'):
      ageRange3['FACEBOOK'] = ageRange3['FACEBOOK'] + value['averageTime']['facebook']
      ageRange3['WHATSAPP'] = ageRange3['WHATSAPP'] + value['averageTime']['whatsapp']
      ageRange3['TWITTER'] = ageRange3['TWITTER'] + value['averageTime']['twitter']
      ageRange3['INSTAGRAM'] = ageRange3['INSTAGRAM'] + value['averageTime']['instagram']
      ageRange3['TIKTOK'] = ageRange3['TIKTOK'] + value['averageTime']['tiktok']
    elif (value['ageRange'] == 'AGE_RANGE_4'):
      ageRange4['FACEBOOK'] = ageRange4['FACEBOOK'] + value['averageTime']['facebook']
      ageRange4['WHATSAPP'] = ageRange4['WHATSAPP'] + value['averageTime']['whatsapp']
      ageRange4['TWITTER'] = ageRange4['TWITTER'] + value['averageTime']['twitter']
      ageRange4['INSTAGRAM'] = ageRange4['INSTAGRAM'] + value['averageTime']['instagram']
      ageRange4['TIKTOK'] = ageRange4['TIKTOK'] + value['averageTime']['tiktok']

  return ({'AGE_RANGE_1': ageRange1, 'AGE_RANGE_2': ageRange2, 'AGE_RANGE_3': ageRange3, 'AGE_RANGE_4': ageRange4})



##POST METHODS##
#Create survey
@app.route('/api/create-survey', methods = ['POST'])
def createSurvey():

  #Data Structure Format
  survey = {
    "name": request.args.get('name', default = '-'),
    "email": request.args.get('email', default = '-'),
    "gender": request.args.get('gender', default = '-'),
    "ageRange": request.args.get('ageRange', default = '-'),
    "favoriteNetwork": request.args.get('favoriteNetwork', default = '-'),
    "favoriteTime": request.args.get('favoriteTime', default = '-'),
    "averageTime": {
      "facebook": request.args.get('facebook', default = 0, type = int),
      "whatsapp": request.args.get('whatsapp', default = 0, type = int),
      "twitter": request.args.get('twitter', default = 0, type = int),
      "instagram": request.args.get('instagram', default = 0, type = int),
      "tiktok": request.args.get('tiktok', default = 0, type = int)
    }
  }
  result = firebase.post('/surveys',survey)
  return result

#Create random survey
@app.route('/api/create-random-survey', methods = ['POST'])
def createRandomSurvey():
  
  gender_list = ['MALE', 'FEMALE', 'OTHER']
  ageRange_List = ['AGE_RANGE_1','AGE_RANGE_2','AGE_RANGE_3','AGE_RANGE_4']
  network_List = ['FACEBOOK','WHATSAPP','TWITTER','INSTAGRAM','TIKTOK']
  time_List = ['DAYTIME_1','DAYTIME_2','DAYTIME_3','DAYTIME_4']

  randomSurvey = {
    "name": names.get_full_name(gender='male'),
    "email": names.get_last_name()+'@yopmail.com',
    "gender": random.choice(gender_list),
    "ageRange": random.choice(ageRange_List),
    "favoriteNetwork": random.choice(network_List),
    "favoriteTime": random.choice(time_List),
    "averageTime": {
      "facebook": randrange(3),
      "whatsapp": randrange(3),
      "twitter": randrange(3),
      "instagram": randrange(3),
      "tiktok": randrange(3)
    }
  }

  result = firebase.post('/surveys',randomSurvey)
  return result

##DELETE METHODS##
#Delete all surveys
@app.route('/api/delete-all-surveys', methods = ['DELETE'])
def deletAllPeople():
  result = firebase.delete('/surveys','')
  return jsonify(result)

#Server Run
if __name__ == '__main__':
  app.run(debug=True)