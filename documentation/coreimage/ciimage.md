# CIImage

**Framework**: Core Image  
**Kind**: class

A representation of an image to be processed or produced by Core Image filters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIImage
```

## Mentions

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)
- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)
- [Customizing Image Transitions](customizing-image-transitions.md)

#### Overview

You use `CIImage` objects in conjunction with other Core Image classes—such as [`CIFilter`](cifilter-swift.class.md), [`CIContext`](cicontext.md), [`CIVector`](civector.md), and [`CIColor`](cicolor.md)—to take advantage of the built-in Core Image filters when processing images. You can create `CIImage` objects with data supplied from a variety of sources, including Quartz 2D images, Core Video image buffers ([`CVImageBuffer`](https://developer.apple.com/documentation/CoreVideo/CVImageBuffer)), URL-based objects, and `NSData` objects.

Although a `CIImage` object has image data associated with it, it is not an image. You can think of a `CIImage` object as an image “recipe.” A `CIImage` object has all the information necessary to produce an image, but Core Image doesn’t actually render an image until it is told to do so. This lazy evaluation allows Core Image to operate as efficiently as possible. To show a `CIImage` object as an on-screen image, you can display it as a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) in [`UIImageView`](https://developer.apple.com/documentation/UIKit/UIImageView):

`CIContext`  and `CIImage` objects are immutable, which means each can be shared safely among threads. Multiple threads can use the same GPU or CPU `CIContext` object to render `CIImage` objects.  However, this is not the case for `CIFilter` objects, which are mutable. A `CIFilter` object cannot be shared safely among threads.  If you app is multithreaded, each thread must create its own `CIFilter` objects. Otherwise, your app could behave unexpectedly.

Core Image also provides auto-adjustment methods. These methods analyze an image for common deficiencies and return a set of filters to correct those deficiencies. The filters are preset with values for improving image quality by altering values for skin tones, saturation, contrast, and shadows and for removing red-eye or other artifacts caused by flash. (See Getting Autoadjustment Filters.)

For a discussion of all the methods you can use to create `CIImage` objects on iOS and macOS, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Topics

### Creating an Image
- [class func empty() -> CIImage](ciimage/empty.md)
  Creates and returns an empty image object.
- [init?(image: UIImage)](ciimage/init(image:).md)
  Initializes an image object with the specified UIKit image object.
- [init?(image: UIImage, options: [CIImageOption : Any]?)](ciimage/init(image:options:).md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [init?(contentsOf: URL)](ciimage/init(contentsof:).md)
  Initializes an image object by reading an image from a URL.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](ciimage/init(contentsof:options:).md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [init(cgImage: CGImage)](ciimage/init(cgimage:).md)
  Initializes an image object with a Quartz 2D image.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](ciimage/init(cgimage:options:).md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](ciimage/init(cgimagesource:index:options:).md)
- [init?(data: Data)](ciimage/init(data:).md)
  Initializes an image object with the supplied image data.
- [init?(data: Data, options: [CIImageOption : Any]?)](ciimage/init(data:options:).md)
  Initializes an image object with the supplied image data, using the specified options.
- [init(bitmapData: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](ciimage/init(bitmapdata:bytesperrow:size:format:colorspace:).md)
  Initializes an image object with bitmap data.
- [init?(bitmapImageRep: NSBitmapImageRep)](ciimage/init(bitmapimagerep:).md)
  Initializes an image object with the specified bitmap image representation.
- [init(imageProvider: Any, size: Int, Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]?)](ciimage/init(imageprovider:size:_:format:colorspace:options:).md)
  Initializes an image object with  data provided by an image provider, using the specified options.
- [init?(depthData: AVDepthData)](ciimage/init(depthdata:).md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](ciimage/init(depthdata:options:).md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](ciimage/init(portaiteffectsmatte:).md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte, options: [CIImageOption : Any]?)](ciimage/init(portaiteffectsmatte:options:).md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte)](ciimage/init(semanticsegmentationmatte:).md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte, options: [CIImageOption : Any]?)](ciimage/init(semanticsegmentationmatte:options:).md)
- [init(cvImageBuffer: CVImageBuffer)](ciimage/init(cvimagebuffer:).md)
  Initializes an image object from the contents of a Core Video image buffer.
- [init(cvImageBuffer: CVImageBuffer, options: [CIImageOption : Any]?)](ciimage/init(cvimagebuffer:options:).md)
  Initializes an image object from the contents of a Core Video image buffer, using the specified options.
- [init(cvPixelBuffer: CVPixelBuffer)](ciimage/init(cvpixelbuffer:).md)
  Initializes an image object from the contents of a Core Video pixel buffer.
- [init(cvPixelBuffer: CVPixelBuffer, options: [CIImageOption : Any]?)](ciimage/init(cvpixelbuffer:options:).md)
  Initializes an image object from the contents of a Core Video pixel buffer using the specified options.
- [init?(mtlTexture: any MTLTexture, options: [CIImageOption : Any]?)](ciimage/init(mtltexture:options:).md)
  Initializes an image object with data supplied by a Metal texture.
- [init(ioSurface: IOSurfaceRef)](ciimage/init(iosurface:).md)
  Initializes an image with the contents of an IOSurface.
- [init(ioSurface: IOSurfaceRef, options: [CIImageOption : Any]?)](ciimage/init(iosurface:options:).md)
  Initializes, using the specified options, an image with the contents of an IOSurface.
### Creating an Image by Modifying an Existing Image
- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](ciimage/applyingfilter(_:parameters:).md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](ciimage/applyingfilter(_:).md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](ciimage/transformed(by:).md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](ciimage/transformed(by:highqualitydownsample:).md)
- [func cropped(to: CGRect) -> CIImage](ciimage/cropped(to:).md)
  Returns a new image with a cropped portion of the original image.
- [func oriented(forExifOrientation: Int32) -> CIImage](ciimage/oriented(forexiforientation:).md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
- [func clampedToExtent() -> CIImage](ciimage/clampedtoextent.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](ciimage/clamped(to:).md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](ciimage/composited(over:).md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](ciimage/convertingworkingspacetolab.md)
- [func convertingLabToWorkingSpace() -> CIImage](ciimage/convertinglabtoworkingspace.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](ciimage/matchedtoworkingspace(from:).md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](ciimage/matchedfromworkingspace(to:).md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](ciimage/premultiplyingalpha.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](ciimage/unpremultiplyingalpha.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](ciimage/settingalphaone(in:).md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
- [func applyingGaussianBlur(sigma: Double) -> CIImage](ciimage/applyinggaussianblur(sigma:).md)
  Returns a new image created by applying a Gaussian Blur filter to the image.
- [func settingProperties([AnyHashable : Any]) -> CIImage](ciimage/settingproperties(_:).md)
  Returns a new image created by adding the specified metadata properties to the image.
- [func insertingIntermediate() -> CIImage](ciimage/insertingintermediate.md)
  Returns a new image created by inserting an intermediate.
- [func insertingIntermediate(cache: Bool) -> CIImage](ciimage/insertingintermediate(cache:).md)
  Returns a new image created by inserting a cacheable intermediate.
### Creating Solid Colors
- [init(color: CIColor)](ciimage/init(color:).md)
  Initializes an image of infinite extent whose entire content is the specified color.
- [class var black: CIImage](ciimage/black.md)
- [class var blue: CIImage](ciimage/blue.md)
- [class var clear: CIImage](ciimage/clear.md)
- [class var cyan: CIImage](ciimage/cyan.md)
- [class var gray: CIImage](ciimage/gray.md)
- [class var green: CIImage](ciimage/green.md)
- [class var magenta: CIImage](ciimage/magenta.md)
- [class var red: CIImage](ciimage/red.md)
- [class var white: CIImage](ciimage/white.md)
- [class var yellow: CIImage](ciimage/yellow.md)
### Getting Image Information
- [var definition: CIFilterShape](ciimage/definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/properties.md)
  A dictionary containing metadata about the image.
- [var url: URL?](ciimage/url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/orientationtransform(forexiforientation:).md)
  Returns the transformation needed to reorient the image to the specified orientation.
### Drawing Images
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/draw(at:from:operation:fraction:).md)
  Draws all or part of the image at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/draw(in:from:operation:fraction:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system
### Getting Autoadjustment Filters
- [func autoAdjustmentFilters() -> [CIFilter]](ciimage/autoadjustmentfilters.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]?) -> [CIFilter]](ciimage/autoadjustmentfilters(options:).md)
  Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](autoadjustment-keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](ciimage/autoadjustmentfilters(options:).md) method.
### Working with Filter Regions of Interest
- [func regionOfInterest(for: CIImage, in: CGRect) -> CGRect](ciimage/regionofinterest(for:in:).md)
  Returns the region of interest for the filter chain that generates the image.
### Working with Orientation
- [func oriented(CGImagePropertyOrientation) -> CIImage](ciimage/oriented(_:).md)
  Transforms the original image by a given orientation.
- [func orientationTransform(for: CGImagePropertyOrientation) -> CGAffineTransform](ciimage/orientationtransform(for:).md)
  The affine transform for changing the image to the given orientation.
### Sampling the Image
- [func samplingNearest() -> CIImage](ciimage/samplingnearest.md)
  Samples the image using nearest-neighbor and returns the result.
- [func samplingLinear() -> CIImage](ciimage/samplinglinear.md)
  Samples the image using bilinear interpolation and returns the result.
### Accessing Original Image Content
- [var cgImage: CGImage?](ciimage/cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](ciimage/pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](ciimage/depthdata.md)
  Depth data associated with the image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/portraiteffectsmatte.md)
  The portrait effects matte associated with the image.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/semanticsegmentationmatte.md)
### Image Dictionary Keys
- [struct CIImageOption](ciimageoption.md)
### AutoAdjustment Keys
- [struct CIImageAutoAdjustmentOption](ciimageautoadjustmentoption.md)
### Deprecated
- [init(cgLayer: CGLayer)](ciimage/init(cglayer:).md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/init(cglayer:options:).md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/init(texture:size:flipped:colorspace:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/init(texture:size:flipped:options:).md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/init(iosurface:plane:format:options:).md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/textureformat.md)
  The key for an OpenGL texture format.
### Instance Properties
- [var contentHeadroom: Float](ciimage/contentheadroom.md)
- [var isOpaque: Bool](ciimage/isopaque.md)
- [var metalTexture: (any MTLTexture)?](ciimage/metaltexture.md)
- [var contentAverageLightLevel: Float](ciimage/contentaveragelightlevel.md)
  Returns the content average light level of the image.
### Instance Methods
- [func applyingGainMap(CIImage) -> CIImage](ciimage/applyinggainmap(_:).md)
- [func applyingGainMap(CIImage, headroom: Float) -> CIImage](ciimage/applyinggainmap(_:headroom:).md)
- [func insertingTiledIntermediate() -> CIImage](ciimage/insertingtiledintermediate.md)
  Create an image that inserts a intermediate that is cached in tiles
- [func settingContentAverageLightLevel(Float) -> CIImage](ciimage/settingcontentaveragelightlevel(_:).md)
  Create an image by changing the receiver’s contentAverageLightLevel property.
- [func settingContentHeadroom(Float) -> CIImage](ciimage/settingcontentheadroom(_:).md)
  Create an image by changing the receiver’s contentHeadroom property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIContext](cicontext.md)
  An evaluation context for rendering image processing results and performing image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage)*