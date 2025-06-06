# CIContext

**Framework**: Core Image  
**Kind**: cl

An evaluation context for rendering image processing results and performing image analysis.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIContext : NSObject
```

#### Overview

The [`CIContext`](cicontext.md) class provides an evaluation context for Core Image processing with Quartz 2D, Metal, or OpenGL. You use [`CIContext`](cicontext.md) objects in conjunction with other Core Image classes, such as [`CIFilter`](cifilter.md), [`CIImage`](ciimage.md), and [`CIColor`](cicolor.md), to process images using Core Image filters. You also use a Core Image context with the [`CIDetector`](cidetector.md) class to analyze images—for example, to detect faces or barcodes.

[`CIContext`](cicontext.md) and [`CIImage`](ciimage.md) objects are immutable, so multiple threads can use the same [`CIContext`](cicontext.md) object to render [`CIImage`](ciimage.md) objects. However, [`CIFilter`](cifilter.md) objects are mutable and thus cannot be shared safely among threads. Each thread must create its own [`CIFilter`](cifilter.md) objects, but you can pass a filter’s immutable input and output [`CIImage`](ciimage.md) objects between threads.

## Topics

### Creating a Context Without Specifying a Destination
- [init()](cicontext/1642212-init.md)
  Initializes a context without a specific rendering destination, using default options.
- [init(options: [CIContextOption : Any]?)](cicontext/1438261-init.md)
  Initializes a context without a specific rendering destination, using the specified options.
### Creating a Context for CPU-Based Rendering
- [init(cgContext: CGContext, options: [CIContextOption : Any]?)](cicontext/1437864-init.md)
  Creates a Core Image context from a Quartz context, using the specified options.
### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](cicontext/1437609-init.md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](cicontext/1437711-init.md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](cicontext/3365984-init.md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](cicontext/3365985-init.md)
### Rendering Images
- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/1437784-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](cicontext/1437978-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](cicontext/1642211-createcgimage.md)
  Creates a Quartz 2D image from a region of a Core Image image object with deferred rendering.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/1437897-render.md)
  Renders to the given bitmap. 
- [func render(CIImage, to: CVPixelBuffer)](cicontext/1437853-render.md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/1437835-render.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/1437778-render.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/1438026-render.md)
  Renders a region of an image to a Metal texture.
### Drawing Images
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/1473521-draw.md)
  Renders a region of an image to a point in the context destination.
- [func draw(CIImage, in: CGRect, from: CGRect)](cicontext/1437786-draw.md)
  Renders a region of an image to a rectangle in the context destination.
### Determining the Allowed Extents for Images Used by a Context
- [func inputImageMaximumSize() -> CGSize](cicontext/1620425-inputimagemaximumsize.md)
  Returns the maximum size allowed for any image rendered into the context.
- [func outputImageMaximumSize() -> CGSize](cicontext/1620335-outputimagemaximumsize.md)
  Returns the maximum size allowed for any image created by the context.
### Managing Resources
- [func clearCaches()](cicontext/1437790-clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/1437967-reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/1437817-offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](cicontext/1438061-workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/1642215-workingformat.md)
  The working pixel format of the Core Image context.
### Rendering Images for Data or File Export
- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/1642220-tiffrepresentation.md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/1642214-jpegrepresentation.md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/2866196-pngrepresentation.md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/2902269-heifrepresentation.md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data](cicontext/3762899-heif10representation.md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) -> Data](cicontext/4210204-openexrrepresentation.md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/1642213-writetiffrepresentation.md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/1642218-writejpegrepresentation.md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/2866197-writepngrepresentation.md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/2902266-writeheifrepresentation.md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any])](cicontext/3762900-writeheif10representation.md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any])](cicontext/4210205-writeopenexrrepresentation.md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](ciimagerepresentationoption.md)
### Creating Depth Blur Filters
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/3600105-depthblureffectfilter.md)
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/3228045-depthblureffectfilter.md)
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/3019315-depthblureffectfilter.md)
- [func depthBlurEffectFilter(forImageData: Data, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/3020629-depthblureffectfilter.md)
- [func depthBlurEffectFilter(forImageURL: URL, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/3019316-depthblureffectfilter.md)
### Constants
- [struct CIContextOption](cicontextoption.md)
### Customizing Render Destination
- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint)](cicontext/2875428-preparerender.md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) -> CIRenderTask](cicontext/2875450-starttask.md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/2875443-alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) -> CIRenderTask](cicontext/2875448-starttask.md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) -> CIRenderTask](cicontext/2875429-starttask.md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/1438137-init.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/1620419-init.md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/1620362-init.md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAt: UInt32)](cicontext/1437772-init.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAt: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/1437758-init.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](cicontext/1438267-createcglayer.md)
  Creates a CGLayer object from the provided parameters.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)

## See Also

- [Processing an Image Using Built-in Filters](processing_an_image_using_built-in_filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIImage](ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext)*