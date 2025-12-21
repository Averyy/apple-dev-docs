# textImageGenerator()

**Framework**: Core Image  
**Kind**: method

Generates a text image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func textImageGenerator() -> any CIFilter & CITextImageGenerator
```

#### Return Value

The generated image.

#### Discussion

This method generates a text image. The effect takes the input string property and the scale factor to scale up the text. You commonly combine this filter with other filters to create a watermark on images.

The text image generator filter uses the following properties:

The following code creates a filter that generates a string of text as a grayscale image:

```swift
func textImage(inputText: String) -> CIImage {
    let textImageGenerator = CIFilter.textImageGenerator()
    textImageGenerator.text = inputText
    textImageGenerator.fontName = "Helvetica"
    textImageGenerator.fontSize = 25
    textImageGenerator.scaleFactor = 4
    return textImageGenerator.outputImage!
}
```

![An image with the text Hello World! in black and a hand wave emoticon in gray.](https://docs-assets.developer.apple.com/published/6c5365a54c0a0655883f08fb58a25a73/media-3546321%402x.png)

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
- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](cifilter-swift.class/code128barcodegenerator.md)
  Generates a high-density, linear barcode.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/textimagegenerator())*