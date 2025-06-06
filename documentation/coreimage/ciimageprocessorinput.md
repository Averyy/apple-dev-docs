# CIImageProcessorInput

**Framework**: Core Image  
**Kind**: intf

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

In your image processor class' [`process(with:arguments:output:)`](ciimageprocessorkernel/2138290-process.md) method, use the provided [`CIImageProcessorInput`](ciimageprocessorinput.md) object to access the image data and supporting information to perform your custom image processing routine. For example, if you process the image using a Metal shader, use the [`metalTexture`](ciimageprocessorinput/1639651-metaltexture.md) property to bind the image as an input texture. Or, if you process the image using a CPU-based routine, use the [`baseAddress`](ciimageprocessorinput/1639645-baseaddress.md) property to access pixel data in memory.

To finish setting up or performing your image processing routine, use the provided [`CIImageProcessorOutput`](ciimageprocessoroutput.md) object to return processed pixel data to Core Image.

## Topics

### Accessing Input Image Data
- [var baseAddress: UnsafeRawPointer](ciimageprocessorinput/1639645-baseaddress.md)
  A pointer to the image data in CPU memory to be processed.
- [var metalTexture: (any MTLTexture)?](ciimageprocessorinput/1639651-metaltexture.md)
  A Metal texture containing the image data to be processed.
- [var pixelBuffer: CVPixelBuffer?](ciimageprocessorinput/1639649-pixelbuffer.md)
  A CoreVideo pixel buffer containing the image data to be processed.
- [var surface: IOSurfaceRef](ciimageprocessorinput/1639657-surface.md)
  An IOSurface object containing the image data to be processed.
### Getting Supplemental Information for Image Processing
- [var region: CGRect](ciimageprocessorinput/1639633-region.md)
  The area within the input image to be processed.
- [var bytesPerRow: Int](ciimageprocessorinput/1639655-bytesperrow.md)
  The number of bytes per row of pixels in the input image data.
- [var format: CIFormat](ciimageprocessorinput/1639639-format.md)
  The per-pixel data format of the image to be processed.
### Instance Properties
- [var digest: UInt64](ciimageprocessorinput/4048310-digest.md)
- [var roiTileCount: Int](ciimageprocessorinput/4172814-roitilecount.md)
- [var roiTileIndex: Int](ciimageprocessorinput/4172815-roitileindex.md)

## See Also

- [class CIImageProcessorKernel](ciimageprocessorkernel.md)
  The abstract class you extend to create custom image processors that can integrate with Core Image workflows.
- [protocol CIImageProcessorOutput](ciimageprocessoroutput.md)
  A container for writing image data and information produced by a custom image processor. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput)*