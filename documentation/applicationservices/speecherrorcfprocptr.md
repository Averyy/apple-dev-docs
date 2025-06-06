# SpeechErrorCFProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to an error callback function that handles syntax errors within commands embedded in a `CFString` object being processed by the Speech Synthesis Manager.

**Availability**:
- macOS 10.5+

## Declaration

```swift
typealias SpeechErrorCFProcPtr = (SpeechChannel, SRefCon, CFError) -> Void
```

#### Discussion

An error callback function defined by the `SpeechErrorCFProcPtr` is the Core Foundation-based equivalent of an error callback function defined by [`SpeechErrorProcPtr`](speecherrorprocptr.md). The Speech Synthesis Manager calls a speech channel’s error callback function whenever it encounters a syntax error within a command embedded in a `CFString` object it is processing. This can be useful during application debugging, to detect problems with commands that you have embedded in strings that your application speaks. It can also be useful if your application allows users to embed commands within strings. Your application might display an alert indicating that the Speech Synthesis Manager encountered a problem in processing an embedded command.

Ordinarily, the error information that the Speech Synthesis Manager provides the error callback function should be sufficient. However, if your application needs information about errors that occurred before the error callback function was enabled, the application (including the error callback function) can call the [`CopySpeechProperty(_:_:_:)`](1459075-copyspeechproperty.md) function with the `kSpeechErrorsProperty` property.

You can specify an error callback function by passing the `kSpeechErrorCFCallback` property to the [`SetSpeechProperty(_:_:_:)`](1459256-setspeechproperty.md) function. 

## Parameters

- `chan`: The speech channel that has finished processing input text.
- `refCon`: The reference constant associated with the speech channel. 
- `theError`: The error that occurred in processing an embedded command.

## See Also

- [typealias SpeechDoneProcPtr](speechdoneprocptr.md)
  Defines a pointer to a speech-done callback functionwhich is called when the Speech Synthesis Manager finishes speakinga buffer of text.
- [typealias SpeechErrorProcPtr](speecherrorprocptr.md)
  Defines a pointer to an error callback functionthat handles syntax errors within commands embedded in a text bufferbeing processed by the Speech Synthesis Manager.
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speecherrorcfprocptr)*