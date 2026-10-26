# SpeakText

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Begins speaking a buffer of text.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr SpeakText(SpeechChannel chan, const void *textBuf, unsigned long textBytes);
```

#### Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

#### Discussion

Like `SpeakString`,the `SpeakText` functionalso generates speech, but through a speech channel through whichyou can exert control over the generated speech.

The `SpeakText` functionconverts the text stream specified by the `textBuf` and `textBytes` parametersinto speech using the voice and control settings for the speechchannel `chan`, which shouldbe created with the `NewSpeechChannel` function.The speech is generated asynchronously. This means that controlis returned to your application before the speech has finished (andprobably even before it has begun). The maximum length of the text bufferthat can be spoken is limited only by the available RAM.

If `SpeakText` iscalled while the channel is currently busy speaking the contentsof a prior text buffer, it immediately stops speaking from the priorbuffer and begins speaking from the new text buffer as soon as possible.If you pass a zero-length string (or, in C, a `null` pointer)to `SpeakText`, the SpeechSynthesis Manager stops all speech currently being synthesized bythe speech channel specified in the `chan` parameterwithout generating additional speech.

The text buffer must be locked in memory and must not movewhile the Speech Synthesis Manager processes it. This buffer isread at interrupt time, and moving it could cause a system crash.If your application defines a text-done callback function, thenit can move the text buffer or dispose of it once the callback functionis executed. 

## Parameters

- `chan`: The speech channel through which speech is to be spoken.
- `textBuf`: A pointer to the first byte of text to spoken. 
- `textBytes`: The number of bytes of text to spoken. 

## See Also

### Starting, Stopping, and Pausing Speech
- [ContinueSpeech](./api-1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [PauseSpeechAt](./api-1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [SpeakBuffer](./api-1552252-speakbuffer.md)
  Speaks a buffer of text, using certain flags to controlspeech behavior.
- [SpeakString](./api-1552250-speakstring.md)
  Begins speaking a text string.
- [SpeakCFString](./api-1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [StopSpeech](./api-1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [StopSpeechAt](./api-1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552236-speaktext)*