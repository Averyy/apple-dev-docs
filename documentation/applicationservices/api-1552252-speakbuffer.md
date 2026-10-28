# SpeakBuffer

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Speaks a buffer of text, using certain flags to controlspeech behavior.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr SpeakBuffer(SpeechChannel chan, const void *textBuf, unsigned long textBytes, SInt32 controlFlags);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

The `SpeakBuffer` functionbehaves identically to the `SpeakText` function,but allows control of several speech parameters by setting valuesof the `controlFlags` parameter.The `controlFlags` parameterrelies on specific constants, which may be applied additively. See [Control Flags Constants](./api-1552213-control_flags_constants.md).

Each constant specifies a flag bit of the `controlFlags` parameter,so by passing the constants additively you can enable multiple capabilitiesof `SpeakBuffer`. If youpass `0` in the `controlFlags` parameter, `SpeakBuffer` worksjust like `SpeakText`.By passing `kNoEndingProsody + kNoSpeechInterrupt` inthe `controlFlags` parameter, `SpeakBuffer` workslike `SpeakText` exceptthat the `kNoEndingProsody` and `kNoSpeechInterrupt` features havebeen selected. Future versions of the Speech Synthesis Manager maydefine additional constants. 

When the `controlFlags` parameteris set to `0`, `SpeakBuffer` behavesidentically to `SpeakText`. 

## Parameters

- `chan`: The speech channel through which speech is to be spoken.
- `textBuf`: A pointer to the first byte of text to spoken. 
- `textBytes`: The number of bytes of text to spoken. 
- `controlFlags`: Control flags to customize speech behavior. 

## See Also

### Starting, Stopping, and Pausing Speech
- [ContinueSpeech](./api-1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [PauseSpeechAt](./api-1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [SpeakString](./api-1552250-speakstring.md)
  Begins speaking a text string.
- [SpeakCFString](./api-1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [SpeakText](./api-1552236-speaktext.md)
  Begins speaking a buffer of text.
- [StopSpeech](./api-1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [StopSpeechAt](./api-1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552252-speakbuffer)*