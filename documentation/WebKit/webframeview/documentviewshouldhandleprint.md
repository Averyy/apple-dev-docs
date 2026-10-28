# documentViewShouldHandlePrint

**Framework**: WebKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the document view should handle a print operation.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
var documentViewShouldHandlePrint: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL documentViewShouldHandlePrint;
```

## Discussion

If this method returns [`false`](../../Swift/false.md), the application terminates its print operation and sends [`printDocumentView()`](./printdocumentview%28%29.md) to the web frame view.

## See Also

### Printing Views
- [var canPrintHeadersAndFooters: Bool](./canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](./printoperation%28with%29.md)
  Returns a print operation object to print this frame.
- [func printDocumentView()](./printdocumentview%28%29.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/documentviewshouldhandleprint)*