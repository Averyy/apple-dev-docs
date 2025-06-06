# RecognizedItem

**Framework**: Visionkit  
**Kind**: enum

An item that the data scanner recognizes in the camera’s live video.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum RecognizedItem
```

## Mentions

- [Scanning data with the camera](scanning-data-with-the-camera.md)

#### Overview

A `RecognizedItem` enumeration contains the data for an item that the scanner identifies, such as the location, bounds, and content of the item. For text items, the content is the selected string, and for barcodes, it’s the encoded payload string.

## Topics

### Machine-readable items
- [case barcode(RecognizedItem.Barcode)](recognizeditem/barcode(_:).md)
  A machine-readable barcode.
- [RecognizedItem.Barcode](recognizeditem/barcode.md)
  An object that represents a machine-readable code that the scanner recognizes.
### Text items
- [case text(RecognizedItem.Text)](recognizeditem/text(_:).md)
  Text or data the analyzer detects in text.
- [RecognizedItem.Text](recognizeditem/text.md)
  An object that represents a text item that the scanner recognizes.
### Item location
- [var bounds: RecognizedItem.Bounds](recognizeditem/bounds-swift.property.md)
  The four corners of the recognized item in view coordinates.
- [RecognizedItem.Bounds](recognizeditem/bounds-swift.struct.md)
  An object that represents the four corners of a recognized item.
### Item identification
- [var id: UUID](recognizeditem/id.md)
  A unique identifier for the recognized item.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [Scanning data with the camera](scanning-data-with-the-camera.md)
  Enable Live Text data scanning of text and codes that appear in the camera’s viewfinder.
- [class DataScannerViewController](datascannerviewcontroller.md)
  An object that scans the camera live video for text, data in text, and machine-readable codes.
- [protocol DataScannerViewControllerDelegate](datascannerviewcontrollerdelegate.md)
  A delegate object that responds when people interact with items that the data scanner recognizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionkit/recognizeditem)*