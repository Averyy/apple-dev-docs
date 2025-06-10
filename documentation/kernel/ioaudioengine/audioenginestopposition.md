# audioEngineStopPosition

**Framework**: Kernel  
**Kind**: pseudo

## Declaration

```swift
IOAudioEnginePosition audioEngineStopPosition;
```

#### Overview

When all clients have disconnected, this is set to one buffer length past the current audio engine position at the time. Then when the stop position is reached, the audio engine is stopped

## See Also

- [workLoop](ioaudioengine/workloop.md)
- [userClients](ioaudioengine/userclients.md)
- [status](ioaudioengine/status.md)
- [state](ioaudioengine/state.md)
- [sampleRate](ioaudioengine/samplerate.md)
- [runEraseHead](ioaudioengine/runerasehead.md)
- [outputStreams](ioaudioengine/outputstreams.md)
- [numSampleFramesPerBuffer](ioaudioengine/numsampleframesperbuffer.md)
- [numErasesPerBuffer](ioaudioengine/numerasesperbuffer.md)
- [numActiveUserClients](ioaudioengine/numactiveuserclients.md)
- [isRegistered](ioaudioengine/isregistered.md)
- [inputStreams](ioaudioengine/inputstreams.md)
- [deviceStartedAudioEngine](ioaudioengine/devicestartedaudioengine.md)
- [defaultAudioControls](ioaudioengine/defaultaudiocontrols.md)
- [configurationChangeInProgress](ioaudioengine/configurationchangeinprogress.md)
- [commandGate](ioaudioengine/commandgate.md)
- [audioDevice](ioaudioengine/audiodevice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioengine/audioenginestopposition)*