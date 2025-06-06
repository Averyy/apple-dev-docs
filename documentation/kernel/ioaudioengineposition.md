# IOAudioEnginePosition

**Framework**: Kernel  
**Kind**: struct

Represents a position in an audio audio engine.

**Availability**:
- macOS 10.1+

## Declaration

```swift
typedef struct IOAudioEnginePosition {
    ...
} IOAudioEnginePosition;
```

#### Overview

This position is based on the sample frame within a loop around the sample buffer, and the loop count which starts at 0 when the audio engine begins playback.

## Topics

### Instance Properties
- [fLoopCount](ioaudioengineposition/1561645-floopcount.md)
- [fSampleFrame](ioaudioengineposition/1561650-fsampleframe.md)

## See Also

- [IOAudioEngineNotifications](ioaudioenginenotifications.md)
- [IOAudioEngineTraps](ioaudioenginetraps.md)
- [IOAudioSampleRate](ioaudiosamplerate.md)
- [IOAudioStreamFormat](ioaudiostreamformat.md)
- [IOAudioStreamFormatExtension](ioaudiostreamformatextension.md)
- [IOAudioTimeStamp](ioaudiotimestamp.md)
- [IOAudioClientBuffer](ioaudioclientbuffer.md)
- [IOAudioClientBuffer64](ioaudioclientbuffer64.md)
- [IOAudioClientBufferExtendedInfo](ioaudioclientbufferextendedinfo.md)
- [IOAudioClientBufferExtendedInfo64](ioaudioclientbufferextendedinfo64.md)
- [IOAF_bcopy_WriteCombine](1416189-ioaf_bcopy_writecombine.md)
  An efficient bcopy from "write combine" memory to regular memory. It is safe to assume that all memory has been copied when the function has completed
- [UInt64mult](1402722-uint64mult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioengineposition)*