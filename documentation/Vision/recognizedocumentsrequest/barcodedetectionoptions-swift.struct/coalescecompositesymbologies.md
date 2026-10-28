# coalesceCompositeSymbologies

**Framework**: Vision  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the request combines multiple codes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var coalesceCompositeSymbologies: Bool
```

## Discussion

The default value for this property is `false`.

## See Also

### Getting the symbology
- [var enabled: Bool](./enabled.md)
  Boolean value that indicates whether to detect barcodes in the document.
- [var symbologies: [BarcodeSymbology]](./symbologies.md)
  The barcode symbologies that the request detects in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.struct/coalescecompositesymbologies)*