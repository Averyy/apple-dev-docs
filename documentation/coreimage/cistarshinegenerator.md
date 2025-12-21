# CIStarShineGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a star-shine generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIStarShineGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cistarshinegenerator/center.md)
  The x and y position to use as the center of the star.
- [var color: CIColor](cistarshinegenerator/color.md)
  The color to use for the outer shell of the circular star.
- [var crossAngle: Float](cistarshinegenerator/crossangle.md)
  The angle of the cross pattern.
- [var crossOpacity: Float](cistarshinegenerator/crossopacity.md)
  The opacity of the cross pattern.
- [var crossScale: Float](cistarshinegenerator/crossscale.md)
  The size of the cross pattern.
- [var crossWidth: Float](cistarshinegenerator/crosswidth.md)
  The width of the cross pattern.
- [var epsilon: Float](cistarshinegenerator/epsilon.md)
  The length of the cross spikes.
- [var radius: Float](cistarshinegenerator/radius.md)
  The radius of the star.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter-swift.class/starshinegenerator.md)
  Generates a star-shine image.
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
- [protocol CILenticularHaloGenerator](cilenticularhalogenerator.md)
  The properties you use to configure a lenticular halo generator filter.
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
- [protocol CIStripesGenerator](cistripesgenerator.md)
  The properties you use to configure a stripes generator filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cistarshinegenerator)*