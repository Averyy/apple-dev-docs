# printDocumentView()

**Framework**: Webkit  
**Kind**: method

Prints the receiver.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
func printDocumentView()
```

#### Discussion

This method is invoked if the [`documentViewShouldHandlePrint`](webframeview/documentviewshouldhandleprint.md) method returns [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var canPrintHeadersAndFooters: Bool](webframeview/canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](webframeview/printoperation(with:).md)
  Returns a print operation object to print this frame.
- [var documentViewShouldHandlePrint: Bool](webframeview/documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/printdocumentview())*