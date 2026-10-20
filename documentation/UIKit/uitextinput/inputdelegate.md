# inputDelegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An input delegate that receives a notification when text changes or when the selection changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
weak var inputDelegate: (any UITextInputDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UITextInputDelegate> inputDelegate;
```

#### Discussion

The text input system automatically assigns a delegate to this property at runtime. It is the responsibility of the view that adopts the [`UITextInput`](../uitextinput.md) protocol to notify the input delegate at the appropriate junctures.

## See Also

### Handling text input
- [protocol UITextInputDelegate](../uitextinputdelegate.md)
  An intermediary between a document and the text input system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinput/inputdelegate)*