# enabled

**Framework**: Vision  
**Kind**: property

A Boolean value that indicates whether to detect barcodes in the document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var enabled: Bool
```

#### Discussion

The value is unavailable by default. To enable barcode detection, set the property value to `true`.

## See Also

- [var coalesceCompositeSymbologies: Bool](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/coalescecompositesymbologies.md)
  A Boolean value that indicates whether the request combines multiple codes.
- [var symbologies: [BarcodeSymbology]](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/symbologies.md)
  The barcode symbologies that the request detects in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.struct/enabled)*