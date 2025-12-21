# symbologies

**Framework**: Vision  
**Kind**: property

The barcode symbologies that the request detects in an image.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var symbologies: [BarcodeSymbology]
```

#### Discussion

By default, a request scans for all symbologies. Specify a subset of symbologies to limit the request’s detection range. To see the specific codes recognized refer to [`supportedBarcodeSymbologies`](recognizedocumentsrequest/supportedbarcodesymbologies.md).

## See Also

- [var coalesceCompositeSymbologies: Bool](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/coalescecompositesymbologies.md)
  A Boolean value that indicates whether the request combines multiple codes.
- [var enabled: Bool](recognizedocumentsrequest/barcodedetectionoptions-swift.struct/enabled.md)
  Boolean value that indicates whether to detect barcodes in the document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/recognizedocumentsrequest/barcodedetectionoptions-swift.struct/symbologies)*