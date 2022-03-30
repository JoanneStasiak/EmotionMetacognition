#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys

from psychopy.hardware import keyboard
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
psychopyVersion = '2021.1.2'
expName = 'HBC'
expInfo = {'Participant': '', 'Session': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\joann\\Downloads\\Grad School\\Research\\Metacognition EmoPhys\\HBC.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)
endExpNow = False
frameTolerance = 0.001
win = visual.Window(size=(1024, 768), fullscr=True, screen=0,  winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()
startClock = core.Clock()
key_resp_4 = keyboard.Keyboard()

trialClock = core.Clock()
star1 = visual.ShapeStim(win=win, vertices='star7', size=(0.75, 0.75),pos=(0, 0),lineWidth=1.0,fillColor='green',interpolate=True)
stop1 = visual.Polygon(win=win,edges=8, size=(0.65, 0.65),ori=0.0, pos=(0, 0),lineWidth=1.0, fillColor='crimson',depth=-1.0, interpolate=True)
text = visual.TextStim(win=win,text='STOP',font='Open Sans',pos=(0, 0), height=0.13,color='white',depth=-2.0);
key_resp_2 = keyboard.Keyboard()

trial2Clock = core.Clock()
star2 = visual.ShapeStim(win=win, vertices='star7',size=(0.75, 0.75),pos=(0, 0),lineWidth=1.0, lineColor='white', fillColor='forestgreen', interpolate=True)
stop2 = visual.Polygon(win=win,edges=8, size=(0.65, 0.65),pos=(0, 0),lineWidth=1.0, lineColor='white', fillColor='crimson',depth=-1.0, interpolate=True)
text_2 = visual.TextStim(win=win, text='STOP',pos=(0, 0), height=0.13, color='white', depth=-2.0);
key_resp = keyboard.Keyboard()

trial3Clock = core.Clock()
polygon_5 = visual.ShapeStim(win=win,vertices='star7',size=(0.75, 0.75),ori=0.0, pos=(0, 0), lineWidth=1.0, lineColor='white', fillColor='forestgreen',interpolate=True)
polygon_6 = visual.Polygon( win=win, edges=8, size=(0.65, 0.65), pos=(0, 0), lineWidth=1.0, lineColor='white', fillColor='crimson', depth=-1.0, interpolate=True)
text_3 = visual.TextStim(win=win, text='STOP',font='Open Sans',pos=(0, 0), height=0.13, color='white', depth=-2.0);
key_resp_3 = keyboard.Keyboard()
sound_1 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
sound_2 = sound.Sound('A', secs=2.0, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
globalClock = core.Clock()
routineTimer = core.CountdownTimer()

continueRoutine = True
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
startComponents = [key_resp_4]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)
frameN = -1

while continueRoutine:
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        key_resp_4.frameNStart = frameN
        key_resp_4.tStart = t
        key_resp_4.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp_4, 'tStartRefresh')
        key_resp_4.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            continueRoutine = False
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()

for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()
continueRoutine = True
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
sound_1.setSound('A', secs=2.0, hamming=True)
sound_1.setVolume(1.0, log=False)
sound_2.setSound('A', secs=2.0, hamming=True)
sound_2.setVolume(1.0, log=False)
trialComponents = [star1, stop1, text, key_resp_2,sound_1, sound_2]
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

