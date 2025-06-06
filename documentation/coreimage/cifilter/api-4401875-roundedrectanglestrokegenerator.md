# roundedRectangleStrokeGenerator()

**Framework**: Core Image  
**Kind**: clm

Creates an image containing the outline of a rounded rectangle.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.5+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator
```

#### Return_value

A [`CIImage`](ciimage.md) containing the stroked rectangle.

#### Discussion

This filter creates an outline of a rounded rectangle.

The filter takes the following properties:

The following code generates an image containing a stroked rounded rectangle:

```swift
func roundedRectangleStroke() -> CIImage {
    let filter = CIFilter.roundedRectangleStrokeGenerator()
    filter.extent = CGRect(x: 0, y: 0, width: 200, height: 100)
    filter.color = CIColor.red
    filter.width = 5
    filter.radius = 20
    return filter.outputImage!
}
```

![An image containing an outlined rectangle with rounded corners.](https://docs-assets.developer.apple.com/published/5e57680a19/rendered2x-1708530123.png)

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
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter/3228415-starshinegenerator.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter/3228417-stripesgenerator.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter/3228419-sunbeamsgenerator.md)
  Generates an image resembling the sun.
- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](cifilter/3228422-textimagegenerator.md)
  Generates a text image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/4401875-roundedrectanglestrokegenerator)*