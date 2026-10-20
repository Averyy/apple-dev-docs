# supportedSymbologies

**Framework**: Vision  
**Kind**: property  
**Role**: Type Property

The array of barcode symbologies that the request supports.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.13+ - Deprecated in 12.0
- tvOS 11.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`supportedSymbologies()`](./supportedsymbologies%28%29.md) instead.

## Declaration

```swift
class var supportedSymbologies: [VNBarcodeSymbology] { get }
```

```objc
@property (class, nonatomic, copy, readonly) NSArray<NSString *> * supportedSymbologies;
```

#### Discussion

Calling this method can be an expensive operation.

## See Also

### Specifying Symbologies
- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](./supportedsymbologies%28%29.md)
  Returns the barcode symbologies that the request supports.
- [var symbologies: [VNBarcodeSymbology]](./symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var coalesceCompositeSymbologies: Bool](./coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](../vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/supportedsymbologies)*