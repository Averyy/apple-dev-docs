# IOAudioFlush

**Framework**: IOKit  
**Kind**: func

Indicate the position at which the audio stream can be stopped.

## Declaration

```c
kern_return_t IOAudioFlush(
   io_connect_t connect,
   IOAudioStreamPosition *end);
```

## Return Value

kern_return_t

## Parameters

- `connect`: the audio stream
- `end`: the position

## See Also

### Miscellaneous
- [IOAudioIsOutput](./api-1812070-ioaudioisoutput.md)
  Determines if the audio stream is an output stream
- [IOAudioSetErase](./api-1812074-ioaudioseterase.md)
  Set autoerase flag, returns old value


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudiolib_h/1812066-ioaudioflush)*