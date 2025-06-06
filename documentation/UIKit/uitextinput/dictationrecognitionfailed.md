# dictationRecognitionFailed()

**Framework**: UIKit  
**Kind**: method

Tells the object when dictation ends, but recognition fails.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func dictationRecognitionFailed()
```

#### Discussion

Implement this optional method if you want to respond to failed dictation recognition.

## See Also

- [func dictationRecordingDidEnd()](uitextinput/dictationrecordingdidend.md)
  Tells the object when there is a pending dictation result.
- [func insertDictationResult([UIDictationPhrase])](uitextinput/insertdictationresult(_:).md)
  Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [var insertDictationResultPlaceholder: Any](uitextinput/insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](uitextinput/frame(fordictationresultplaceholder:).md)
  Asks for the rectangle for displaying the dictation placeholder animation.
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](uitextinput/removedictationresultplaceholder(_:willinsertresult:).md)
  Tells the view that the specified placeholder object is unnecessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/dictationrecognitionfailed())*