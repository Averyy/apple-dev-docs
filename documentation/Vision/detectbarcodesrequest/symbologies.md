# symbologies

**Framework**: Vision  
**Kind**: property

The barcode symbologies that the request detects in an image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var symbologies: [BarcodeSymbology]
```

#### Discussion

By default, a request scans for all symbologies. Specify a subset of symbologies to limit the request’s detection range.

## See Also

- [var supportedSymbologies: [BarcodeSymbology]](detectbarcodesrequest/supportedsymbologies.md)
  The collection of barcode symbologies that the request can recognize.
- [enum BarcodeSymbology](barcodesymbology.md)
  The barcode symbologies that the framework detects.
- [var coalescesCompositeSymbologies: Bool](detectbarcodesrequest/coalescescompositesymbologies.md)
  A Boolean value that indicates whether the request coalesces multiple codes into one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectbarcodesrequest/symbologies)*