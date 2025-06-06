# barcode(symbologies:)

**Framework**: Visionkit  
**Kind**: method

Creates a data type for barcodes the use the specified symbologies.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func barcode(symbologies: [VNBarcodeSymbology] = []) -> DataScannerViewController.RecognizedDataType
```

#### Return Value

A barcode data type for the specified symbologies.

## Parameters

- `symbologies`: The barcode symbologies that the scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/datascannerviewcontroller/recognizeddatatype/barcode(symbologies:))*