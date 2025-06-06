# barcodeGenerator()

**Framework**: Core Image  
**Kind**: clm

Generates a barcode as an image from the descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator
```

#### Return_value

The generated image.

#### Discussion

This method generates a custom barcode as an image. The effect uses barcode descriptors to specify properties of the generated barcode.

The barcode generator uses the following property:

The following code creates a filter that generates a QR code containing the text 

```swift
func barcode(inputMessage: Data) -> CIImage {
   let barcodeGenerator = CIFilter.barcodeGenerator()
    barcodeGenerator.barcodeDescriptor = CIQRCodeDescriptor(payload: inputMessage, symbolVersion: 1, maskPattern: 4, errorCorrectionLevel: .levelL)!
    return barcodeGenerator.outputImage!
}

let johnnyAppleseed: [UInt8] = [0x41, 0x04, 0xA6, 0xF6, 0x86, 0xE6, 0xE7, 0x92, 0x04, 0x17, 0x07, 0x06, 0xC6, 0x57, 0x36, 0x56, 0x56, 0x40, 0xEC]
let data = Data(johnnyAppleseed)

let bImage = barcode(inputMessage: data)
```

![A QR code containing the text Johnny Appleseed.](https://docs-assets.developer.apple.com/published/55e118ccd4/rendered2x-1706203917.png)

## See Also

- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](cifilter/3228267-attributedtextimagegenerator.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter/3228268-azteccodegenerator.md)
  Generates a low-density barcode.
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
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter/3228419-sunbeamsgenerator.md)
  Generates an image resembling the sun.
- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](cifilter/3228422-textimagegenerator.md)
  Generates a text image.
- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass of  that represents an Aztec code symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass of  that represents a Data Matrix code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of  that represents a PDF417 symbol.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of  that represents a square QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/3228269-barcodegenerator)*