# selectionDidChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the input delegate when the selection has changed in the document.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func selectionDidChange(_ textInput: (any UITextInput)?)
```

```objc
- (void) selectionDidChange:(id<UITextInput>) textInput;
```

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation
- [func textDidChange((any UITextInput)?)](./textdidchange%28_%29.md)
  Tells the input delegate when text has changed in the document.
### Notifying the delegate of selection changes
- [func selectionWillChange((any UITextInput)?)](./selectionwillchange%28_%29.md)
  Tells the input delegate when the selection is about to change in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectiondidchange(_:))*