# CILenticularHaloGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a lenticular halo generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CILenticularHaloGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cilenticularhalogenerator/center.md)
  The x and y position to use as the center of the halo.
- [var color: CIColor](cilenticularhalogenerator/color.md)
  The color of the halo.
- [var haloOverlap: Float](cilenticularhalogenerator/halooverlap.md)
  The separation of colors in the halo.
- [var haloRadius: Float](cilenticularhalogenerator/haloradius.md)
  The radius of the halo.
- [var haloWidth: Float](cilenticularhalogenerator/halowidth.md)
  The width of the halo, from its inner radius to its outer radius.
- [var striationContrast: Float](cilenticularhalogenerator/striationcontrast.md)
  The contrast of the halo colors.
- [var striationStrength: Float](cilenticularhalogenerator/striationstrength.md)
  The intensity of the halo colors.
- [var time: Float](cilenticularhalogenerator/time.md)
  The current time of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](cifilter-swift.class/lenticularhalogenerator.md)
  Generates a lenticular halo image.
- [protocol CICode128BarcodeGenerator](cicode128barcodegenerator.md)
  The properties you use to configure a Code 128 barcode generator filter.
- [protocol CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md)
  The properties you use to configure an attributed-text image generator filter.
- [protocol CIAztecCodeGenerator](ciazteccodegenerator.md)
  The properties you use to configure an Aztec code generator filter.
- [protocol CIBarcodeGenerator](cibarcodegenerator.md)
  The properties you use to configure a barcode generator filter.
- [protocol CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [protocol CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [protocol CICheckerboardGenerator](cicheckerboardgenerator.md)
  The properties you use to configure a checkerboard generator filter.
- [protocol CIMeshGenerator](cimeshgenerator.md)
  The properties you use to configure a mesh generator filter.
- [protocol CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md)
  The properties you use to configure a PDF417 barcode generator filter.
- [protocol CIQRCodeGenerator](ciqrcodegenerator.md)
  The properties you use to configure a QR code generator filter.
- [protocol CIRandomGenerator](cirandomgenerator.md)
  The properties you use to configure a random generator filter.
- [protocol CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md)
  The properties you use to configure a rounded rectangle generator filter.
- [protocol CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [protocol CIStarShineGenerator](cistarshinegenerator.md)
  The properties you use to configure a star-shine generator filter.
- [protocol CIStripesGenerator](cistripesgenerator.md)
  The properties you use to configure a stripes generator filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilenticularhalogenerator)*