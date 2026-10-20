# VNBarcodeCompositeType

**Framework**: Vision  
**Kind**: enum  
**Role**: Enumeration

Composite types for barcode requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@frozen
enum VNBarcodeCompositeType
```

```c
enum VNBarcodeCompositeType : NSInteger;
```

## Topics

### Composite Types
- [VNBarcodeCompositeType.gs1TypeA](./vnbarcodecompositetype/gs1typea.md)
  A type that represents trade items in bulk.
- [VNBarcodeCompositeType.gs1TypeB](./vnbarcodecompositetype/gs1typeb.md)
  A type that represents trade items by piece.
- [VNBarcodeCompositeType.gs1TypeC](./vnbarcodecompositetype/gs1typec.md)
  A type that represents trade items in varying quantity.
- [VNBarcodeCompositeType.linked](./vnbarcodecompositetype/linked.md)
  A type that represents a linked composite type.
- [VNBarcodeCompositeType.none](./vnbarcodecompositetype/none.md)
  A type that represents no composite type.
### Creating a Composite Type
- [init?(rawValue: Int)](./vnbarcodecompositetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Barcode detection
- [class VNDetectBarcodesRequest](./vndetectbarcodesrequest.md)
  A request that detects barcodes in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnbarcodecompositetype)*