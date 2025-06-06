# supportedSymbologies

**Framework**: Vision  
**Kind**: property

The array of barcode symbologies that the request supports.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class var supportedSymbologies: [VNBarcodeSymbology] { get }
```

#### Discussion

Calling this method can be an expensive operation.

## See Also

- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](vndetectbarcodesrequest/supportedsymbologies.md)
  Returns the barcode symbologies that the request supports.
- [var symbologies: [VNBarcodeSymbology]](vndetectbarcodesrequest/symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var coalesceCompositeSymbologies: Bool](vndetectbarcodesrequest/coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/supportedsymbologies)*