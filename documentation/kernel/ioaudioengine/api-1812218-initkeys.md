# initKeys

**Framework**: Kernel  
**Kind**: instm

Generates the OSSymbols with the keys.

## Declaration

```c
static void initKeys();
```

## Overview

Do not call this directly. This is an internal initialization routine.

## See Also

### Miscellaneous
- [addAudioStream](./api-1812081-addaudiostream.md)
  Adds an IOAudioStream to the audio engine.
- [addTimer](./api-1812084-addtimer.md)
  Enables the timer event for the audio engine.
- [clearAllSampleBuffers](./api-1812089-clearallsamplebuffers.md)
  Zeros out all of the sample and mix buffers associated with the IOAudioEngine
- [clientClosed](./api-1812093-clientclosed.md)
  Called automatically when a user client closes its connection to the audio engine.
- [convertInputSamplesVBR](./api-1812098-convertinputsamplesvbr.md)
  Override this method if you want to return a different number of sample frames than was requested.
- [createDictionaryFromSampleRate](./api-1812105-createdictionaryfromsamplerate.md)
  Generates a dictionary matching the given sample rate.
- [createSampleRateFromDictionary](./api-1812109-createsampleratefromdictionary.md)
  Generates a sample rate from an OSDictionary.
- [eraseOutputSamples](./api-1812115-eraseoutputsamples.md)
  This function allows for the actual erasing of the mix and sample buffer to be overridden by a child class.
- [free](./api-1812122-free.md)
  Frees all of the resources allocated by the IOAudioEngine.
- [getAttributeForConnection](./api-1812127-getattributeforconnection.md)
  Generic method to retrieve some attribute of the audio engine, specific to one connection.
- [getCommandGate](./api-1812131-getcommandgate.md)
  Returns the IOCommandGate for this IOAudioEngine.
- [getCurrentSampleFrame](./api-1812136-getcurrentsampleframe.md)
  Gets the current sample frame from the IOAudioEngine subclass.
- [getRunEraseHead](./api-1812140-getrunerasehead.md)
  Returns true if the audio engine will run the erase head when the audio engine is running.
- [getSampleRate](./api-1812148-getsamplerate.md)
  Returns the sample rate of the IOAudioEngine in samples per second.
- [getState](./api-1812155-getstate.md)
  Returns the current state of the IOAudioEngine.
- [getStatus](./api-1812164-getstatus.md)
  Returns a pointer to the shared status buffer.
- [getTimerInterval](./api-1812174-gettimerinterval.md)
  Gets the timer interval for use by the timer event.
- [getWorkLoop](./api-1812185-getworkloop.md)
  Returns the IOWorkLoop for the driver.
- [init](./api-1812194-init.md)
  Performs initialization of a newly allocated IOAudioEngine.
- [initHardware](./api-1812206-inithardware.md)
  This function is called by start() to provide a convenient place for the subclass to perform its hardware initialization.
- [newUserClient](./api-1812227-newuserclient.md)
  Requests a new user client object for this service.
- [performAudioEngineStart](./api-1812238-performaudioenginestart.md)
  Called to start the audio I/O engine
- [performAudioEngineStop](./api-1812251-performaudioenginestop.md)
  Called to stop the audio I/O engine
- [performErase](./api-1812263-performerase.md)
  Performs erase head processing.
- [performFlush](./api-1812272-performflush.md)
  Performs the flush operation.
- [registerService](./api-1812282-registerservice.md)
  Called when this audio engine is ready to begin vending services.
- [removeTimer](./api-1812286-removetimer.md)
  Disables the timer event for the audio engine.
- [resetStatusBuffer](./api-1812290-resetstatusbuffer.md)
  Resets the status buffer to its default values.
- [setAttributeForConnection](./api-1812296-setattributeforconnection.md)
  Generic method to set some attribute of the audio engine, specific to one connection.
- [setClockDomain](./api-1812301-setclockdomain.md)
  Sets a property that CoreAudio uses to determine how devices are synchronized. If an audio device can tell that it is synchronized to another engine, it should set this value to that engine's clock domain. If an audio device can be a primary clock, it may publish its own clock domain for other devices to use.
- [setClockIsStable](./api-1812306-setclockisstable.md)
  This function sets a flag that CoreAudio uses to select its sample rate tracking algorithm. Set this to TRUE unless that results in dropped audio. If the driver is experiencing unexplained dropouts setting this FALSE might help.
- [setInputSampleOffset](./api-1812309-setinputsampleoffset.md)
  set the offset CoreAudio will read from off the current read pointer
- [setMixClipOverhead](./api-1812312-setmixclipoverhead.md)
  Used to tell IOAudioFamily when the watchdog timer must fire by.
- [setOutputSampleOffset](./api-1812315-setoutputsampleoffset.md)
  set the offset CoreAudio will write at off the current write pointer
- [setRunEraseHead](./api-1812317-setrunerasehead.md)
  Tells the audio engine whether or not to run the erase head.
- [setSampleLatency](./api-1812320-setsamplelatency.md)
  Sets the sample latency for the audio engine.
- [setSampleRate](./api-1812325-setsamplerate.md)
  Records the sample rate of the audio engine.
- [setState](./api-1812329-setstate.md)
  Indicates that the audio engine is in the specified state.
- [start(IOService *)](./api-1812338-start.md)
  A simple cover function for start(IOService *, IOAudioDevice *) that assumes the provider is the IOAudioDevice.
- [start(IOService *, IOAudioDevice *)](./api-1812342-start.md)
  Standard IOKit start() routine called to start an IOService.
- [startAudioEngine](./api-1812346-startaudioengine.md)
  Starts the audio I/O engine.
- [stop](./api-1812350-stop.md)
  Stops the service and prepares for the driver to be terminated.
- [stopAudioEngine](./api-1812359-stopaudioengine.md)
  Stops the audio I/O engine.
- [timerCallback](./api-1812365-timercallback.md)
  A static method used as a callback for the IOAudioDevice timer services.
- [timerFired](./api-1812371-timerfired.md)
  Indicates the timer has fired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioengine/1812218-initkeys)*