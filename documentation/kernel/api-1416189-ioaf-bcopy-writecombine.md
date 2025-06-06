# IOAF_bcopy_WriteCombine

**Framework**: Kernel  
**Kind**: func

An efficient bcopy from "write combine" memory to regular memory. It is safe to assume that all memory has been copied when the function has completed

**Availability**:
- macOS 10.7+

## Declaration

```swift
void IOAF_bcopy_WriteCombine(const void *src, void *dest, unsigned int count);
```

## Parameters

- `src`: Pointer to the data to convert
- `dest`: Pointer to the converted data
- `count`: The number of items to convert

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
- [IOAudioEnginePosition](ioaudioengineposition.md)
  Represents a position in an audio audio engine.
- [UInt64mult](1402722-uint64mult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1416189-ioaf_bcopy_writecombine)*