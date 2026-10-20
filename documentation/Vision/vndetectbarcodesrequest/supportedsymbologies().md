# supportedSymbologies()

**Framework**: Vision  
**Kind**: method  
**Role**: Instance Method

Returns the barcode symbologies that the request supports.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func supportedSymbologies() throws -> [VNBarcodeSymbology]
```

```objc
- (NSArray<NSString *> *) supportedSymbologiesAndReturnError:(NSError **) error;
```

#### Return Value

An array of symbologies.

## See Also

### Specifying Symbologies
- [var symbologies: [VNBarcodeSymbology]](./symbologies.md)
  The barcode symbologies that the request detects in an image.
- [var coalesceCompositeSymbologies: Bool](./coalescecompositesymbologies.md)
  A Boolean value that indicates whether to coalesce multiple codes based on the symbology.
- [struct VNBarcodeSymbology](../vnbarcodesymbology.md)
  The barcode symbologies that the framework detects.
- [class var supportedSymbologies: [VNBarcodeSymbology]](./supportedsymbologies.md)
  The array of barcode symbologies that the request supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vndetectbarcodesrequest/supportedsymbologies())*