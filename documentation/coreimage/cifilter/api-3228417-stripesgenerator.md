# stripesGenerator()

**Framework**: Core Image  
**Kind**: clm

Generates a line of stripes as an image

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func stripesGenerator() -> any CIFilter & CIStripesGenerator
```

#### Return_value

The generated image.

#### Discussion

This method generates a vertical stripped line pattern as an image. 

The stripes generator filter uses the following properties:

The following code creates a filter that generates a black and white vertical striped image:

```swift
func stripes() -> CIImage {
    let stripesGenerator = CIFilter.stripesGenerator()
    stripesGenerator.center = CGPoint(x: 150, y: 150)
    stripesGenerator.color0 = .white
    stripesGenerator.color1 = .black
    stripesGenerator.width = 80
    stripesGenerator.sharpness = 1
    return stripesGenerator.outputImage!
}
```

![A series of vertical black and white lines repeating the entire image.](https://docs-assets.developer.apple.com/published/a07ad748ba/rendered2x-1588954341.png)

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
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter/3228419-sunbeamsgenerator.md)
  Generates an image resembling the sun.
- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](cifilter/3228422-textimagegenerator.md)
  Generates a text image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228417-stripesgenerator)*