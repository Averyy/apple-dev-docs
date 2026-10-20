# frame(forDictationResultPlaceholder:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks for the rectangle for displaying the dictation placeholder animation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
optional func frame(forDictationResultPlaceholder placeholder: Any) -> CGRect
```

```objc
- (CGRect) frameForDictationResultPlaceholder:(id) placeholder;
```

#### Return Value

The rectangle, in the coordinate system of your input view, at which to display the dictation placeholder animation.

#### Discussion

While dictation results are being generated, UIKit displays the built-in dictation placeholder animation. Your implementation of this method should provide the rectangle at which to display this animation (at the location where the dictation results will be inserted).

> ❗ **Important**:  This method is called only if the custom text view client leverages system selection by subclassing `UITextView`. Other clients can use [`dictationRecordingDidEnd()`](./dictationrecordingdidend%28%29.md) and [`dictationRecognitionFailed()`](./dictationrecognitionfailed%28%29.md) to implement a custom placeholder.

## Parameters

- `placeholder`: A placeholder object provided by your app and used to identify the location of the dictation results.

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
- [func removeDictationResultPlaceholder(Any, willInsertResult: Bool)](./removedictationresultplaceholder%28_,willinsertresult%29.md)
  Tells the view that the specified placeholder object is unnecessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/frame(fordictationresultplaceholder:))*