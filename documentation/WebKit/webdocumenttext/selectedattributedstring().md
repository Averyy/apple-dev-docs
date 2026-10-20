# selectedAttributedString()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the currently selected text in the web document as an attributed string.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func selectedAttributedString() -> NSAttributedString!
```

```objc
- (NSAttributedString *) selectedAttributedString;
```

#### Return Value

An attributed string containing the currently selected text in the web document.

## See Also

### Selecting and deselecting text
- [func selectAll()](./selectall%28%29.md)
  Selects all the text in the web document.
- [func deselectAll()](./deselectall%28%29.md)
  Deselects the currently selected text in the web document.
- [func selectedString() -> String!](./selectedstring%28%29.md)
  Returns the currently selected text in the web document as a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webdocumenttext/selectedattributedstring())*