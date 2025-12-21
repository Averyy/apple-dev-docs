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

In your image processor class’ [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md) method, use an appropriate property of the provided `CIImageProcessorOutput` object to return processed pixel data to Core Image. For example, if you process the image using a Metal shader, bind the [`metalTexture`](ciimageprocessoroutput/metaltexture.md) property as an attachment in a render pass or as an output texture in a compute pass. Or, if you process the image using a CPU-based routine, write processed pixel data to memory using the [`baseAddress`](ciimageprocessoroutput/baseaddress.md) pointer. You must provide rendered output to one (and only one) of the properties listed in [`Providing Output Image Data`](ciimageprocessoroutput#Providing-Output-Image-Data.md).

To access input pixel data in your image processor block, see the [`CIImageProcessorInput`](ciimageprocessorinput.md) class.

## Topics

### Providing Output Image Data
- [var baseAddress: UnsafeMutableRawPointer](ciimageprocessoroutput/baseaddress.md)
  The base address of CPU memory that your Core Image Processor Kernel can write pixels to.
- [var metalTexture: (any MTLTexture)?](ciimageprocessoroutput/metaltexture.md)
  A Metal texture object that can be bound for output using Metal.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessoroutput/pixelbuffer.md)
  An output pixelBuffer object that your Core Image Processor Kernel can write to.
- [var surface: IOSurfaceRef](ciimageprocessoroutput/surface.md)
  An output surface object that your Core Image Processor Kernel can write to.
### Getting Supplemental Information for Image Processing
- [var region: CGRect](ciimageprocessoroutput/region.md)
  The rectangular region of the output image that your Core Image Processor Kernel must provide.
- [var metalCommandBuffer: (any MTLCommandBuffer)?](ciimageprocessoroutput/metalcommandbuffer.md)
  Returns a Metal command buffer object that can be used for encoding commands.
- [var bytesPerRow: Int](ciimageprocessoroutput/bytesperrow.md)
  The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.
- [var format: CIFormat](ciimageprocessoroutput/format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.
### Instance Properties
- [var digest: UInt64](ciimageprocessoroutput/digest.md)
  A 64-bit digest that uniquely describes the contents of the output of a processor.

## See Also

- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorInput](ciimageprocessorinput.md)
  A container of image data and information for use in a custom image processor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput)*