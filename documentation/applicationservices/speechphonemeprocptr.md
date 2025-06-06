# SpeechPhonemeProcPtr

**Framework**: Application Services  
**Kind**: tdef

Defines a pointer to a phoneme callback functionthat is called by the Speech Synthesis Manager before it pronouncesa phoneme.

**Availability**:
- macOS 10.0+

## Declaration

```swift
typealias SpeechPhonemeProcPtr = (SpeechChannel, SRefCon, Int16) -> Void
```

#### Discussion

The Speech Synthesis Manager calls a speech channel’s phonemecallback function just before it pronounces a phoneme. For example,your application might use such a callback function to enable mouthsynchronization. In this case, the callback function would set a globalflag variable to indicate that the phoneme being pronounced is changingand another global variable to `phonemeOpcode`.A function called by your application’s main event loop coulddetect that the phoneme being pronounced is changing and updatea picture of a mouth to reflect the current phoneme. In practice,providing a visual indication of the pronunciation of a phonemerequires several consecutive pictures of mouth movement to be rapidlydisplayed. Consult the linguistics literature for information on mouthmovements associated with different phonemes.

You can specify a phoneme callback function by passing the `soPhonemeCallBack` selectorto the `SetSpeechInfo` function. 

## Parameters

- `chan`: The speech channel that has finished processing input text.
- `refCon`: The reference constant associated with the speech channel. 
- `phonemeOpcode`: The phoneme about to be pronounced. 

## See Also

- [typealias SpeechDoneProcPtr](speechdoneprocptr.md)
  Defines a pointer to a speech-done callback functionwhich is called when the Speech Synthesis Manager finishes speakinga buffer of text.
- [typealias SpeechErrorProcPtr](speecherrorprocptr.md)
  Defines a pointer to an error callback functionthat handles syntax errors within commands embedded in a text bufferbeing processed by the Speech Synthesis Manager.
- [typealias SpeechErrorCFProcPtr](speecherrorcfprocptr.md)
  Defines a pointer to an error callback function that handles syntax errors within commands embedded in a `CFString` object being processed by the Speech Synthesis Manager.
- [typealias SpeechSyncProcPtr](speechsyncprocptr.md)
  Defines a pointer to a synchronization callbackfunction that is called when the Speech Synthesis Manager encountersa synchronization command embedded in a text buffer.
- [typealias SpeechTextDoneProcPtr](speechtextdoneprocptr.md)
  Defines a pointer to a text-done callback functionthat is called when the Speech Synthesis Manager has finished processinga buffer of text.
- [typealias SpeechWordProcPtr](speechwordprocptr.md)
  Defines a pointer to a word callback functionthat is called by the Speech Synthesis Manager before it pronouncesa word.
- [typealias SpeechWordCFProcPtr](speechwordcfprocptr.md)
  Defines a pointer to a Core Foundation-based word callback function that is called by the Speech Synthesis Manager before it pronounces a word.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/speechphonemeprocptr)*