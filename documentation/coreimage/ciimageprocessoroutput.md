# CIImageProcessorOutput

**Framework**: Core Image  
**Kind**: protocol

A container for writing image data and information produced by a custom image processor.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIImageProcessorOutput
```

#### Overview

Your app does not define classes that adopt this protocol; Core Image provides an object of this type when applying a custom image processor you create with a [`CIImageProcessorKernel`](ciimageprocessorkernel.md) subclass.

In your image processor class’ [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md) method, use an appropriate property of the provided `CIImageProcessorOutput` object to return processed pixel data to Core Image. For example, if you process the image using a Metal shader, bind the [`metalTexture`](ciimageprocessoroutput/metaltexture.md) property as an attachment in a render pass or as an output texture in a compute pass. Or, if you process the image using a CPU-based routine, write processed pixel data to memory using the the [`baseAddress`](ciimageprocessoroutput/baseaddress.md) pointer. You must provide rendered output to one (and only one) of the properties listed in [`Providing Output Image Data`](ciimageprocessoroutput#Providing-Output-Image-Data.md).

To access input pixel data in your image processor block, see the [`CIImageProcessorInput`](ciimageprocessorinput.md) class.

## Topics

### Providing Output Image Data
- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/baseaddress.md)
  A pointer to CPU memory at which to write output pixel data.
- [var metalTexture: (any MTLTexture)?](ciimageprocessoroutput/metaltexture.md)
  A Metal texture to which you can write output pixel data.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/pixelbuffer.md)
  A CoreVideo pixel buffer to which you can write output pixel data.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/surface.md)
  An IOSurface object to which you can write output pixel data.
### Getting Supplemental Information for Image Processing
- [var region: CGRect](ciimageprocessoroutput/region.md)
  The rectangular region of the output image that your processor must provide.
- [var metalCommandBuffer: (any MTLCommandBuffer)?](ciimageprocessoroutput/metalcommandbuffer.md)
  A command buffer to use for image processing using Metal.
- [var bytesPerRow: Int](ciimageprocessoroutput/bytesperrow.md)
  The number of bytes per row of pixels for the output image.
- [var format: CIFormat](ciimageprocessoroutput/format.md)
  The per-pixel data format expected of the output image.
### Instance Properties
- [var digest: UInt64](ciimageprocessoroutput/digest.md)

## See Also

- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorInput](ciimageprocessorinput.md)
  A container of image data and information for use in a custom image processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput)*