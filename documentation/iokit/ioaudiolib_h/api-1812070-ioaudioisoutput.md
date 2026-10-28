# IOAudioIsOutput

**Framework**: IOKit  
**Kind**: func

Determines if the audio stream is an output stream

## Declaration

```c
kern_return_t IOAudioIsOutput(
   io_service_t service,
   int *out);
```

## Return Value

kern_return_t

## Parameters

- `service`: 
- `out`: 

## See Also

### Miscellaneous
- [IOAudioFlush](./api-1812066-ioaudioflush.md)
  Indicate the position at which the audio stream can be stopped.
- [IOAudioSetErase](./api-1812074-ioaudioseterase.md)
  Set autoerase flag, returns old value


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudiolib_h/1812070-ioaudioisoutput)*