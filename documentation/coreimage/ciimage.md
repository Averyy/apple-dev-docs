# CIImage

**Framework**: Core Image  
**Kind**: cl

A representation of an image to be processed or produced by Core Image filters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIImage : NSObject
```

#### Overview

You use [`CIImage`](ciimage.md) objects in conjunction with other Core Image classes—such as [`CIFilter`](cifilter.md), [`CIContext`](cicontext.md), [`CIVector`](civector.md), and [`CIColor`](cicolor.md)—to take advantage of the built-in Core Image filters when processing images. You can create [`CIImage`](ciimage.md) objects with data supplied from a variety of sources, including Quartz 2D images, Core Video image buffers ([`CVImageBuffer`](https://developer.apple.com/documentation/corevideo/cvimagebuffer)), URL-based objects, and `NSData` objects.

Although a [`CIImage`](ciimage.md) object has image data associated with it, it is not an image. You can think of a [`CIImage`](ciimage.md) object as an image “recipe.” A [`CIImage`](ciimage.md) object has all the information necessary to produce an image, but Core Image doesn’t actually render an image until it is told to do so. This lazy evaluation allows Core Image to operate as efficiently as possible. 

[`CIContext`](cicontext.md)  and [`CIImage`](ciimage.md) objects are immutable, which means each can be shared safely among threads. Multiple threads can use the same GPU or CPU [`CIContext`](cicontext.md) object to render [`CIImage`](ciimage.md) objects.  However, this is not the case for `CIFilter` objects, which are mutable. A `CIFilter` object cannot be shared safely among threads.  If you app is multithreaded, each thread must create its own `CIFilter` objects. Otherwise, your app could behave unexpectedly.

Core Image also provides auto-adjustment methods. These methods analyze an image for common deficiencies and return a set of filters to correct those deficiencies. The filters are preset with values for improving image quality by altering values for skin tones, saturation, contrast, and shadows and for removing red-eye or other artifacts caused by flash. (See [`Getting Autoadjustment Filters`](ciimage#1652741.md).)

For a discussion of all the methods you can use to create [`CIImage`](ciimage.md) objects on iOS and macOS, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

## Topics

### Creating an Image
- [class func empty() -> CIImage](ciimage/1438023-empty.md)
  Creates and returns an empty image object.
- [init?(image: UIImage)](ciimage/1624119-init.md)
  Initializes an image object with the specified UIKit image object.
- [init?(image: UIImage, options: [CIImageOption : Any]?)](ciimage/1624098-init.md)
  Initializes an image object with the specified UIKit image object, using the specified options.
- [init?(contentsOf: URL)](ciimage/1437908-init.md)
  Initializes an image object by reading an image from a URL.
- [init?(contentsOf: URL, options: [CIImageOption : Any]?)](ciimage/1437867-init.md)
  Initializes an image object by reading an image from a URL, using the specified options.
- [init(cgImage: CGImage)](ciimage/1437986-init.md)
  Initializes an image object with a Quartz 2D image.
- [init(cgImage: CGImage, options: [CIImageOption : Any]?)](ciimage/1437764-init.md)
  Initializes an image object with a Quartz 2D image, using the specified options.
- [init(cgImageSource: CGImageSource, index: Int, options: [CIImageOption : Any]?)](ciimage/3152399-init.md)
- [init?(data: Data)](ciimage/1437925-init.md)
  Initializes an image object with the supplied image data.
- [init?(data: Data, options: [CIImageOption : Any]?)](ciimage/1438032-init.md)
  Initializes an image object with the supplied image data, using the specified options.
- [init(bitmapData: Data, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](ciimage/1437857-init.md)
  Initializes an image object with bitmap data. 
- [init?(bitmapImageRep: NSBitmapImageRep)](ciimage/1535335-init.md)
  Initializes an image object with the specified bitmap image representation.
- [init(imageProvider: Any, size: Int, Int, format: CIFormat, colorSpace: CGColorSpace?, options: [CIImageOption : Any]?)](ciimage/1437868-init.md)
  Initializes an image object with  data provided by an image provider, using the specified options. 
- [init?(depthData: AVDepthData)](ciimage/2998421-init.md)
- [init?(depthData: AVDepthData, options: [String : Any]?)](ciimage/2998422-init.md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte)](ciimage/2998423-init.md)
- [init?(portaitEffectsMatte: AVPortraitEffectsMatte, options: [CIImageOption : Any]?)](ciimage/2998424-init.md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte)](ciimage/3242779-init.md)
- [init?(semanticSegmentationMatte: AVSemanticSegmentationMatte, options: [CIImageOption : Any]?)](ciimage/3242780-init.md)
- [init(cvImageBuffer: CVImageBuffer)](ciimage/1438012-init.md)
  Initializes an image object from the contents of a Core Video image buffer.
- [init(cvImageBuffer: CVImageBuffer, options: [CIImageOption : Any]?)](ciimage/1437617-init.md)
  Initializes an image object from the contents of a Core Video image buffer, using the specified options.
- [init(cvPixelBuffer: CVPixelBuffer)](ciimage/1438072-init.md)
  Initializes an image object from the contents of a Core Video pixel buffer.
- [init(cvPixelBuffer: CVPixelBuffer, options: [CIImageOption : Any]?)](ciimage/1438209-init.md)
  Initializes an image object from the contents of a Core Video pixel buffer using the specified options.
- [init?(mtlTexture: any MTLTexture, options: [CIImageOption : Any]?)](ciimage/1437890-init.md)
  Initializes an image object with data supplied by a Metal texture.
- [init(ioSurface: IOSurfaceRef)](ciimage/1438030-init.md)
  Initializes an image with the contents of an IOSurface.
- [init(ioSurface: IOSurfaceRef, options: [CIImageOption : Any]?)](ciimage/1438181-init.md)
  Initializes, using the specified options, an image with the contents of an IOSurface.
### Creating an Image by Modifying an Existing Image
- [func applyingFilter(String, parameters: [String : Any]) -> CIImage](ciimage/1437589-applyingfilter.md)
  Returns a new image created by applying a filter to the original image with the specified name and parameters.
- [func applyingFilter(String) -> CIImage](ciimage/2915368-applyingfilter.md)
  Applies the filter to an image and returns the output.
- [func transformed(by: CGAffineTransform) -> CIImage](ciimage/1438203-transformed.md)
  Returns a new image that represents the original image after applying an affine transform.
- [func transformed(by: CGAffineTransform, highQualityDownsample: Bool) -> CIImage](ciimage/3334939-transformed.md)
- [func cropped(to: CGRect) -> CIImage](ciimage/1437833-cropped.md)
  Returns a new image with a cropped portion of the original image.
- [func oriented(forExifOrientation: Int32) -> CIImage](ciimage/1438223-oriented.md)
  Returns a new image created by transforming the original image to the specified EXIF orientation.
- [func clampedToExtent() -> CIImage](ciimage/1437628-clampedtoextent.md)
  Returns a new image created by making the pixel colors along its edges extend infinitely in all directions.
- [func clamped(to: CGRect) -> CIImage](ciimage/1645893-clamped.md)
  Returns a new image created by cropping to a specified area, then making the pixel colors along the edges of the cropped image extend infinitely in all directions.
- [func composited(over: CIImage) -> CIImage](ciimage/1437837-composited.md)
  Returns a new image created by compositing the original image over the specified destination image.
- [func convertingWorkingSpaceToLab() -> CIImage](ciimage/3975704-convertingworkingspacetolab.md)
- [func convertingLabToWorkingSpace() -> CIImage](ciimage/3975703-convertinglabtoworkingspace.md)
- [func matchedToWorkingSpace(from: CGColorSpace) -> CIImage?](ciimage/1645896-matchedtoworkingspace.md)
  Returns a new image created by color matching from the specified color space to the context’s working color space.
- [func matchedFromWorkingSpace(to: CGColorSpace) -> CIImage?](ciimage/1645898-matchedfromworkingspace.md)
  Returns a new image created by color matching from the context’s working color space to the specified color space.
- [func premultiplyingAlpha() -> CIImage](ciimage/1645894-premultiplyingalpha.md)
  Returns a new image created by multiplying the image’s RGB values by its alpha values.
- [func unpremultiplyingAlpha() -> CIImage](ciimage/1645892-unpremultiplyingalpha.md)
  Returns a new image created by dividing the image’s RGB values by its alpha values.
- [func settingAlphaOne(in: CGRect) -> CIImage](ciimage/1645891-settingalphaone.md)
  Returns a new image created by setting all alpha values to 1.0 within the specified rectangle and to 0.0 outside of that area.
- [func applyingGaussianBlur(sigma: Double) -> CIImage](ciimage/1645897-applyinggaussianblur.md)
  Returns a new image created by applying a Gaussian Blur filter to the image.
- [func settingProperties([AnyHashable : Any]) -> CIImage](ciimage/1645895-settingproperties.md)
  Returns a new image created by adding the specified metadata properties to the image.
- [func insertingIntermediate() -> CIImage](ciimage/2966521-insertingintermediate.md)
  Returns a new image created by inserting an intermediate.
- [func insertingIntermediate(cache: Bool) -> CIImage](ciimage/2966522-insertingintermediate.md)
  Returns a new image created by inserting a cacheable intermediate.
### Creating Solid Colors
- [init(color: CIColor)](ciimage/1437947-init.md)
  Initializes an image of infinite extent whose entire content is the specified color.
- [class var black: CIImage](ciimage/3074421-black.md)
- [class var blue: CIImage](ciimage/3074422-blue.md)
- [class var clear: CIImage](ciimage/3074423-clear.md)
- [class var cyan: CIImage](ciimage/3074424-cyan.md)
- [class var gray: CIImage](ciimage/3074425-gray.md)
- [class var green: CIImage](ciimage/3074426-green.md)
- [class var magenta: CIImage](ciimage/3074427-magenta.md)
- [class var red: CIImage](ciimage/3074428-red.md)
- [class var white: CIImage](ciimage/3074429-white.md)
- [class var yellow: CIImage](ciimage/3074430-yellow.md)
### Getting Image Information
- [var definition: CIFilterShape](ciimage/1437804-definition.md)
  Returns a filter shape object that represents the domain of definition of the image.
- [var extent: CGRect](ciimage/1437996-extent.md)
  A rectangle that specifies the extent of the image.
- [var properties: [String : Any]](ciimage/1437733-properties.md)
  A dictionary containing metadata about the image.
- [var url: URL?](ciimage/1438195-url.md)
  The URL from which the image was loaded.
- [var colorSpace: CGColorSpace?](ciimage/1437750-colorspace.md)
  The color space of the image.
- [func orientationTransform(forExifOrientation: Int32) -> CGAffineTransform](ciimage/1437930-orientationtransform.md)
  Returns the transformation needed to reorient the image to the specified orientation.
### Drawing Images
- [func draw(at: NSPoint, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/1534432-draw.md)
  Draws all or part of the image at the specified point in the current coordinate system. 
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat)](ciimage/1534407-draw.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system
### Getting Autoadjustment Filters
- [func autoAdjustmentFilters() -> [CIFilter]](ciimage/1645889-autoadjustmentfilters.md)
  Returns all possible automatically selected and configured filters for adjusting the image.
- [func autoAdjustmentFilters(options: [CIImageAutoAdjustmentOption : Any]?) -> [CIFilter]](ciimage/1437792-autoadjustmentfilters.md)
  Returns a subset of automatically selected and configured filters for adjusting the image.
- [Autoadjustment Keys](ciimage/autoadjustment_keys.md)
  Constants used as keys in the options dictionary for the [`autoAdjustmentFilters(options:)`](ciimage/1437792-autoadjustmentfilters.md) method.
### Working with Filter Regions of Interest
- [func regionOfInterest(for: CIImage, in: CGRect) -> CGRect](ciimage/1437994-regionofinterest.md)
  Returns the region of interest for the filter chain that generates the image.
### Working with Orientation
- [func oriented(CGImagePropertyOrientation) -> CIImage](ciimage/2919727-oriented.md)
  Transforms the original image by a given [`CGImagePropertyOrientation`](https://developer.apple.com/documentation/imageio/cgimagepropertyorientation) and returns the result.
- [func orientationTransform(for: CGImagePropertyOrientation) -> CGAffineTransform](ciimage/2919726-orientationtransform.md)
  The affine transform for changing the image to the given orientation.
### Sampling the Image
- [func samplingNearest() -> CIImage](ciimage/2867429-samplingnearest.md)
  Samples the image using nearest-neighbor and returns the result.
- [func samplingLinear() -> CIImage](ciimage/2867346-samplinglinear.md)
  Samples the image using bilinear interpolation and returns the result.
### Accessing Original Image Content
- [var cgImage: CGImage?](ciimage/1687603-cgimage.md)
  The CoreGraphics image object this image was created from, if applicable.
- [var pixelBuffer: CVPixelBuffer?](ciimage/1687604-pixelbuffer.md)
  The CoreVideo pixel buffer this image was created from, if applicable.
- [var depthData: AVDepthData?](ciimage/2902251-depthdata.md)
  [`AVDepthData`](https://developer.apple.com/documentation/avfoundation/avdepthdata) representation of the depth image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](ciimage/2976440-portraiteffectsmatte.md)
  [`AVPortraitEffectsMatte`](https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte) representation of portrait effects.
- [var semanticSegmentationMatte: AVSemanticSegmentationMatte?](ciimage/3242781-semanticsegmentationmatte.md)
### Image Dictionary Keys
- [struct CIImageOption](ciimageoption.md)
### AutoAdjustment Keys
- [struct CIImageAutoAdjustmentOption](ciimageautoadjustmentoption.md)
### Deprecated
- [init(cgLayer: CGLayer)](ciimage/1438065-init.md)
  Initializes an image object  from the contents supplied by a CGLayer object.
- [init(cgLayer: CGLayer, options: [CIImageOption : Any]?)](ciimage/1437687-init.md)
  Initializes an image object  from the contents supplied by a CGLayer object, using the  specified options.
- [init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](ciimage/1438015-init.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(texture: UInt32, size: CGSize, flipped: Bool, options: [CIImageOption : Any]?)](ciimage/1437880-init.md)
  Initializes an image object with data supplied by an OpenGL texture.
- [init(ioSurface: IOSurfaceRef, plane: Int, format: CIFormat, options: [CIImageOption : Any]?)](ciimage/1437670-init.md)
  Initializes, using the specified format and options, an image with the contents of a specific data plane in an IOSurface.
- [static let textureTarget: CIImageOption](ciimageoption/1437613-texturetarget.md)
  The key for an OpenGL texture target.
- [static let textureFormat: CIImageOption](ciimageoption/1437934-textureformat.md)
  The key for an OpenGL texture format.
### Instance Properties
- [var contentHeadroom: Float](ciimage/4438508-contentheadroom.md)
- [var isOpaque: Bool](ciimage/4354031-isopaque.md)
- [var metalTexture: (any MTLTexture)?](ciimage/4430013-metaltexture.md)
### Instance Methods
- [func applyingGainMap(CIImage) -> CIImage](ciimage/4354029-applyinggainmap.md)
- [func applyingGainMap(CIImage, headroom: Float) -> CIImage](ciimage/4354030-applyinggainmap.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Processing an Image Using Built-in Filters](processing_an_image_using_built-in_filters.md)
  Apply effects such as sepia tint, highlight strengthening, and scaling to images.
- [class CIContext](cicontext.md)
  An evaluation context for rendering image processing results and performing image analysis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimage)*