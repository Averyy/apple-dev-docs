# barcodeGenerator()

**Framework**: Core Image  
**Kind**: method

Generates a barcode as an image from the descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator
```

#### Return Value

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

![A QR code containing the text Johnny Appleseed.](https://docs-assets.developer.apple.com/published/24c42769de52d594e7afa325f3c526a8/media-4327881%402x.png)

## See Also

- [class CIAztecCodeDescriptor](ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIDataMatrixCodeDescriptor](cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
- [class CIPDF417CodeDescriptor](cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIQRCodeDescriptor](ciqrcodedescriptor.md)
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](cifilter-swift.class/attributedtextimagegenerator.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter-swift.class/azteccodegenerator.md)
  Generates a low-density barcode.
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
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter-swift.class/sunbeamsgenerator.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/barcodegenerator())*