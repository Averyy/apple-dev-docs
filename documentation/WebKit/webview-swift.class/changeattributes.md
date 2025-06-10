# changeAttributes(_:)

**Framework**: WebKit  
**Kind**: method

An action method that changes the attributes of the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func changeAttributes(_ sender: Any?)
```

#### Discussion

This method behaves similar to the [`changeAttributes(_:)`](https://developer.apple.com/documentation/AppKit/NSTextView/changeAttributes(_:)) method in [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView).

## Parameters

- `sender`: The object that sent this message.

## See Also

- [func changeFont(Any?)](webview-swift.class/changefont(_:).md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeDocumentBackgroundColor(Any?)](webview-swift.class/changedocumentbackgroundcolor(_:).md)
  Sets the background color of the selected content.
- [func changeColor(Any?)](webview-swift.class/changecolor(_:).md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changeattributes(_:))*