while continueRoutine:
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if star1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        star1.frameNStart = frameN
        star1.tStart = t
        star1.tStartRefresh = tThisFlipGlobal
        # ADD EVENT CODE HERE - START
        win.timeOnFlip(star1, 'tStartRefresh')
        star1.setAutoDraw(True)
    if star1.status == STARTED:
        if tThisFlipGlobal > star1.tStartRefresh + 2.0-frameTolerance:
            star1.tStop = t
            star1.frameNStop = frameN
            win.timeOnFlip(star1, 'tStopRefresh')
            star1.setAutoDraw(False)
    if stop1.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        stop1.frameNStart = frameN
        stop1.tStart = t
        stop1.tStartRefresh = tThisFlipGlobal
        # ADD EVENT CODE HERE - STOP
        win.timeOnFlip(stop1, 'tStartRefresh')
        stop1.setAutoDraw(True)
    if stop1.status == STARTED:
        if tThisFlipGlobal > stop1.tStartRefresh + 2.0-frameTolerance:
            stop1.tStop = t
            stop1.frameNStop = frameN
            win.timeOnFlip(stop1, 'tStopRefresh')
            stop1.setAutoDraw(False)
    if text.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        text.frameNStart = frameN
        text.tStart = t
        text.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text, 'tStartRefresh')
        text.setAutoDraw(True)
    if text.status == STARTED:
        if tThisFlipGlobal > text.tStartRefresh + 3.0-frameTolerance:
            text.tStop = t
            text.frameNStop = frameN
            win.timeOnFlip(text, 'tStopRefresh')
            text.setAutoDraw(False)
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        sound_1.frameNStart = frameN
        sound_1.tStart = t
        sound_1.tStartRefresh = tThisFlipGlobal
        sound_1.play(when=win)
    if sound_1.status == STARTED:
        if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
            sound_1.tStop = t
            sound_1.frameNStop = frameN
            win.timeOnFlip(sound_1, 'tStopRefresh')
            sound_1.stop()
    if sound_2.status == NOT_STARTED and tThisFlip >= 25.0-frameTolerance:
        sound_2.frameNStart = frameN
        sound_2.tStart = t
        sound_2.tStartRefresh = tThisFlipGlobal
        sound_2.play(when=win)
    if sound_2.status == STARTED:
        if tThisFlipGlobal > sound_2.tStartRefresh + 2.0-frameTolerance:
            sound_2.tStop = t
            sound_2.frameNStop = frameN
            win.timeOnFlip(sound_2, 'tStopRefresh')
            sound_2.stop()

    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 27.0-frameTolerance:
        key_resp_2.frameNStart = frameN
        key_resp_2.tStart = t
        key_resp_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp_2, 'tStartRefresh')
        key_resp_2.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            continueRoutine = False

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
thisExp.addData('Star 1.started', star1.tStartRefresh)
thisExp.addData('Star 1.stopped', star1.tStopRefresh)
thisExp.addData('Stop 1.started', stop1.tStartRefresh)
thisExp.addData('Stop 1.stopped', stop1.tStopRefresh)
if key_resp_2.keys in ['', [], None]:
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()

continueRoutine = True
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
trial2Components = [star2, stop2, text_2, key_resp, sound_1, sound_2]
for thisComponent in trial2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

while continueRoutine:
    t = trial2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if star2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        star2.frameNStart = frameN
        star2.tStart = t
        star2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(star2, 'tStartRefresh')
        star2.setAutoDraw(True)
    if star2.status == STARTED:
        if tThisFlipGlobal > star2.tStartRefresh + 2.0-frameTolerance:
            star2.tStop = t
            star2.frameNStop = frameN
            win.timeOnFlip(star2, 'tStopRefresh')
            star2.setAutoDraw(False)

    if stop2.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        stop2.frameNStart = frameN
        stop2.tStart = t
        stop2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(stop2, 'tStartRefresh')
        stop2.setAutoDraw(True)
    if stop2.status == STARTED:
        if tThisFlipGlobal > stop2.tStartRefresh + 2.0-frameTolerance:
            stop2.tStop = t
            stop2.frameNStop = frameN
            win.timeOnFlip(stop2, 'tStopRefresh')
            stop2.setAutoDraw(False)
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        sound_1.frameNStart = frameN
        sound_1.tStart = t
        sound_1.tStartRefresh = tThisFlipGlobal
        sound_1.play(when=win)
    if sound_1.status == STARTED:
        if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
            sound_1.tStop = t
            sound_1.frameNStop = frameN
            win.timeOnFlip(sound_1, 'tStopRefresh')
            sound_1.stop()
    if sound_2.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        sound_2.frameNStart = frameN
        sound_2.tStart = t
        sound_2.tStartRefresh = tThisFlipGlobal
        sound_2.play(when=win)
    if sound_2.status == STARTED:
        if tThisFlipGlobal > sound_2.tStartRefresh + 2.0-frameTolerance:
            sound_2.tStop = t
            sound_2.frameNStop = frameN
            win.timeOnFlip(sound_2, 'tStopRefresh')
            sound_2.stop()

    if text_2.status == NOT_STARTED and tThisFlip >= 35.0-frameTolerance:
        text_2.frameNStart = frameN
        text_2.tStart = t
        text_2.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text_2, 'tStartRefresh')
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        if tThisFlipGlobal > text_2.tStartRefresh + 2.0-frameTolerance:
            text_2.tStop = t
            text_2.frameNStop = frameN
            win.timeOnFlip(text_2, 'tStopRefresh')
            text_2.setAutoDraw(False)

    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 37.0-frameTolerance:
        key_resp.frameNStart = frameN
        key_resp.tStart = t
        key_resp.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp, 'tStartRefresh')
        key_resp.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            continueRoutine = False

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break

    if continueRoutine:
        win.flip()

