# changeDocumentBackgroundColor(_:)

**Framework**: WebKit  
**Kind**: method

Sets the background color of the selected content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeDocumentBackgroundColor(_ sender: Any?)
```

#### Discussion

This method is invoked by the `NSColorPanel` sender and behaves similar to the [`changeDocumentBackgroundColor(_:)`](https://developer.apple.com/documentation/AppKit/NSTextView/changeDocumentBackgroundColor(_:)) method in [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView).

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func changeFont(Any?)](webview-swift.class/changefont(_:).md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeAttributes(Any?)](webview-swift.class/changeattributes(_:).md)
  An action method that changes the attributes of the current selection.
- [func changeColor(Any?)](webview-swift.class/changecolor(_:).md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changedocumentbackgroundcolor(_:))*