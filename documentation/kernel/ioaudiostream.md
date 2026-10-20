# IOAudioStream

**Framework**: Kernel  
**Kind**: cl  
**Role**: Class

This class wraps a single sample buffer in an audio driver.

**Availability**:
- macOS 10.1+

## Declaration

```cpp
class IOAudioStream : IOService
```

#### Overview

An IOAudioStream represents one hardware sample buffer as well as the direction of that buffer, the mix buffer that multiple clients mix into as well as a list of all of the formats to which this buffer can be set.

When an IOAudioEngine is created during init time in the driver, an IOAudioStream must be created for each sample buffer in the device. Typically, the sample buffer will be interleaved (or single channel), as a non-interleaved buffer should be divided into multiple single-channel buffers (and multiple IOAudioStreams).

Additionally, when an IOAudioStream is created it must have all of the possible formats (and allowed sample rates for each format) set and must have the currently set format specified (addAvailableFormat() and setFormat()).

## Topics

### Instance Methods
- [- addAvailableFormat](./ioaudiostream/api-1580021-addavailableformat.md)
- [- addAvailableFormat](./ioaudiostream/api-3516531-addavailableformat.md)
- [- addAvailableFormat](./ioaudiostream/api-3516532-addavailableformat.md)
- [- addAvailableFormat](./ioaudiostream/api-3516533-addavailableformat.md)
- [- addClient](./ioaudiostream/api-1580015-addclient.md)
- [- addDefaultAudioControl](./ioaudiostream/api-1580039-adddefaultaudiocontrol.md)
- [- clearAvailableFormats](./ioaudiostream/api-1580032-clearavailableformats.md)
- [- clearSampleBuffer](./ioaudiostream/api-1580056-clearsamplebuffer.md)
- [- clipIfNecessary](./ioaudiostream/api-1580058-clipifnecessary.md)
- [- clipOutputSamples](./ioaudiostream/api-1580040-clipoutputsamples.md)
- [- free](./ioaudiostream/api-1580016-free.md)
- [- getDirection](./ioaudiostream/api-1580048-getdirection.md)
- [- getFormat](./ioaudiostream/api-1580050-getformat.md)
- [- getFormatExtension](./ioaudiostream/api-1580019-getformatextension.md)
- [- getMaxNumChannels](./ioaudiostream/api-1580049-getmaxnumchannels.md)
- [- getMetaClass](./ioaudiostream/api-1580051-getmetaclass.md)
- [- getMixBuffer](./ioaudiostream/api-1580037-getmixbuffer.md)
- [- getMixBufferSize](./ioaudiostream/api-1580063-getmixbuffersize.md)
- [- getNumClients](./ioaudiostream/api-1580054-getnumclients.md)
- [- getNumSampleFramesRead](./ioaudiostream/api-1580061-getnumsampleframesread.md)
- [- getSampleBuffer](./ioaudiostream/api-1580022-getsamplebuffer.md)
- [- getSampleBufferSize](./ioaudiostream/api-1580028-getsamplebuffersize.md)
- [- getStartingChannelID](./ioaudiostream/api-1580018-getstartingchannelid.md)
- [- getStreamAvailable](./ioaudiostream/api-1580024-getstreamavailable.md)
- [- getWorkLoop](./ioaudiostream/api-1580023-getworkloop.md)
- [- hardwareFormatChanged](./ioaudiostream/api-1580044-hardwareformatchanged.md)
- [- initWithAudioEngine](./ioaudiostream/api-1580064-initwithaudioengine.md)
- [- lockStreamForIO](./ioaudiostream/api-1580035-lockstreamforio.md)
- [- mixOutputSamples](./ioaudiostream/api-1580043-mixoutputsamples.md)
- [- numSampleFramesPerBufferChanged](./ioaudiostream/api-1580030-numsampleframesperbufferchanged.md)
- [- processOutputSamples](./ioaudiostream/api-1580041-processoutputsamples.md)
- [- readInputSamples](./ioaudiostream/api-1580045-readinputsamples.md)
- [- removeClient](./ioaudiostream/api-1580057-removeclient.md)
- [- removeDefaultAudioControls](./ioaudiostream/api-1580034-removedefaultaudiocontrols.md)
- [- resetClipInfo](./ioaudiostream/api-1580053-resetclipinfo.md)
- [- safeLogError](./ioaudiostream/api-1580047-safelogerror.md)
- [- setDefaultNumSampleFramesRead](./ioaudiostream/api-1580062-setdefaultnumsampleframesread.md)
- [- setDirection](./ioaudiostream/api-1580060-setdirection.md)
- [- setFormat](./ioaudiostream/api-1580046-setformat.md)
- [- setFormat](./ioaudiostream/api-3516534-setformat.md)
- [- setFormat](./ioaudiostream/api-3516535-setformat.md)
- [- setFormat](./ioaudiostream/api-3516536-setformat.md)
- [- setFormat](./ioaudiostream/api-3516537-setformat.md)
- [- setIOFunction](./ioaudiostream/api-1580033-setiofunction.md)
- [- setIOFunctionList](./ioaudiostream/api-1580026-setiofunctionlist.md)
- [- setMixBuffer](./ioaudiostream/api-1580065-setmixbuffer.md)
- [- setProperties](./ioaudiostream/api-1580042-setproperties.md)
- [- setSampleBuffer](./ioaudiostream/api-1580036-setsamplebuffer.md)
- [- setSampleLatency](./ioaudiostream/api-1580055-setsamplelatency.md)
- [- setStartingChannelNumber](./ioaudiostream/api-1580052-setstartingchannelnumber.md)
- [- setStreamAvailable](./ioaudiostream/api-1580038-setstreamavailable.md)
- [- setTerminalType](./ioaudiostream/api-1580066-setterminaltype.md)
- [- stop](./ioaudiostream/api-1580017-stop.md)
- [- unlockStreamForIO](./ioaudiostream/api-1580020-unlockstreamforio.md)
- [- updateNumClients](./ioaudiostream/api-1580029-updatenumclients.md)
- [- validateFormat](./ioaudiostream/api-1580059-validateformat.md)
- [- validateFormat](./ioaudiostream/api-3516538-validateformat.md)
- [- validateFormat](./ioaudiostream/api-3516539-validateformat.md)
### Type Methods
- [+ createDictionaryFromFormat](./ioaudiostream/api-1580027-createdictionaryfromformat.md)
- [+ createFormatFromDictionary](./ioaudiostream/api-1580025-createformatfromdictionary.md)
- [+ initKeys](./ioaudiostream/api-1580067-initkeys.md)
- [+ setFormatAction](./ioaudiostream/api-1580031-setformataction.md)

## Relationships

### Inherits From
- [IOService](./ioservice.md)

## See Also

### Interfaces
- [IOAudioLevelControl](./ioaudiolevelcontrol.md)
- [IOAudioSelectorControl](./ioaudioselectorcontrol.md)
- [IOAudioToggleControl](./ioaudiotogglecontrol.md)
- [IOAudioControl](./ioaudiocontrol.md)
  Represents any controllable attribute of an IOAudioDevice.
- [IOAudioEngine](./ioaudioengine.md)
  Abstract base class for a single audio audio / I/O engine.
- [IOAudioPort](./ioaudioport.md)
  Represents a logical or physical port or functional unit in an audio device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudiostream)*