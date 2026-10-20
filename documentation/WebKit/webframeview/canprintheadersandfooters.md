# canPrintHeadersAndFooters

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver can print headers and footers.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var canPrintHeadersAndFooters: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL canPrintHeadersAndFooters;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver can print headers and footers; otherwise, [`false`](../../Swift/false.md).

## See Also

### Printing Views
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](./printoperation%28with%29.md)
  Returns a print operation object to print this frame.
- [var documentViewShouldHandlePrint: Bool](./documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.
- [func printDocumentView()](./printdocumentview%28%29.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/canprintheadersandfooters)*