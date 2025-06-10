# changeFont(_:)

**Framework**: WebKit  
**Kind**: method

An action method that changes the font of the selection, or all content if there is no selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeFont(_ sender: Any?)
```

#### Discussion

If the receiver doesn’t use the Fonts panel, this method does nothing.

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func changeAttributes(Any?)](webview-swift.class/changeattributes(_:).md)
  An action method that changes the attributes of the current selection.
- [func changeDocumentBackgroundColor(Any?)](webview-swift.class/changedocumentbackgroundcolor(_:).md)
  Sets the background color of the selected content.
- [func changeColor(Any?)](webview-swift.class/changecolor(_:).md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changefont(_:))*