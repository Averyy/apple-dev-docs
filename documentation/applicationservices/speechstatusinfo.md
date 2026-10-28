# SpeechStatusInfo

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Defines a speech status information structure, which stores information about the status of a speech channel.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SpeechStatusInfo
```

```c
typedef struct SpeechStatusInfo {
    ...
} SpeechStatusInfo;
```

## Overview

By calling the [`GetSpeechInfo`](./api-1552220-getspeechinfo.md) function with the `soStatus` selector, you can find out information about the status of a speech channel.

## Topics

### Initializers
- [init()](./speechstatusinfo/api-1463999-init.md)
- [init(outputBusy: DarwinBoolean, outputPaused: DarwinBoolean, inputBytesLeft: Int, phonemeCode: Int16)](./speechstatusinfo/api-1463725-init.md)
### Instance Properties
- [var inputBytesLeft: Int](./speechstatusinfo/api-1461214-inputbytesleft.md)
  The number of input bytes of the text that the speech channel must still process. When `inputBytesLeft` is 0, the buffer of input text passed to one of the `SpeakText` or `SpeakBuffer` functions may be disposed of. When you call the `SpeakString` function, the Speech Synthesis Manager stores a duplicate of the string to be spoken in an internal buffer; thus, you may delete the original string immediately after calling `SpeakString`.
- [var outputBusy: DarwinBoolean](./speechstatusinfo/api-1459111-outputbusy.md)
  Whether the speech channel is currently producing speech. A speech channel is considered to be producing speech even at some times when no audio data is being produced through the Macintosh speaker. This occurs, for example, when the Speech Synthesis Manager is processing an input buffer but has not yet initiated speech or when speech output is paused.
- [var outputPaused: DarwinBoolean](./speechstatusinfo/api-1460606-outputpaused.md)
  Whether speech output in the speech channel has been paused by a call to the [`PauseSpeechAt(_:_:)`](./api-1461174-pausespeechat.md) function.
- [var phonemeCode: Int16](./speechstatusinfo/api-1461423-phonemecode.md)
  The opcode for the phoneme that the speech channel is currently processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechstatusinfo)*