# IOAudioEngineMemory

**Framework**: Kernel  
**Kind**: tdef  
**Role**: Type Alias

Used to identify the type of memory requested by a client process to be mapped into its process space

**Availability**:
- macOS 10.1+

## Declaration

```c
typedef enum _IOAudioEngineMemory IOAudioEngineMemory;
```

#### Discussion

This is the parameter to the type field of IOMapMemory when called on an IOAudioEngine. This is only intended for use by the Audio Device API library.

## Topics

### Constants
- [kIOAudioSampleBuffer](./ioaudioenginememory/kioaudiosamplebuffer.md)
- [kIOAudioStatusBuffer](./ioaudioenginememory/kioaudiostatusbuffer.md)
- [kIOAudioMixBuffer](./ioaudioenginememory/kioaudiomixbuffer.md)
- [kIOAudioBytesInInputBuffer](./ioaudioenginememory/kioaudiobytesininputbuffer.md)
- [kIOAudioBytesInOutputBuffer](./ioaudioenginememory/kioaudiobytesinoutputbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioaudioenginememory)*