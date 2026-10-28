# SpeakString

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

Begins speaking a text string.

**Availability**:
- macOS 10.0+ - Deprecated in 10.8

## Declaration

```c
OSErr SpeakString(ConstStr255Param textToBeSpoken);
```

## Return Value

A resultcode. See [Result Codes](./speech_synthesis_manager.md#1659745).

## Discussion

The `SpeakString` functionattempts to speak the Pascal-style text string contained in the string `textToBeSpoken`.Speech is produced asynchronously using the default system voice.When an application calls this function, the Speech Synthesis Managermakes a copy of the passed string and creates any structures requiredto speak it. As soon as speaking has begun, control is returnedto the application. The synthesized speech is generated asynchronously tothe application so that normal processing can continue while thetext is being spoken. No further interaction with the Speech SynthesisManager is required at this point, and the application is free torelease the memory that the original string occupied.

If `SpeakString` iscalled while a prior string is still being spoken, the sound currentlybeing synthesized is interrupted immediately. Conversion of thenew text into speech is then begun. If you pass a zero-length string(or, in C, a `null` pointer)to `SpeakString`, the Speech SynthesisManager stops any speech previously being synthesized by `SpeakString` without generatingadditional speech. If your application uses `SpeakString`,it is often a good idea to stop any speech in progress wheneveryour application receives a suspend event. Calling `SpeakString` witha zero-length string has no effect on speech channels other than theone managed internally by the Speech Synthesis Manager for the `SpeakString` function.)

The text passed to the `SpeakString` functionmay contain embedded speech commands. 

## Parameters

- `textToBeSpoken`: The string to be spoken.

## See Also

### Starting, Stopping, and Pausing Speech
- [ContinueSpeech](./api-1462728-continuespeech.md)
  Resumes speech paused by the `PauseSpeechAt` function.
- [PauseSpeechAt](./api-1461174-pausespeechat.md)
  Pauses speech on a speech channel.
- [SpeakBuffer](./api-1552252-speakbuffer.md)
  Speaks a buffer of text, using certain flags to controlspeech behavior.
- [SpeakCFString](./api-1461621-speakcfstring.md)
  Begins speaking a string represented as a `CFString` object.
- [SpeakText](./api-1552236-speaktext.md)
  Begins speaking a buffer of text.
- [StopSpeech](./api-1462745-stopspeech.md)
  Terminates speech immediately on the specified channel.
- [StopSpeechAt](./api-1459780-stopspeechat.md)
  Terminates speech delivery on a specified channel eitherimmediately or at the end of the current word or sentence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1552250-speakstring)*