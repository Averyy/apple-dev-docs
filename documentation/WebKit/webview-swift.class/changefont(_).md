# changeFont(_:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

An action method that changes the font of the selection, or all content if there is no selection.

**Availability**:
- macOS

## Declaration

```swift
func changeFont(_ sender: Any?)
```

```objc
- (void) changeFont:(id) sender;
```

#### Discussion

If the receiver doesn’t use the Fonts panel, this method does nothing.

## Parameters

- `sender`: The object that sent this message.

## See Also

### Changing the Font, Color and Other Attributes When Editing
- [func changeAttributes(Any?)](./changeattributes%28_%29.md)
  An action method that changes the attributes of the current selection.
- [func changeDocumentBackgroundColor(Any?)](./changedocumentbackgroundcolor%28_%29.md)
  Sets the background color of the selected content.
- [func changeColor(Any?)](./changecolor%28_%29.md)
  Sets the color of the selected content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webview-swift.class/changefont(_:))*