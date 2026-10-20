# selectionWillChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the input delegate when the selection is about to change in the document.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func selectionWillChange(_ textInput: (any UITextInput)?)
```

```objc
- (void) selectionWillChange:(id<UITextInput>) textInput;
```

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation
- [func textWillChange((any UITextInput)?)](./textwillchange%28_%29.md)
  Tells the input delegate when text is about to change in the document.
### Notifying the delegate of selection changes
- [func selectionDidChange((any UITextInput)?)](./selectiondidchange%28_%29.md)
  Tells the input delegate when the selection has changed in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/selectionwillchange(_:))*