# printDocumentView()

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Prints the receiver.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func printDocumentView()
```

```objc
- (void) printDocumentView;
```

## Discussion

This method is invoked if the [`documentViewShouldHandlePrint`](./documentviewshouldhandleprint.md) method returns [`false`](../../Swift/false.md).

## See Also

### Printing Views
- [var canPrintHeadersAndFooters: Bool](./canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [func printOperation(with: NSPrintInfo!) -> NSPrintOperation!](./printoperation%28with%29.md)
  Returns a print operation object to print this frame.
- [var documentViewShouldHandlePrint: Bool](./documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/printdocumentview())*