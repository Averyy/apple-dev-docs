# sunbeamsGenerator()

**Framework**: Core Image  
**Kind**: clm

Generates an image resembling the sun.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator
```

#### Return_value

The generated image.

#### Discussion

This method generates a sunbeam as an image. The effect generates a center-textured sun with striations. You can combine with other filters to create more sophisticated images. 

The sunbeams generator filter uses the following properties:

The following code creates a filter that generates an image that resembles a yellow sun with sunbeams:

```swift
    func sunBeam () -> CIImage {
        let sunBeamGenerator = CIFilter.sunbeamsGenerator()
        sunBeamGenerator.center = CGPoint(x: 150, y: 150)
        sunBeamGenerator.color = CIColor(red: 0.96, green: 1, blue: 1, alpha: 1)
        sunBeamGenerator.sunRadius = 40
        sunBeamGenerator.maxStriationRadius = 2.58
        sunBeamGenerator.striationStrength = 0.50
        sunBeamGenerator.striationContrast = 1.38
        sunBeamGenerator.time = 0
        return sunBeamGenerator.outputImage!
    }
```

![An image of a hazy yellow and white ball with lines of color gradually fading to the periphery.](https://docs-assets.developer.apple.com/published/abb2e950d6/rendered2x-1583282308.png)

## See Also

- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](cifilter/3228267-attributedtextimagegenerator.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter/3228268-azteccodegenerator.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](cifilter/3228269-barcodegenerator.md)
  Generates a barcode as an image from the descriptor.
- [class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator](cifilter/4401849-blurredrectanglegenerator.md)
  Generates a blurred rectangle.
- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](cifilter/3228279-checkerboardgenerator.md)
  Generates a checkerboard image.
- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](cifilter/3228281-code128barcodegenerator.md)
  Generates a high-density, linear barcode.
- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](cifilter/3228345-lenticularhalogenerator.md)
  Generates a lenticular halo image.
- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](cifilter/3228359-meshgenerator.md)
  Generates a pattern made from an array of line segments.
- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](cifilter/3228261-pdf417barcodegenerator.md)
  Generates a high-density linear barcode.
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter/3228262-qrcodegenerator.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](cifilter/3228396-randomgenerator.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](cifilter/3335007-roundedrectanglegenerator.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](cifilter/4401875-roundedrectanglestrokegenerator.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter/3228415-starshinegenerator.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter/3228417-stripesgenerator.md)
  Generates a line of stripes as an image
- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](cifilter/3228422-textimagegenerator.md)
  Generates a text image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228419-sunbeamsgenerator)*