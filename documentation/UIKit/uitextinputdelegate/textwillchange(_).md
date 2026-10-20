# textWillChange(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the input delegate when text is about to change in the document.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
func textWillChange(_ textInput: (any UITextInput)?)
```

```objc
- (void) textWillChange:(id<UITextInput>) textInput;
```

## Mentions

- [Configuring a custom keyboard interface](../configuring-a-custom-keyboard-interface.md)

## Parameters

- `textInput`: The document instance whose class adopts the UITextInput protocol.

## See Also

### Related Documentation
- [func selectionWillChange((any UITextInput)?)](./selectionwillchange%28_%29.md)
  Tells the input delegate when the selection is about to change in the document.
### Notifying the delegate of textual changes
- [func textDidChange((any UITextInput)?)](./textdidchange%28_%29.md)
  Tells the input delegate when text has changed in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitextinputdelegate/textwillchange(_:))*