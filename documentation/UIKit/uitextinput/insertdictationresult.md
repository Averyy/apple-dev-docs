# insertDictationResult(_:)

**Framework**: UIKit  
**Kind**: method

Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.

**Availability**:
- iOS 5.1+
- iPadOS 5.1+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])
```

#### Discussion

Implement this optional method if you want to support dictation phrase alternatives. If you do not implement this method, iOS inserts the most likely interpretation of the dictated phrase.

> ❗ **Important**:  This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](uitextinput/dictationrecordingdidend().md) and [`dictationRecognitionFailed()`](uitextinput/dictationrecognitionfailed().md) to implement a custom placeholder.

## Parameters

- `dictationResult`: An array of   objects.

## See Also

- [func dictationRecordingDidEnd()](uitextinput/dictationrecordingdidend.md)
  Tells the object when there is a pending dictation result.
- [func dictationRecognitionFailed()](uitextinput/dictationrecognitionfailed.md)
  Tells the object when dictation ends, but recognition fails.
- [var insertDictationResultPlaceholder: Any](uitextinput/insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](uitextinput/frame(fordictationresultplaceholder:).md)
  Asks for the rectangle for displaying the dictation placeholder animation.
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](uitextinput/removedictationresultplaceholder(_:willinsertresult:).md)
  Tells the view that the specified placeholder object is unnecessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/insertdictationresult(_:))*