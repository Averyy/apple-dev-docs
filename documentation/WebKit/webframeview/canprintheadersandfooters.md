# canPrintHeadersAndFooters

**Framework**: WebKit  
**Kind**: property

A Boolean value indicating whether the receiver can print headers and footers.

**Availability**:
- macOS 10.3+

## Declaration

```swift
@MainActor
var canPrintHeadersAndFooters: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver can print headers and footers; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](webframeview/printoperation(with:).md)
  Returns a print operation object to print this frame.
- [var documentViewShouldHandlePrint: Bool](webframeview/documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.
- [func printDocumentView()](webframeview/printdocumentview.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/canprintheadersandfooters)*