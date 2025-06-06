# symbologies

**Framework**: Vision  
**Kind**: property

The barcode symbologies that the request detects in an image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var symbologies: [VNBarcodeSymbology] { get set }
```

#### Discussion

By default, a request scans for all symbologies. Specify a subset of symbologies to limit the request’s detection range.

> **Note**:  Setting a revision on the request resets the symbologies to all symbologies for the specified revision.

 Setting a revision on the request resets the symbologies to all symbologies for the specified revision.

## See Also

- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](vndetectbarcodesrequest/supportedsymbologies.md)
  Returns the barcode symbologies that the request supports.
- [var coalesceCompositeSymbologies: Bool](vndetectbarcodesrequest/coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.
- [class var supportedSymbologies: [VNBarcodeSymbology]](vndetectbarcodesrequest/supportedsymbologies.md)
  The array of barcode symbologies that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/symbologies)*