# CIPDF417BarcodeGenerator

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a PDF417 barcode generator filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPDF417BarcodeGenerator
```

## Topics

### Instance Properties
- [var alwaysSpecifyCompaction: Float](cipdf417barcodegenerator/3228605-alwaysspecifycompaction.md)
  A Boolean value specifying whether to force compaction style.
- [var compactStyle: Float](cipdf417barcodegenerator/3228606-compactstyle.md)
  A Boolean value specifying whether to force compact style Aztec code.
- [var compactionMode: Float](cipdf417barcodegenerator/3228607-compactionmode.md)
  The compaction mode of the generated barcode.
- [var correctionLevel: Float](cipdf417barcodegenerator/3228608-correctionlevel.md)
  The correction level ratio of the generated barcode.
- [var dataColumns: Float](cipdf417barcodegenerator/3228609-datacolumns.md)
  The number of data columns in the generated barcode.
- [var maxHeight: Float](cipdf417barcodegenerator/3228610-maxheight.md)
  The maximum height, in pixels, of the generated barcode.
- [var maxWidth: Float](cipdf417barcodegenerator/3228611-maxwidth.md)
  The maximum width, in pixels, of the generated barcode.
- [var message: Data](cipdf417barcodegenerator/3228612-message.md)
  The message to encode in the PDF417 barcode.
- [var minHeight: Float](cipdf417barcodegenerator/3228613-minheight.md)
  The minimum height, in pixels, of the generated barcode.
- [var minWidth: Float](cipdf417barcodegenerator/3228614-minwidth.md)
  The minimum width, in pixels, of the generated barcode.
- [var preferredAspectRatio: Float](cipdf417barcodegenerator/3228615-preferredaspectratio.md)
  The preferred aspect ratio of the generated barcode.
- [var rows: Float](cipdf417barcodegenerator/3228616-rows.md)
  The number of rows in the generated barcode.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](cifilter/3228261-pdf417barcodegenerator.md)
  Generates a high-density linear barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417barcodegenerator)*