# code128BarcodeGenerator()

**Framework**: Core Image  
**Kind**: method

Generates a high-density, linear barcode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator
```

#### Return Value

The generated image.

#### Discussion

This method generates a Code 128 barcode as an image. Code 128 is a high-density linear barcode defined in the ISO/IEC 15417:2007 standard. Use this filter to generate alphanumeric or numeric-only barcodes. The barcode can contain any of the 128 ASCII characters.

The Code 128 barcode filter uses the following properties:

The following code creates a filter that generates a Code 128 barcode:

```swift
func code128Barcode(barcode: String) -> CIImage {
    let code128Barcode = CIFilter.code128BarcodeGenerator()
    code128Barcode.message = barcode.data(using: .ascii)!
    code128Barcode.quietSpace = 5
    code128Barcode.barcodeHeight = 20
    return code128Barcode.outputImage!
}
```

![An image of a black and white barcode made of vertical lines of various widths representing the encoded data of: hello!](https://docs-assets.developer.apple.com/published/51cae82b76916ec1265ac840d44ca2a7/media-3546314%402x.png)

## See Also

- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](cifilter-swift.class/attributedtextimagegenerator.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter-swift.class/azteccodegenerator.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](cifilter-swift.class/barcodegenerator.md)
  Generates a barcode as an image from the descriptor.
- [class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator](cifilter-swift.class/blurredrectanglegenerator.md)
  Generates a blurred rectangle.
- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](cifilter-swift.class/checkerboardgenerator.md)
  Generates a checkerboard image.
- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](cifilter-swift.class/lenticularhalogenerator.md)
  Generates a lenticular halo image.
- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](cifilter-swift.class/meshgenerator.md)
  Generates a pattern made from an array of line segments.
- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](cifilter-swift.class/pdf417barcodegenerator.md)
  Generates a high-density linear barcode.
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter-swift.class/qrcodegenerator.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](cifilter-swift.class/randomgenerator.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](cifilter-swift.class/roundedrectanglegenerator.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](cifilter-swift.class/roundedrectanglestrokegenerator.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter-swift.class/starshinegenerator.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter-swift.class/stripesgenerator.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter-swift.class/sunbeamsgenerator.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/code128barcodegenerator())*