# dictationRecognitionFailed()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the object when dictation ends, but recognition fails.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func dictationRecognitionFailed()
```

```objc
- (void) dictationRecognitionFailed;
```

## Discussion

Implement this optional method if you want to respond to failed dictation recognition.

## See Also

### Using dictation
- [func dictationRecordingDidEnd()](./dictationrecordingdidend%28%29.md)
  Tells the object when there is a pending dictation result.
- [func insertDictationResult([UIDictationPhrase])](./insertdictationresult%28_%29.md)
  Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [var insertDictationResultPlaceholder: Any](./insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](./frame%28fordictationresultplaceholder%29.md)
  Asks for the rectangle for displaying the dictation placeholder animation.
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](./removedictationresultplaceholder%28_,willinsertresult%29.md)
  Tells the view that the specified placeholder object is unnecessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/dictationrecognitionfailed())*