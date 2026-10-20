# changeAttributes(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that changes the attributes of the current selection.

**Availability**:
- macOS

## Declaration

```swift
func changeAttributes(_ sender: Any?)
```

```objc
- (void) changeAttributes:(id) sender;
```

#### Discussion

This method behaves similar to the [`changeAttributes(_:)`](../../AppKit/nstextview/changeattributes%28_%29.md) method in [`NSTextView`](../../AppKit/nstextview.md).

## Parameters

- `sender`: The object that sent this message.

## See Also

### Changing the Font, Color and Other Attributes When Editing
- [func changeFont(Any?)](./changefont%28_%29.md)
  An action method that changes the font of the selection, or all content if there is no selection.
- [func changeDocumentBackgroundColor(Any?)](./changedocumentbackgroundcolor%28_%29.md)
  Sets the background color of the selected content.
- [func changeColor(Any?)](./changecolor%28_%29.md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changeattributes(_:))*