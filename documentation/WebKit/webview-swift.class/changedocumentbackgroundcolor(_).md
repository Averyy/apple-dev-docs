# changeDocumentBackgroundColor(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Sets the background color of the selected content.

**Availability**:
- macOS

## Declaration

```swift
func changeDocumentBackgroundColor(_ sender: Any?)
```

```objc
- (void) changeDocumentBackgroundColor:(id) sender;
```

## Discussion

This method is invoked by the `NSColorPanel` sender and behaves similar to the [`changeDocumentBackgroundColor(_:)`](../../AppKit/nstextview/changedocumentbackgroundcolor%28_%29.md) method in [`NSTextView`](../../AppKit/nstextview.md).

## Parameters

- `sender`: The object that sent this message.

## See Also

### Changing the Font, Color and Other Attributes When Editing
- [func changeFont(Any?)](./changefont%28_%29.md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeAttributes(Any?)](./changeattributes%28_%29.md)
  An action method that changes the attributes of the current selection.
- [func changeColor(Any?)](./changecolor%28_%29.md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changedocumentbackgroundcolor(_:))*