# printOperation(with:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

Returns a print operation object to print this frame.

**Availability**:
- macOS 10.3+ - Deprecated in 10.14

## Declaration

```swift
func printOperation(with printInfo: NSPrintInfo!) -> NSPrintOperation!
```

```objc
- (NSPrintOperation *) printOperationWithPrintInfo:(NSPrintInfo *) printInfo;
```

## Return Value

An `NSPrintOperation` object set up to print this frame. See [`NSPrintOperation`](../../AppKit/nsprintoperation.md) for more information about this object.

## Parameters

- `printInfo`: Information about the print settings needed to print this frame. See [`NSPrintInfo`](../../AppKit/nsprintinfo.md) for more information about this object.

## See Also

### Printing Views
- [var canPrintHeadersAndFooters: Bool](./canprintheadersandfooters.md)
  A Boolean value indicating whether the receiver can print headers and footers.
- [var documentViewShouldHandlePrint: Bool](./documentviewshouldhandleprint.md)
  A Boolean value indicating whether the document view should handle a print operation.
- [func printDocumentView()](./printdocumentview%28%29.md)
  Prints the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webframeview/printoperation(with:))*