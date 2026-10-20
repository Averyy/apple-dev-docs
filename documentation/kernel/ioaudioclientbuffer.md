# IOAudioClientBuffer

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.1+

## Declaration

```c
typedef struct IOAudioClientBuffer {
    ...
} IOAudioClientBuffer;
```

## Topics

### Instance Properties
- [audioStream](./ioaudioclientbuffer/api-1495580-audiostream.md)
- [bufferDataDescriptor](./ioaudioclientbuffer/api-1495548-bufferdatadescriptor.md)
- [mNextBuffer32](./ioaudioclientbuffer/api-1495554-mnextbuffer32.md)
- [mixedPosition](./ioaudioclientbuffer/api-1495542-mixedposition.md)
- [nextClient](./ioaudioclientbuffer/api-1495566-nextclient.md)
- [nextClip](./ioaudioclientbuffer/api-1495538-nextclip.md)
- [numChannels](./ioaudioclientbuffer/api-1495616-numchannels.md)
- [numSampleFrames](./ioaudioclientbuffer/api-1495588-numsampleframes.md)
- [previousClip](./ioaudioclientbuffer/api-1495528-previousclip.md)
- [sourceBuffer](./ioaudioclientbuffer/api-1495481-sourcebuffer.md)
- [sourceBufferDescriptor](./ioaudioclientbuffer/api-1495500-sourcebufferdescriptor.md)
- [sourceBufferMap](./ioaudioclientbuffer/api-1495505-sourcebuffermap.md)
- [unmappedSourceBuffer](./ioaudioclientbuffer/api-1495562-unmappedsourcebuffer.md)
- [userClient](./ioaudioclientbuffer/api-1495511-userclient.md)

## See Also

### Audio Data
- [IOAudioEngineNotifications](./ioaudioenginenotifications.md)
- [IOAudioEngineTraps](./ioaudioenginetraps.md)
- [IOAudioSampleRate](./ioaudiosamplerate.md)
- [IOAudioStreamFormat](./ioaudiostreamformat.md)
- [IOAudioStreamFormatExtension](./ioaudiostreamformatextension.md)
- [IOAudioTimeStamp](./ioaudiotimestamp.md)
- [IOAudioClientBuffer64](./ioaudioclientbuffer64.md)
- [IOAudioClientBufferExtendedInfo](./ioaudioclientbufferextendedinfo.md)
- [IOAudioClientBufferExtendedInfo64](./ioaudioclientbufferextendedinfo64.md)
- [IOAudioEnginePosition](./ioaudioengineposition.md)
  Represents a position in an audio audio engine.
- [IOAF_bcopy_WriteCombine](./api-1416189-ioaf_bcopy_writecombine.md)
  An efficient bcopy from "write combine" memory to regular memory. It is safe to assume that all memory has been copied when the function has completed
- [UInt64mult](./api-1402722-uint64mult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioclientbuffer)*