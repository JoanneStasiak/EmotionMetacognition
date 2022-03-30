# Metacognitive Awareness of Emotional Responding
# Author: Jo Stasiak

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
from psychopy import prefs
from psychopy import gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, STOPPED, FINISHED)
import numpy as np
from numpy.random import random, choice
from psychopy.hardware import keyboard
import pandas as pd
from collections import Counter
import random
import sys
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

exec(open('shuffleScript.py').read())

expName = "Metacognitive Awareness of Emotional Responding"
expInfo = {"Participant" :"", "Date":""}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()
win = visual.Window(size=(1024, 768), fullscr=True, screen=0,  winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

fileName =  u'Data/%s_%s' % (expInfo['Participant'], expName)
thisExp = data.ExperimentHandler(name=expName, extraInfo=expInfo, dataFileName = fileName)
logFile = logging.LogFile(fileName+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)
endExpNow = False
frameTolerance = 0.001

defaultKeyboard = keyboard.Keyboard()
spaceKey = keyboard.Keyboard()
choiceKeys = keyboard.Keyboard()
instText = visual.TextStim(win=win, text='', pos=[0,0], height=0.05, wrapWidth = 1.1, color='white')


trialClock = core.Clock()
image = visual.ImageStim(win=win,image='sin', pos=(0, 0), size=(0.85, 0.85),interpolate=True)
text = visual.TextStim(win=win,text='+',pos=(0, 0), height=0.1, color='white');
image_2 = visual.ImageStim(win=win,image='sin', pos=(0, 0), size=(0.85, 0.85))
text_2 = visual.TextStim(win=win, text='+',pos=(0, 0), height=0.1,color='white');

q1Clock = core.Clock()
accuracy = visual.TextStim(win=win,text='',pos=(0, 0.25), height=0.09, wrapWidth=1.45,color='white');
choice1 = visual.TextStim(win=win, text='',pos=(-0.35, -0.1), height=0.13, color='white');
choice2 = visual.TextStim(win=win, text='', pos=(0.35, -0.1), height=0.13, color='white');
polygon = visual.Rect(win=win, width=(0.25, 0.3)[0], height=(0.25, 0.3)[1], pos=(-0.35, -0.1), lineWidth=6.0, lineColor='black', fillColor=None)
polygon_2 = visual.Rect(win=win,width=(0.25, 0.3)[0], height=(0.25, 0.3)[1], pos=(0.35, -0.1),lineWidth=6.0, lineColor='black', fillColor=None)
key_resp = keyboard.Keyboard()
blank = visual.TextStim(win=win, text='', pos=(0,0), height=0.001, color='white')
blank2 = visual.TextStim(win=win, text='', pos=(0,0), height=0.001, color='white')
q2Clock = core.Clock()
certainty = visual.TextStim(win=win, text='', pos=(0, 0.25), height=0.09, wrapWidth=1.45, color='white');
slider = visual.Slider(win=win, size=(1.0, 0.08), pos=(0, -0.15), ticks=(1, 2, 3, 4), granularity=1.0, style='rating', color='LightGray', fillColor='Blue', borderColor='White', labelHeight=0.05, flip=False, depth=-1, readOnly=False)
leftAnchor = visual.TextStim(win=win, text='Not at all',pos=(-0.515, -0.275), height=0.06, color='white');
one = visual.TextStim(win=win, text='1', pos=(-0.5, -0.23), height=0.04, color='white');
two = visual.TextStim(win=win, text='2', pos=(-0.24, -0.23), height=0.04, color='white');
three = visual.TextStim(win=win, text='3', pos=(0.24, -0.23), height=0.04, color='white');
four = visual.TextStim(win=win, text='4', pos=(0.5, -0.23), height=0.04, color='white');

rightAnchor = visual.TextStim(win=win, text='Completely', pos=(0.515, -0.275), height=0.06, color='white');
key_resp_2 = keyboard.Keyboard()

itiClock = core.Clock()
text_3 = visual.TextStim(win=win,text='+', pos=(0, 0), height=0.08,color='white');

globalClock = core.Clock()
routineTimer = core.CountdownTimer()


#Begin intro loop
def instructionsFunction(text):
    continueRoutine = True
    instructionComponents= [instText, spaceKey]
    for i in instructionComponents:
        i.status = STARTED
    while continueRoutine:
        instText.setText(text)
        instText.setAutoDraw(True)
        win.flip()
        if spaceKey.status == STARTED:
            theseKeys = spaceKey.getKeys(keyList=['space'])
            if len(theseKeys):
                continueRoutine = False
                instText.setAutoDraw(False)
                spaceKey.rt = theseKeys[-1].rt
        if defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
    thisExp.addData("Instructions Text", instText.text)
    thisExp.addData("Space RT", spaceKey.rt)
    spaceKey.keys=[]
    spaceKey.rt=[]
    thisExp.nextEntry()

isiClock=core.Clock()
isiOffsetTime=[0]
routineTimer = core.CountdownTimer()
def isiFunc(timeVar):
    
    continueRoutine = True
    routineTimer.add(timeVar)
    isiComponents = [text]
    for thisComponent in isiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isiClock.reset(-_timeToFirstFrame)
    frameN = -1

    # every frame isi
    while continueRoutine and routineTimer.getTime() > 0:
        t = isiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1

        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            text.frameNStart = frameN
            text.tStart = t
            text.tStartRefresh = tThisFlipGlobal
            win.timeOnFlip(text, 'tStartRefresh')
            text.setAutoDraw(True)
        if text.status == STARTED:
            if tThisFlipGlobal > text.tStartRefresh + timeVar-frameTolerance:
                text.tStop = t
                text.frameNStop = frameN
                win.timeOnFlip(text, 'tStopRefresh')
                text.setAutoDraw(False)
        isiOffsetTime.append(text.tStartRefresh + isiClock.getTime())

        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break

        if continueRoutine:
            win.flip()

    # end isi
    for thisComponent in isiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('isi Onset', text.tStartRefresh)
#    thisExp.addData('isi Offset', isiOffsetTime)
    thisExp.addData("isi Duration", text.tStop)
    thisExp.addData("isi Offset", isiOffsetTime[-1])


instArray=["In this part of the study, you will be viewing images and judging your emotional responses to them. \n\n Press SPACE to continue.",\
    "You will be completing a series of trials in which you will see two images presented in sequence on the screen. Following the second image, you will be prompted to choose which of the two intervals provoked a bigger change in heart rate. \n\nPress the '1' key if the first interval provoking a bigger heart rate change. Press the '2' key if the second interval provoking a bigger heart rate change.\n\nPress SPACE to continue.",\
    "You will also be asked to assess how certain you are in your interval choice. You will make this assessment on a rating scale ranging from 1 ('Not at all certain') to 4 ('Completely certain'). \nYou can use the keys 1,2,3,4 to make your response.\n\nPress SPACE to continue.",\
    "For each question, you will have as much time as you need to respond. \nYou will then see a fixation cross on the screen and the task will continue to the next trial. \n\nPress SPACE to continue.",
    "You will be given breaks intermittently throughout this task. The task will last about one hour in total. \n\nWhen you are ready to begin, please press SPACE!"]
timeList = [3,3,5,5,5,7,7,7,3,3,3,3]
#run = [1,2,3,4,5,6,7]
for i in instArray:
    instructionsFunction(i)
isiFunc(5.000)
counter=0
trials = data.TrialHandler(nReps=1.0, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Rows.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)
thisTrial = trials.trialList[0]
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
#rowList=['00:40', '40:80', '80:120', '120:160', '160:200', '200:240']
#for i in rowList:


    trials_2 = data.TrialHandler(nReps=1.0, method='random',
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('AllBlocks.csv', selection=Rows),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)
    thisTrial_2 = trials_2.trialList[0]
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        continueRoutine = True
        routineTimer.add(9.000100)
        text.setText("+")
        image.setImage(Img1Dir)
        image_2.setImage(Img2Dir)
        trialComponents = [image, text, image_2, text_2]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame) 
        frameN = -1

        while continueRoutine and routineTimer.getTime() > 0:
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1

            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                image.frameNStart = frameN  
                image.tStart = t  
                image.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(image, 'tStartRefresh')
                image.setAutoDraw(True)
            if image.status == STARTED:
                if tThisFlipGlobal > image.tStartRefresh + 0.5-frameTolerance:
                    image.tStop = t  
                    image.frameNStop = frameN  
                    win.timeOnFlip(image, 'tStopRefresh')
                    image.setAutoDraw(False)

            if text.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:                
                text.frameNStart = frameN  
                text.tStart = t  
                text.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(text, 'tStartRefresh')
                text.setAutoDraw(True)
            if text.status == STARTED:
                if tThisFlipGlobal > text.tStartRefresh + 4.0-frameTolerance:
                    text.tStop = t  
                    text.frameNStop = frameN  
                    win.timeOnFlip(text, 'tStopRefresh')
                    text.setAutoDraw(False)

            if image_2.status == NOT_STARTED and tThisFlip >= 4.5-frameTolerance:                
                image_2.frameNStart = frameN  
                image_2.tStart = t  
                image_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(image_2, 'tStartRefresh')
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                if tThisFlipGlobal > image_2.tStartRefresh + 0.5-frameTolerance:
                    image_2.tStop = t  
                    image_2.frameNStop = frameN  
                    win.timeOnFlip(image_2, 'tStopRefresh')
                    image_2.setAutoDraw(False)

            if text_2.status == NOT_STARTED and tThisFlip >= 5.0-frameTolerance:                
                text_2.frameNStart = frameN  
                text_2.tStart = t  
                text_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(text_2, 'tStartRefresh')
                text_2.setAutoDraw(True)
            if text_2.status == STARTED:
                if tThisFlipGlobal > text_2.tStartRefresh + 4.0-frameTolerance:
                    text_2.tStop = t  
                    text_2.frameNStop = frameN  
                    win.timeOnFlip(text_2, 'tStopRefresh')
                    text_2.setAutoDraw(False)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine: 
                break
            continueRoutine = False  
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break 
            if continueRoutine:  
                win.flip()
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('Image 1 Started', image.tStartRefresh)
        trials_2.addData('Image 1 Stopped', image.tStopRefresh)
        trials_2.addData('ISI Started', text.tStartRefresh)
        trials_2.addData('ISI Stopped', text.tStopRefresh)
        trials_2.addData('Image 2 Started', image_2.tStartRefresh)
        trials_2.addData('Image 2 Stopped', image_2.tStopRefresh)
        trials_2.addData('ISI2 Started', text_2.tStartRefresh)
        trials_2.addData('ISI2 Stopped', text_2.tStopRefresh)

        continueRoutine = True
        accuracy.setText('Which interval provoked the greater change in heart rate?')
        choice1.setText('1')
        choice2.setText('2')
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        choice2.setColor("white")
        choice1.setColor("white")
        blank.status = NOT_STARTED
        q1Components = [accuracy, choice1, choice2, polygon, polygon_2, key_resp]
        for thisComponent in q1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q1Clock.reset(-_timeToFirstFrame) 
        frameN = -1

        while continueRoutine:
            t = q1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  

            if accuracy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                accuracy.frameNStart = frameN  
                accuracy.tStart = t  
                accuracy.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(accuracy, 'tStartRefresh')
                accuracy.setAutoDraw(True)

            
            if choice1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                choice1.frameNStart = frameN  
                choice1.tStart = t  
                choice1.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(choice1, 'tStartRefresh')
                choice1.setAutoDraw(True)

            if choice2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:        
                choice2.frameNStart = frameN  
                choice2.tStart = t  
                choice2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(choice2, 'tStartRefresh')
                choice2.setAutoDraw(True)

            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:    
                polygon.frameNStart = frameN  
                polygon.tStart = t  
                polygon.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(polygon, 'tStartRefresh')
                polygon.setAutoDraw(True)

            if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                polygon_2.frameNStart = frameN  
                polygon_2.tStart = t  
                polygon_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(polygon_2, 'tStartRefresh')
                polygon_2.setAutoDraw(True)

            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                key_resp.frameNStart = frameN  
                key_resp.tStart = t  
                key_resp.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(key_resp, 'tStartRefresh')
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard') 
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['1', '2'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name 
                    key_resp.rt = _key_resp_allKeys[-1].rt
            if key_resp.keys == '1':
                choice1.setColor("green")
                choice2.setColor("white")
            if key_resp.keys == '2':
                choice2.setColor("green")
                choice1.setColor("white")
            if blank.status == NOT_STARTED and (key_resp.keys == '1' or key_resp.keys== '2'):
                blank.frameNStart = frameN
                blank.tStart = t
                blank.tStartRefresh = tThisFlipGlobal
                blank.setAutoDraw(True)
                print("started blank")
            if blank.status == STARTED:
                if tThisFlipGlobal > blank.tStartRefresh + 1.0-frameTolerance:
                    blank.tStop = t  
                    blank.frameNStop = frameN
                    blank.setAutoDraw(False)
                    print("take away blank")
                    blank.status=FINISHED
                    print("Calling blank status finished every frame")
                    if blank.status == FINISHED:
                        continueRoutine=False
                        print("continue routine false")
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            if not continueRoutine: 
                break
            continueRoutine = False  
            for thisComponent in q1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break 
            if continueRoutine:  
                win.flip()

        for thisComponent in q1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('Accuracy Q Onset', accuracy.tStartRefresh)
        trials_2.addData('Accuracy Q Offset', accuracy.tStopRefresh)
        if key_resp.keys in ['', [], None]: 
            key_resp.keys = None
        trials_2.addData('Accuracy Response',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_2.addData('Accuracy Response RT', key_resp.rt)
        trials_2.addData('Accuracy Response Onset', key_resp.tStartRefresh)
        trials_2.addData('Accuracy Response Offset', key_resp.tStopRefresh)
        choice2.setColor("white")
        choice1.setColor("white")
        print("Calling blank status finished at endof routine")

        if blank.status == FINISHED:
            continueRoutine=False
            print("continue routine false")
        routineTimer.reset()

        continueRoutine = True
        certainty.setText('How certain are you of your interval choice?')
        slider.reset()
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        blank2.status = NOT_STARTED

        q2Components = [certainty, slider, leftAnchor, rightAnchor, key_resp_2, one, two, three, four]
        for thisComponent in q2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        q2Clock.reset(-_timeToFirstFrame) 
        frameN = -1

        while continueRoutine:
            t = q2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=q2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  
            if certainty.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:        
                certainty.frameNStart = frameN  
                certainty.tStart = t  
                certainty.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(certainty, 'tStartRefresh')
                certainty.setAutoDraw(True)
            if slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                slider.frameNStart = frameN  
                slider.tStart = t  
                slider.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(slider, 'tStartRefresh')
                slider.setAutoDraw(True)
            if slider.getRating() is not None and slider.status == STARTED:
                continueRoutine = False

            if leftAnchor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                leftAnchor.frameNStart = frameN  
                leftAnchor.tStart = t  
                leftAnchor.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(leftAnchor, 'tStartRefresh')
                leftAnchor.setAutoDraw(True)

            if rightAnchor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                rightAnchor.frameNStart = frameN  
                rightAnchor.tStart = t  
                rightAnchor.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(rightAnchor, 'tStartRefresh')
                rightAnchor.setAutoDraw(True)
                one.setAutoDraw(True)
                two.setAutoDraw(True)
                three.setAutoDraw(True)
                four.setAutoDraw(True)

            waitOnFlip = False
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                key_resp_2.frameNStart = frameN  
                key_resp_2.tStart = t  
                key_resp_2.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(key_resp_2, 'tStartRefresh')
                key_resp_2.status = STARTED
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard') 
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['1', '2', '3', '4'], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name 
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            keys = event.getKeys()
            if key_resp_2.keys == '1':
                slider.markerPos = 1
            if key_resp_2.keys == '2':
                slider.markerPos = 2
            if key_resp_2.keys == '3':
                slider.markerPos = 3
            if key_resp_2.keys == '4':
                slider.markerPos = 4

            if blank2.status == NOT_STARTED and (key_resp_2.keys == '1' or key_resp_2.keys == '2' or key_resp_2.keys == '3' or key_resp_2.keys == '4'):
                blank2.frameNStart = frameN
                blank2.tStart = t
                blank2.tStartRefresh = tThisFlipGlobal
                blank2.setAutoDraw(True)
                print("started blank")
            if blank2.status == STARTED:
                if tThisFlipGlobal > blank2.tStartRefresh + 0.8-frameTolerance:
                    blank2.tStop = t  
                    blank2.frameNStop = frameN
                    blank2.setAutoDraw(False)
                    print("take away blank")

                    blank2.status=FINISHED
                    print("Calling blank status finished every frame")
                    if blank2.status == FINISHED:
                        continueRoutine=False
                        print("continue routine false")

            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            if not continueRoutine: 
                break
            continueRoutine = False  
            for thisComponent in q2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break 
            if continueRoutine:
                win.flip()

        for thisComponent in q2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('Certainty Q Onset', certainty.tStartRefresh)
        trials_2.addData('Certainty Q Offset', certainty.tStopRefresh)
        if key_resp_2.keys in ['', [], None]:
            key_resp_2.keys = None
        trials_2.addData('Certainty Response',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            trials_2.addData('Certainty Response RT', key_resp_2.rt)
        trials_2.addData('Certainty Response Onset', key_resp_2.tStartRefresh)
        trials_2.addData('Certainty Response Offset', key_resp_2.tStopRefresh)
        thisExp.addData("Rating", slider.markerPos)

        if blank2.status == FINISHED:
            continueRoutine = False
        routineTimer.reset()

        continueRoutine = True
        routineTimer.add(1.000000)
        itiComponents = [text_3]
        for thisComponent in itiComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        itiClock.reset(-_timeToFirstFrame) 
        frameN = -1

        while continueRoutine and routineTimer.getTime() > 0:
            t = itiClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=itiClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                text_3.frameNStart = frameN  
                text_3.tStart = t  
                text_3.tStartRefresh = tThisFlipGlobal 
                win.timeOnFlip(text_3, 'tStartRefresh')
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                if tThisFlipGlobal > text_3.tStartRefresh + 1.0-frameTolerance:    
                    text_3.tStop = t  
                    text_3.frameNStop = frameN  
                    win.timeOnFlip(text_3, 'tStopRefresh')
                    text_3.setAutoDraw(False)
            
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()

            if not continueRoutine: 
                break
            continueRoutine = False  
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break
            if continueRoutine:  
                win.flip()

        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('ITI.started', text_3.tStartRefresh)
        trials_2.addData('ITI.stopped', text_3.tStopRefresh)
        thisExp.nextEntry()
    thisExp.nextEntry()
    counter+=1
    if counter > 1 and counter < 8:
        instructionsFunction("You have completed a block of trials. \n Please take a moment to rest your eyes, relax, or stretch before completing the next block of trials. \nWhen you are ready to begin, press SPACE!")
        isiFunc(5.0000)
win.flip()

instructionsFunction("You have completed this part of the study!\n\nPlease press SPACE.")

thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
core.quit()
