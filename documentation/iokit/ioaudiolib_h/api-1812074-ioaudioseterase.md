# IOAudioSetErase

**Framework**: IOKit  
**Kind**: func

Set autoerase flag, returns old value

## Declaration

```c
kern_return_t IOAudioSetErase(
   io_connect_t connect,
   int erase,
   int *oldVal);
```

#### Return Value

kern_return_t

## Parameters

- `connect`: the audio stream
- `erase`: true to turn off, false otherwise
- `oldVal`: previous value

## See Also

### Miscellaneous
- [IOAudioFlush](./api-1812066-ioaudioflush.md)
  Indicate the position at which the audio stream can be stopped.
- [IOAudioIsOutput](./api-1812070-ioaudioisoutput.md)
  Determines if the audio stream is an output stream


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/ioaudiolib_h/1812074-ioaudioseterase)*