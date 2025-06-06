# changeColor(_:)

**Framework**: Webkit  
**Kind**: method

Sets the color of the selected content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeColor(_ sender: Any?)
```

#### Discussion

This method is invoked by the `NSColorPanel` sender and behaves similar to the [`changeColor(_:)`](https://developer.apple.com/documentation/AppKit/NSTextView/changeColor(_:)) method in [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView).

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func changeFont(Any?)](webview/changefont(_:).md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeAttributes(Any?)](webview/changeattributes(_:).md)
  An action method that changes the attributes of the current selection.
- [func changeDocumentBackgroundColor(Any?)](webview/changedocumentbackgroundcolor(_:).md)
  Sets the background color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview/changecolor(_:))*