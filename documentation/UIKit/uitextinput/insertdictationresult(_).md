# insertDictationResult(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the object when there is more than one interpretation of a spoken phrase in a dictation result.

**Availability**:
- iOS 5.1+
- iPadOS 5.1+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func insertDictationResult(_ dictationResult: [UIDictationPhrase])
```

```objc
- (void) insertDictationResult:(NSArray<UIDictationPhrase *> *) dictationResult;
```

## Discussion

Implement this optional method if you want to support dictation phrase alternatives. If you do not implement this method, iOS inserts the most likely interpretation of the dictated phrase.

> ❗ **Important**:  This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](./dictationrecordingdidend%28%29.md) and [`dictationRecognitionFailed()`](./dictationrecognitionfailed%28%29.md) to implement a custom placeholder.

## Parameters

- `dictationResult`: An array of [`UIDictationPhrase`](../uidictationphrase.md) objects.

## See Also

### Using dictation
- [func dictationRecordingDidEnd()](./dictationrecordingdidend%28%29.md)
  Tells the object when there is a pending dictation result.
- [func dictationRecognitionFailed()](./dictationrecognitionfailed%28%29.md)
  Tells the object when dictation ends, but recognition fails.
- [var insertDictationResultPlaceholder: Any](./insertdictationresultplaceholder.md)
  Asks for the placeholder object to use while generating dictation results.
- [func frame(forDictationResultPlaceholder: Any) -> CGRect](./frame%28fordictationresultplaceholder%29.md)
  Asks for the rectangle for displaying the dictation placeholder animation.
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](./removedictationresultplaceholder%28_,willinsertresult%29.md)
  Tells the view that the specified placeholder object is unnecessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/insertdictationresult(_:))*