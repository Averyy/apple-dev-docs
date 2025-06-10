# CIImageProcessorInput

**Framework**: Core Image  
**Kind**: protocol

A container of image data and information for use in a custom image processor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIImageProcessorInput
```

#### Overview

Your app does not define classes that adopt this protocol; Core Image provides an object of this type when applying a custom image processor you create with a [`CIImageProcessorKernel`](ciimageprocessorkernel.md) subclass.

In your image processor class’ [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md) method, use the provided `CIImageProcessorInput` object to access the image data and supporting information to perform your custom image processing routine. For example, if you process the image using a Metal shader, use the [`metalTexture`](ciimageprocessorinput/metaltexture.md) property to bind the image as an input texture. Or, if you process the image using a CPU-based routine, use the [`baseAddress`](ciimageprocessorinput/baseaddress.md) property to access pixel data in memory.

To finish setting up or performing your image processing routine, use the provided [`CIImageProcessorOutput`](ciimageprocessoroutput.md) object to return processed pixel data to Core Image.

## Topics

### Accessing Input Image Data
- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/baseaddress.md)
  A pointer to the image data in CPU memory to be processed.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/metaltexture.md)
  A Metal texture containing the image data to be processed.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/pixelbuffer.md)
  A CoreVideo pixel buffer containing the image data to be processed.
- [var surface: IOSurfaceRef](ciimageprocessorinput/surface.md)
  An IOSurface object containing the image data to be processed.
### Getting Supplemental Information for Image Processing
- [var region: CGRect](ciimageprocessorinput/region.md)
  The area within the input image to be processed.
- [var bytesPerRow: Int](ciimageprocessorinput/bytesperrow.md)
  The number of bytes per row of pixels in the input image data.
- [var format: CIFormat](ciimageprocessorinput/format.md)
  The per-pixel data format of the image to be processed.
### Instance Properties
- [var digest: UInt64](ciimageprocessorinput/digest.md)
- [var roiTileCount: Int](ciimageprocessorinput/roitilecount.md)
- [var roiTileIndex: Int](ciimageprocessorinput/roitileindex.md)

## See Also

- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorOutput](ciimageprocessoroutput.md)
  A container for writing image data and information produced by a custom image processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput)*