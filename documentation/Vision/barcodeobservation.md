# BarcodeObservation

**Framework**: Vision  
**Kind**: struct

An object that represents barcode information that an image-analysis request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct BarcodeObservation
```

## Topics

### Creating an observation
- [init(VNBarcodeObservation)](barcodeobservation/init(_:).md)
  Creates a barcode observation.
### Getting the bounding region
- [var boundingRegion: NormalizedRegion](barcodeobservation/boundingregion.md)
  The bounding region of the barcode.
### Inspecting an observation
- [enum RequestDescriptor](requestdescriptor.md)
  A type that describes the request and revision combination.
- [let isColorInverted: Bool](barcodeobservation/iscolorinverted.md)
  A Boolean value that indicates whether the barcode is color inverted.
- [let isGS1DataCarrier: Bool](barcodeobservation/isgs1datacarrier.md)
  A Boolean value that indicates whether the barcode carries any global standards data.
### Getting the payload
- [let payloadData: Data?](barcodeobservation/payloaddata.md)
  The raw data representation of the barcode’s payload.
- [let payloadString: String?](barcodeobservation/payloadstring.md)
  A string value that represents the barcode payload.
- [let supplementalPayloadData: Data?](barcodeobservation/supplementalpayloaddata.md)
  The raw data representation of the barcode’s supplemental payload.
- [let supplementalPayloadString: String?](barcodeobservation/supplementalpayloadstring.md)
  The supplemental code decoded as a string value.
### Getting the symbology
- [let symbology: BarcodeSymbology](barcodeobservation/symbology.md)
  The symbology of the observed barcode.
- [enum BarcodeSymbology](barcodesymbology.md)
  The barcode symbologies that the framework detects.
### Getting the composite type
- [let supplementalCompositeType: BarcodeObservation.CompositeType?](barcodeobservation/supplementalcompositetype.md)
  The supplemental composite type.
- [BarcodeObservation.CompositeType](barcodeobservation/compositetype.md)
  Composite types for barcode requests.

## Relationships

### Conforms To
- [BoundingBoxProviding](boundingboxproviding.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [QuadrilateralProviding](quadrilateralproviding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VisionObservation](visionobservation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodeobservation)*