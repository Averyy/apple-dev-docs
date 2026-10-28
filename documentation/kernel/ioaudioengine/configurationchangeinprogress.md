# configurationChangeInProgress

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```c
bool configurationChangeInProgress;
```

## Overview

Set to true after beginConfigurationChange() and false upon a subsequent call to completeConfigurationChange() or cancelConfigurationChange().

## See Also

### Instance Variables
- [workLoop](./workloop.md)
- [userClients](./userclients.md)
- [status](./status.md)
- [state](./state.md)
- [sampleRate](./samplerate.md)
- [runEraseHead](./runerasehead.md)
- [outputStreams](./outputstreams.md)
- [numSampleFramesPerBuffer](./numsampleframesperbuffer.md)
- [numErasesPerBuffer](./numerasesperbuffer.md)
- [numActiveUserClients](./numactiveuserclients.md)
- [isRegistered](./isregistered.md)
- [inputStreams](./inputstreams.md)
- [deviceStartedAudioEngine](./devicestartedaudioengine.md)
- [defaultAudioControls](./defaultaudiocontrols.md)
- [commandGate](./commandgate.md)
- [audioEngineStopPosition](./audioenginestopposition.md)
- [audioDevice](./audiodevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioengine/configurationchangeinprogress)*