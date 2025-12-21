# CIContext

**Framework**: Core Image  
**Kind**: class

The Core Image context class provides an evaluation context for Core Image processing with Metal, OpenGL, or OpenCL.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIContext
```

## Mentions

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)

#### Overview

You use a `CIContext` instance to render a [`CIImage`](ciimage.md) instance which represents a graph of image processing operations which are built using other Core Image classes, such as [`CIFilter`](cifilter-swift.class.md), [`CIKernel`](cikernel.md), [`CIColor`](cicolor.md) and [`CIImage`](ciimage.md). You can also use a `CIContext` with the [`CIDetector`](cidetector.md) class to analyze images — for example, to detect faces or barcodes.

Contexts support automatic color management by performing all processing operations in a working color space. This means that unless told otherwise:

- All input images are color matched from the input’s color space to the working space.
- All renders are color matched from the working space to the destination space. (For more information on `CGColorSpace` see [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace))

`CIContext` and [`CIImage`](ciimage.md) instances are immutable, so multiple threads can use the same [`CIContext`](cicontext.md) instance to render [`CIImage`](ciimage.md) instances. However, [`CIFilter`](cifilter-swift.class.md) instances are mutable and thus cannot be shared safely among threads. Each thread must take case not to access or modify a [`CIFilter`](cifilter-swift.class.md) instance while it is being used by another thread.

The `CIContext` manages various internal state such as `MTLCommandQueue` and caches for compiled kernels and intermediate buffers.  For this reason it is not recommended to create many `CIContext` instances.  As a rule, it recommended that you create one `CIContext` instance for each view that renders [`CIImage`](ciimage.md) or each background task.

## Topics

### Creating a Context Without Specifying a Destination
- [init()](cicontext/init.md)
  Initializes a context without a specific rendering destination, using default options.
### Creating a Context for CPU-Based Rendering
- [init(cgContext: CGContext, options: [CIContextOption : Any]?)](cicontext/init(cgcontext:options:).md)
  Creates a Core Image context from a Quartz context, using the specified options.
### Creating a Context for GPU-Based Rendering
- [init(mtlDevice: any MTLDevice)](cicontext/init(mtldevice:).md)
  Creates a Core Image context using the specified Metal device.
- [init(mtlDevice: any MTLDevice, options: [CIContextOption : Any]?)](cicontext/init(mtldevice:options:).md)
  Creates a Core Image context using the specified Metal device and options.
- [init(mtlCommandQueue: any MTLCommandQueue)](cicontext/init(mtlcommandqueue:).md)
- [init(mtlCommandQueue: any MTLCommandQueue, options: [CIContextOption : Any]?)](cicontext/init(mtlcommandqueue:options:).md)
### Rendering Images
- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/createcgimage(_:from:).md)
  Creates a Core Graphics image from a region of a Core Image image instance.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](cicontext/createcgimage(_:from:format:colorspace:).md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](cicontext/createcgimage(_:from:format:colorspace:deferred:).md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:).md)
  Renders to the given bitmap.
- [func render(CIImage, to: CVPixelBuffer)](cicontext/render(_:to:).md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-2k8l2.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-54b9l.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/render(_:to:commandbuffer:bounds:colorspace:).md)
  Renders a region of an image to a Metal texture.
### Drawing Images
- [func draw(CIImage, in: CGRect, from: CGRect)](cicontext/draw(_:in:from:).md)
  Renders a region of an image to a rectangle in the context destination.
### Determining the Allowed Extents for Images Used by a Context
- [func inputImageMaximumSize() -> CGSize](cicontext/inputimagemaximumsize.md)
  Returns the maximum size allowed for any image rendered into the context.
- [func outputImageMaximumSize() -> CGSize](cicontext/outputimagemaximumsize.md)
  Returns the maximum size allowed for any image created by the context.
### Managing Resources
- [func clearCaches()](cicontext/clearcaches.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](cicontext/reclaimresources.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](cicontext/offlinegpucount.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](cicontext/workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](cicontext/workingformat.md)
  The working pixel format of the Core Image context.
### Rendering Images for Data or File Export
- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/tiffrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/jpegrepresentation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/pngrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/heifrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/heif10representation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/openexrrepresentation(of:options:).md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writetiffrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writejpegrepresentation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writepngrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheifrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheif10representation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeopenexrrepresentation(of:to:options:).md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](ciimagerepresentationoption.md)
### Creating Depth Blur Filters
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, glassesMatte: CIImage?, gainMap: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:glassesmatte:gainmap:orientation:options:).md)
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, hairSemanticSegmentation: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:hairsemanticsegmentation:orientation:options:).md)
- [func depthBlurEffectFilter(for: CIImage, disparityImage: CIImage, portraitEffectsMatte: CIImage?, orientation: CGImagePropertyOrientation, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(for:disparityimage:portraiteffectsmatte:orientation:options:).md)
- [func depthBlurEffectFilter(forImageData: Data, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(forimagedata:options:).md)
- [func depthBlurEffectFilter(forImageURL: URL, options: [AnyHashable : Any]?) -> CIFilter?](cicontext/depthblureffectfilter(forimageurl:options:).md)
### Constants
- [struct CIContextOption](cicontextoption.md)
  An enum string type that your code can use to select different options when creating a Core Image context.
### Customizing Render Destination
- [func prepareRender(CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws](cicontext/preparerender(_:from:to:at:).md)
  An optional call to warm up a [`CIContext`](cicontext.md) so that subsequent calls to render with the same arguments run more efficiently.
- [func startTask(toClear: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(toclear:).md)
  Fills the entire destination with black or clear depending on its [`alphaMode`](cirenderdestination/alphamode.md).
- [func startTask(toRender: CIImage, from: CGRect, to: CIRenderDestination, at: CGPoint) throws -> CIRenderTask](cicontext/starttask(torender:from:to:at:).md)
  Renders a portion of an image to a point in the destination.
- [func startTask(toRender: CIImage, to: CIRenderDestination) throws -> CIRenderTask](cicontext/starttask(torender:to:).md)
  Renders an image to a destination so that point (0, 0) of the image maps to point (0, 0) of the destination.
### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/init(cglcontext:pixelformat:colorspace:options:).md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](cicontext/init(eaglcontext:).md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/init(eaglcontext:options:).md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32)](cicontext/init(forofflinegpuatindex:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](cicontext/createcglayer(with:info:).md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/draw(_:at:from:).md)
  Renders a region of an image to a point in the context destination.
### Initializers
- [init(options: [CIContextOption : Any]?)](cicontext/init(options:).md)
  Initializes a context without a specific rendering destination, using the specified options.
### Instance Methods
- [func calculateHDRStats(for: CGImage) -> CGImage](cicontext/calculatehdrstats(for:)-3ia7r.md)
  Given a Core Graphics image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Graphics image that has the calculated values.
- [func calculateHDRStats(for: IOSurfaceRef)](cicontext/calculatehdrstats(for:)-6lwmz.md)
  Given an IOSurface, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the surface’s attachments to store the values.
- [func calculateHDRStats(for: CVPixelBuffer)](cicontext/calculatehdrstats(for:)-7bcki.md)
  Given a CVPixelBuffer, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then update the buffers’s attachments to store the values.
- [func calculateHDRStats(for: CIImage) -> CIImage?](cicontext/calculatehdrstats(for:)-l1rj.md)
  Given a Core Image image, use the receiving Core Image context to calculate its HDR statistics (content headroom and content average light level) and then return a new Core Image image that has the calculated values.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool, calculateHDRStats: Bool) -> CGImage?](cicontext/createcgimage(_:from:format:colorspace:deferred:calculatehdrstats:).md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for calculating HDR statistics.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIImage](ciimage.md)
  A representation of an image to be processed or produced by Core Image filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext)*