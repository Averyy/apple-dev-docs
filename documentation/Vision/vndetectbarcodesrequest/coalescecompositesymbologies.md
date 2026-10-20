# coalesceCompositeSymbologies

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to coalesce multiple codes based on the symbology.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var coalesceCompositeSymbologies: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL coalesceCompositeSymbologies;
```

## See Also

### Specifying Symbologies
- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](./supportedsymbologies%28%29.md)
  Returns the barcode symbologies that the request supports.
- [var symbologies: [VNBarcodeSymbology]](./symbologies.md)
  The barcode symbologies that the request detects in an image.
- [struct VNBarcodeSymbology](../vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.
- [class var supportedSymbologies: [VNBarcodeSymbology]](./supportedsymbologies.md)
  The array of barcode symbologies that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/coalescecompositesymbologies)*