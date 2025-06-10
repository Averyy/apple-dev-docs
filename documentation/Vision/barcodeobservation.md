# BarcodeObservation

**Framework**: Vision  
**Kind**: struct

An object that represents barcode information that an image-analysis request detects.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
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
### Instance Properties
- [var boundingRegion: NormalizedRegion](barcodeobservation/boundingregion.md)
  The bounding region of the barcode.

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

## See Also

- [func perform(on: URL, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-80bya.md)
  Performs the request on an image URL and produces observations.
- [func perform(on: Data, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3f3f1.md)
  Performs the request on image data and produces observations.
- [func perform(on: CGImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-qxxx.md)
  Performs the request on a Core Graphics image and produces observations.
- [func perform(on: CVPixelBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-xspx.md)
  Performs the request on a pixel buffer and produces observations.
- [func perform(on: CMSampleBuffer, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-3hddl.md)
  Performs the request on a Core Media buffer and produces observations.
- [func perform(on: CIImage, orientation: CGImagePropertyOrientation?) async throws -> Self.Result](imageprocessingrequest/perform(on:orientation:)-85ex1.md)
  Performs the request on a Core Image image and produces observations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/barcodeobservation)*