for thisComponent in trial2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Star 2.started', star2.tStartRefresh)
thisExp.addData('Star 2.stopped', star2.tStopRefresh)
thisExp.addData('Stop 2.started', stop2.tStartRefresh)
thisExp.addData('Stop 2.stopped', stop2.tStopRefresh)
if key_resp.keys in ['', [], None]:
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()
continueRoutine = True
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
trial3Components = [polygon_5, polygon_6, text_3, key_resp_3, sound_1, sound_2]
for thisComponent in trial3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trial3Clock.reset(-_timeToFirstFrame)
frameN = -1
while continueRoutine:
    t = trial3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trial3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        polygon_5.frameNStart = frameN
        polygon_5.tStart = t
        polygon_5.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(polygon_5, 'tStartRefresh')
        polygon_5.setAutoDraw(True)
    if polygon_5.status == STARTED:
        if tThisFlipGlobal > polygon_5.tStartRefresh + 2.0-frameTolerance:
            polygon_5.tStop = t
            polygon_5.frameNStop = frameN
            win.timeOnFlip(polygon_5, 'tStopRefresh')
            polygon_5.setAutoDraw(False)
    if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        sound_1.frameNStart = frameN
        sound_1.tStart = t
        sound_1.tStartRefresh = tThisFlipGlobal
        sound_1.play(when=win)
    if sound_1.status == STARTED:
        if tThisFlipGlobal > sound_1.tStartRefresh + 2.0-frameTolerance:
            sound_1.tStop = t
            sound_1.frameNStop = frameN
            win.timeOnFlip(sound_1, 'tStopRefresh')
            sound_1.stop()
    if sound_2.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        sound_2.frameNStart = frameN
        sound_2.tStart = t
        sound_2.tStartRefresh = tThisFlipGlobal
        sound_2.play(when=win)
    if sound_2.status == STARTED:
        if tThisFlipGlobal > sound_2.tStartRefresh + 2.0-frameTolerance:
            sound_2.tStop = t
            sound_2.frameNStop = frameN
            win.timeOnFlip(sound_2, 'tStopRefresh')
            sound_2.stop()

    if polygon_6.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        polygon_6.frameNStart = frameN
        polygon_6.tStart = t
        polygon_6.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(polygon_6, 'tStartRefresh')
        polygon_6.setAutoDraw(True)
    if polygon_6.status == STARTED:
        if tThisFlipGlobal > polygon_6.tStartRefresh + 2.0-frameTolerance:
            polygon_6.tStop = t
            polygon_6.frameNStop = frameN
            win.timeOnFlip(polygon_6, 'tStopRefresh')
            polygon_6.setAutoDraw(False)

    if text_3.status == NOT_STARTED and tThisFlip >= 60.0-frameTolerance:
        text_3.frameNStart = frameN
        text_3.tStart = t
        text_3.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(text_3, 'tStartRefresh')
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        if tThisFlipGlobal > text_3.tStartRefresh + 2.0-frameTolerance:
            text_3.tStop = t
            text_3.frameNStop = frameN
            win.timeOnFlip(text_3, 'tStopRefresh')
            text_3.setAutoDraw(False)

    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 62.0-frameTolerance:
        key_resp_3.frameNStart = frameN
        key_resp_3.tStart = t
        key_resp_3.tStartRefresh = tThisFlipGlobal
        win.timeOnFlip(key_resp_3, 'tStartRefresh')
        key_resp_3.status = STARTED
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            continueRoutine = False

    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    if not continueRoutine:
        break
    continueRoutine = False
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break
    if continueRoutine:
        win.flip()
for thisComponent in trial3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)

if key_resp_3.keys in ['', [], None]:
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
routineTimer.reset()
win.flip()
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
thisExp.abort()
win.close()
