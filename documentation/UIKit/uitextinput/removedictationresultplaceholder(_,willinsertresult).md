# removeDictationResultPlaceholder(_:willInsertResult:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the view that the specified placeholder object is unnecessary.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func removeDictationResultPlaceholder(_ placeholder: Any, willInsertResult: Bool)
```

```objc
- (void) removeDictationResultPlaceholder:(id) placeholder willInsertResult:(BOOL) willInsertResult;
```

## Discussion

If the value in the `willInsertResult` parameter is [`false`](../../Swift/false.md), the placeholder animation is not replaced by an actual dictation result. When this happens, the system still removes the placeholder animation and removes the strong reference to your placeholder object.

> ❗ **Important**:  This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](./dictationrecordingdidend%28%29.md) and [`dictationRecognitionFailed()`](./dictationrecognitionfailed%28%29.md) to implement a custom placeholder.

## Parameters

- `placeholder`: The placeholder object that is no longer needed.
- `willInsertResult`: The value of this parameter is [`true`](../../Swift/true.md) if the dictation value was generated successfully or [`false`](../../Swift/false.md) if an error occurred.

## See Also

### Using dictation
- [func dictationRecordingDidEnd()](./dictationrecordingdidend%28%29.md)
  Tells the object when there is a pending dictation result.
- [func dictationRecognitionFailed()](./dictationrecognitionfailed%28%29.md)
  Tells the object when dictation ends, but recognition fails.
- [func insertDictationResult([UIDictationPhrase])](./insertdictationresult%28_%29.md)
  Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.
- [var insertDictationResultPlaceholder: Any](./insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](./frame%28fordictationresultplaceholder%29.md)
  Asks for the rectangle for displaying the dictation placeholder animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/removedictationresultplaceholder(_:willinsertresult:))*