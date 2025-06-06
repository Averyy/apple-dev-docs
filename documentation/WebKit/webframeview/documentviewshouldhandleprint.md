# documentViewShouldHandlePrint

**Framework**: Webkit  
**Kind**: property

A Boolean value indicating whether the document view should handle a print operation.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var documentViewShouldHandlePrint: Bool { get }
```

#### Discussion

If this method returns [`false`](https://developer.apple.com/documentation/swift/false), the application terminates its print operation and sends [`printDocumentView()`](webframeview/printdocumentview().md) to the web frame view.

## See Also

- [var canPrintHeadersAndFooters: Bool](webframeview/canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](webframeview/printoperation(with:).md)
  Returns a print operation object to print this frame.
- [func printDocumentView()](webframeview/printdocumentview.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/documentviewshouldhandleprint)*