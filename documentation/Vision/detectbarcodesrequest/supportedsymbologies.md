# supportedSymbologies

**Framework**: Vision  
**Kind**: property

The collection of barcode symbologies that the request can recognize.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var supportedSymbologies: [BarcodeSymbology] { get }
```

#### Discussion

Using this property could be a potentially expensive operation.

## See Also

- [var symbologies: [BarcodeSymbology]](detectbarcodesrequest/symbologies.md)
  The barcode symbologies that the request detects in an image.
- [enum BarcodeSymbology](barcodesymbology.md)
  The barcode symbologies that the framework detects.
- [var coalescesCompositeSymbologies: Bool](detectbarcodesrequest/coalescescompositesymbologies.md)
  A Boolean value that indicates whether the request coalesces multiple codes into one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/detectbarcodesrequest/supportedsymbologies)*