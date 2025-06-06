# getActiveDocument

**Framework**: TVMLKit JS  
**Kind**: func

Retrieves the currently active document.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
Document getActiveDocument();
```

#### Return_value

The currently active document.

#### Discussion

The currently active document is the document that the user is interacting with. It can be the document on top of the navigation stack or a modally presented document. If the a menu bar document is the top most document, this function returns the document that is selected in the Menu Bar.

## See Also

- [UUID](1627409-uuid.md)
  Generates a unique UUID.
- [canOpenURL](2123042-canopenurl.md)
  Determines if a deep-link to another app can be opened.
- [openURL](1627399-openurl.md)
  Opens a deep link into another app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/1627314-getactivedocument)*