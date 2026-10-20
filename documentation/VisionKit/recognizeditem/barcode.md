# RecognizedItem.Barcode

**Framework**: VisionKit  
**Kind**: struct  
**Role**: Structure

An object that represents a machine-readable code that the scanner recognizes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Barcode
```

## Topics

### Getting payloads
- [var payloadStringValue: String?](./barcode/payloadstringvalue.md)
  The payload or string representation for the barcode.
### Locating barcodes
- [var bounds: RecognizedItem.Bounds](./barcode/bounds.md)
  The location of the recognized item in the view.
- [var observation: VNBarcodeObservation](./barcode/observation.md)
  A representation of the barcode information.
### Identifying barcodes
- [var id: UUID](./barcode/id.md)
  A unique identifier for the recognized item.

## Relationships

### Conforms To
- [Identifiable](../../Swift/identifiable.md)

## See Also

### Machine-readable items
- [case barcode(RecognizedItem.Barcode)](./barcode%28_%29.md)
  A machine-readable barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/recognizeditem/barcode)*