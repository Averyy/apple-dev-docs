# IOAudioStream

**Framework**: Kernel  
**Kind**: cl

This class wraps a single sample buffer in an audio driver.

**Availability**:
- macOS 10.1+

## Declaration

```swift
class IOAudioStream : IOService
```

#### Overview

An IOAudioStream represents one hardware sample buffer as well as the direction of that buffer, the mix buffer that multiple clients mix into as well as a list of all of the formats to which this buffer can be set.

When an IOAudioEngine is created during init time in the driver, an IOAudioStream must be created for each sample buffer in the device. Typically, the sample buffer will be interleaved (or single channel), as a non-interleaved buffer should be divided into multiple single-channel buffers (and multiple IOAudioStreams).

Additionally, when an IOAudioStream is created it must have all of the possible formats (and allowed sample rates for each format) set and must have the currently set format specified (addAvailableFormat() and setFormat()).

## Topics

### Instance Methods
- [- addAvailableFormat](ioaudiostream/1580021-addavailableformat.md)
- [- addAvailableFormat](ioaudiostream/3516531-addavailableformat.md)
- [- addAvailableFormat](ioaudiostream/3516532-addavailableformat.md)
- [- addAvailableFormat](ioaudiostream/3516533-addavailableformat.md)
- [- addClient](ioaudiostream/1580015-addclient.md)
- [- addDefaultAudioControl](ioaudiostream/1580039-adddefaultaudiocontrol.md)
- [- clearAvailableFormats](ioaudiostream/1580032-clearavailableformats.md)
- [- clearSampleBuffer](ioaudiostream/1580056-clearsamplebuffer.md)
- [- clipIfNecessary](ioaudiostream/1580058-clipifnecessary.md)
- [- clipOutputSamples](ioaudiostream/1580040-clipoutputsamples.md)
- [- free](ioaudiostream/1580016-free.md)
- [- getDirection](ioaudiostream/1580048-getdirection.md)
- [- getFormat](ioaudiostream/1580050-getformat.md)
- [- getFormatExtension](ioaudiostream/1580019-getformatextension.md)
- [- getMaxNumChannels](ioaudiostream/1580049-getmaxnumchannels.md)
- [- getMetaClass](ioaudiostream/1580051-getmetaclass.md)
- [- getMixBuffer](ioaudiostream/1580037-getmixbuffer.md)
- [- getMixBufferSize](ioaudiostream/1580063-getmixbuffersize.md)
- [- getNumClients](ioaudiostream/1580054-getnumclients.md)
- [- getNumSampleFramesRead](ioaudiostream/1580061-getnumsampleframesread.md)
- [- getSampleBuffer](ioaudiostream/1580022-getsamplebuffer.md)
- [- getSampleBufferSize](ioaudiostream/1580028-getsamplebuffersize.md)
- [- getStartingChannelID](ioaudiostream/1580018-getstartingchannelid.md)
- [- getStreamAvailable](ioaudiostream/1580024-getstreamavailable.md)
- [- getWorkLoop](ioaudiostream/1580023-getworkloop.md)
- [- hardwareFormatChanged](ioaudiostream/1580044-hardwareformatchanged.md)
- [- initWithAudioEngine](ioaudiostream/1580064-initwithaudioengine.md)
- [- lockStreamForIO](ioaudiostream/1580035-lockstreamforio.md)
- [- mixOutputSamples](ioaudiostream/1580043-mixoutputsamples.md)
- [- numSampleFramesPerBufferChanged](ioaudiostream/1580030-numsampleframesperbufferchanged.md)
- [- processOutputSamples](ioaudiostream/1580041-processoutputsamples.md)
- [- readInputSamples](ioaudiostream/1580045-readinputsamples.md)
- [- removeClient](ioaudiostream/1580057-removeclient.md)
- [- removeDefaultAudioControls](ioaudiostream/1580034-removedefaultaudiocontrols.md)
- [- resetClipInfo](ioaudiostream/1580053-resetclipinfo.md)
- [- safeLogError](ioaudiostream/1580047-safelogerror.md)
- [- setDefaultNumSampleFramesRead](ioaudiostream/1580062-setdefaultnumsampleframesread.md)
- [- setDirection](ioaudiostream/1580060-setdirection.md)
- [- setFormat](ioaudiostream/1580046-setformat.md)
- [- setFormat](ioaudiostream/3516534-setformat.md)
- [- setFormat](ioaudiostream/3516535-setformat.md)
- [- setFormat](ioaudiostream/3516536-setformat.md)
- [- setFormat](ioaudiostream/3516537-setformat.md)
- [- setIOFunction](ioaudiostream/1580033-setiofunction.md)
- [- setIOFunctionList](ioaudiostream/1580026-setiofunctionlist.md)
- [- setMixBuffer](ioaudiostream/1580065-setmixbuffer.md)
- [- setProperties](ioaudiostream/1580042-setproperties.md)
- [- setSampleBuffer](ioaudiostream/1580036-setsamplebuffer.md)
- [- setSampleLatency](ioaudiostream/1580055-setsamplelatency.md)
- [- setStartingChannelNumber](ioaudiostream/1580052-setstartingchannelnumber.md)
- [- setStreamAvailable](ioaudiostream/1580038-setstreamavailable.md)
- [- setTerminalType](ioaudiostream/1580066-setterminaltype.md)
- [- stop](ioaudiostream/1580017-stop.md)
- [- unlockStreamForIO](ioaudiostream/1580020-unlockstreamforio.md)
- [- updateNumClients](ioaudiostream/1580029-updatenumclients.md)
- [- validateFormat](ioaudiostream/1580059-validateformat.md)
- [- validateFormat](ioaudiostream/3516538-validateformat.md)
- [- validateFormat](ioaudiostream/3516539-validateformat.md)
### Type Methods
- [+ createDictionaryFromFormat](ioaudiostream/1580027-createdictionaryfromformat.md)
- [+ createFormatFromDictionary](ioaudiostream/1580025-createformatfromdictionary.md)
- [+ initKeys](ioaudiostream/1580067-initkeys.md)
- [+ setFormatAction](ioaudiostream/1580031-setformataction.md)

## Relationships

### Inherits From
- [IOService](ioservice.md)

## See Also

- [IOAudioLevelControl](ioaudiolevelcontrol.md)
- [IOAudioSelectorControl](ioaudioselectorcontrol.md)
- [IOAudioToggleControl](ioaudiotogglecontrol.md)
- [IOAudioControl](ioaudiocontrol.md)
  Represents any controllable attribute of an IOAudioDevice.
- [IOAudioEngine](ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioPort](ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiostream)*