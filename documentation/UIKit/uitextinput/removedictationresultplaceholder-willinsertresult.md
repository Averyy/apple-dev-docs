# removeDictationResultPlaceholder(_:willInsertResult:)

**Framework**: UIKit  
**Kind**: method

Tells the view that the specified placeholder object is unnecessary.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
optional func removeDictationResultPlaceholder(_ placeholder: Any, willInsertResult: Bool)
```

#### Discussion

If the value in the `willInsertResult` parameter is [`false`](https://developer.apple.com/documentation/swift/false), the placeholder animation is not replaced by an actual dictation result. When this happens, the system still removes the placeholder animation and removes the strong reference to your placeholder object.

> ❗ **Important**:  This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](uitextinput/dictationrecordingdidend().md) and [`dictationRecognitionFailed()`](uitextinput/dictationrecognitionfailed().md) to implement a custom placeholder.

 This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](uitextinput/dictationrecordingdidend().md) and [`dictationRecognitionFailed()`](uitextinput/dictationrecognitionfailed().md) to implement a custom placeholder.

## Parameters

- `placeholder`: The placeholder object that is no longer needed.
- `willInsertResult`: The value of this parameter is   if the dictation value was generated successfully or   if an error occurred.

## See Also

- [func dictationRecordingDidEnd()](uitextinput/dictationrecordingdidend.md)
  Tells the object when there is a pending dictation result.
- [func dictationRecognitionFailed()](uitextinput/dictationrecognitionfailed.md)
  Tells the object when dictation ends, but recognition fails.
- [func insertDictationResult([UIDictationPhrase])](uitextinput/insertdictationresult(_:).md)
  Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [var insertDictationResultPlaceholder: Any](uitextinput/insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](uitextinput/frame(fordictationresultplaceholder:).md)
  Asks for the rectangle for displaying the dictation placeholder animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/removedictationresultplaceholder(_:willinsertresult:))*