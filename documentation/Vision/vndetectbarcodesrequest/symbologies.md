# symbologies

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readwrite) NSArray<NSString *> * symbologies;
```

## Discussion

By default, a request scans for all symbologies. Specify a subset of symbologies to limit the request’s detection range.

> **Note**:  Setting a revision on the request resets the symbologies to all symbologies for the specified revision.

## See Also

### Specifying Symbologies
- [func supportedSymbologies() throws -> [VNBarcodeSymbology]](./supportedsymbologies%28%29.md)
  Returns the barcode symbologies that the request supports.
- [var coalesceCompositeSymbologies: Bool](./coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](../vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.
- [class var supportedSymbologies: [VNBarcodeSymbology]](./supportedsymbologies.md)
  The array of barcode symbologies that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/symbologies)*