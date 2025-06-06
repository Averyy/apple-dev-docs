# SpeechDoneProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to a speech-done callback functionwhich is called when the Speech Synthesis Manager finishes speakinga buffer of text.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias SpeechDoneProcPtr = (SpeechChannel, SRefCon) -> Void
```

#### Discussion

If a speech-done callback function is installed in a speechchannel, then the Speech Synthesis Manager calls this function whenit finishes speaking a buffer of text.

You can specify a speech-done callback function by passingthe `soSpeechDoneCallBack` selectorto the `SetSpeechInfo` function.

You might use a speech-done callback function if you needto update some visual indicator that shows what text is currentlybeing spoken. For example, suppose your application passes textbuffers to the Speech Synthesis Manager one paragraph at a time.Your speech-done callback function might set a global flag variableto indicate to the application that the Speech Synthesis Managerhas finished speaking a paragraph. When a function called by yourapplication’s main event loop checks the global flag variableand determines that it has been set, the function might ensure thatthe next paragraph of text is visible.

You might use a speech-done callback function to set a flagvariable that alerts the application that it should pass a new bufferof text to the Speech Synthesis Manager. If you do so, however,there might be a noticeable pause as the Speech Synthesis Manager switchesfrom processing one text buffer to another. Ordinarily, it is easierto achieve this goal by using a text-done callback function, asdescribed earlier. 

## Parameters

- `chan`: The speech channel that has finished processing input text.
- `refCon`: The reference constant associated with the speech channel. 

## See Also

- [typealias SpeechErrorProcPtr](speecherrorprocptr.md)
  Defines a pointer to an error callback functionthat handles syntax errors within commands embedded in a text bufferbeing processed by the Speech Synthesis Manager.
- [typealias SpeechErrorCFProcPtr](speecherrorcfprocptr.md)
  Defines a pointer to an error callback function that handles syntax errors within commands embedded in a `CFString` object being processed by the Speech Synthesis Manager.
- [typealias SpeechPhonemeProcPtr](speechphonemeprocptr.md)
  Defines a pointer to a phoneme callback functionthat is called by the Speech Synthesis Manager before it pronouncesa phoneme.
- [typealias SpeechSyncProcPtr](speechsyncprocptr.md)
  Defines a pointer to a synchronization callbackfunction that is called when the Speech Synthesis Manager encountersa synchronization command embedded in a text buffer.
- [typealias SpeechTextDoneProcPtr](speechtextdoneprocptr.md)
  Defines a pointer to a text-done callback functionthat is called when the Speech Synthesis Manager has finished processinga buffer of text.
- [typealias SpeechWordProcPtr](speechwordprocptr.md)
  Defines a pointer to a word callback functionthat is called by the Speech Synthesis Manager before it pronouncesa word.
- [typealias SpeechWordCFProcPtr](speechwordcfprocptr.md)
  Defines a pointer to a Core Foundation-based word callback function that is called by the Speech Synthesis Manager before it pronounces a word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechdoneprocptr)*