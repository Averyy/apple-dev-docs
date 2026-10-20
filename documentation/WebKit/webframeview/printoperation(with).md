# printOperation(with:)

**Framework**: WebKit  
**Kind**: method

Returns a print operation object to print this frame.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func printOperation(with printInfo: NSPrintInfo!) -> NSPrintOperation!
```

#### Return Value

An `NSPrintOperation` object set up to print this frame. See [`NSPrintOperation`](https://developer.apple.com/documentation/appkit/nsprintoperation) for more information about this object.

## Parameters

- `printInfo`: Information about the print settings needed to print this frame. See [`NSPrintInfo`](https://developer.apple.com/documentation/appkit/nsprintinfo) for more information about this object.

## See Also

- [var canPrintHeadersAndFooters: Bool](webframeview/canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [var documentViewShouldHandlePrint: Bool](webframeview/documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.
- [func printDocumentView()](webframeview/printdocumentview.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/printoperation(with:))*