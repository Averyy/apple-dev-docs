# CIFilter

**Framework**: Core Image  
**Kind**: class

An image processor that produces an image by manipulating one or more input images or by generating new image data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class CIFilter
```

## Mentions

- [Processing an Image Using Built-in Filters](processing-an-image-using-built-in-filters.md)
- [Selectively Focusing on an Image](selectively-focusing-on-an-image.md)
- [Customizing Image Transitions](customizing-image-transitions.md)

#### Overview

The `CIFilter` class produces a [`CIImage`](ciimage.md) object as output. Typically, a filter takes one or more images as input. Some filters, however, generate an image based on other types of input parameters. The par`CIFilter` swift.class` object are set and retrieved through the use of key-value pairs.

You use the `CIFilter` object in conjunction with other Core Image classes, such as  `CIImage`, [`CIContext`](cicontext.md), and [`CIColor`](cicolor.md), to take advantage of the built-in Core Image filters when processing images, creating filter generators, or writing custom filters.

`CIFilter` objects are mutable, and thus cannot be shared safely among threads. Each thread must create its own `CIFilter` objects, but you can pass a filter’s immutable input and output `CIImage` objects between threads.

To get a quick overview of how to set up and use Core Image filters, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

##### Create Type Safe Filters

Core Image provides methods that create type-safe `CIFilter` instances. Use these filters to avoid run-time errors that can occur when relying on Core Image’s string-based API.

To use the type-safe API, import `CoreImage.CIFilterBuiltins`:

```swift
#import <CoreImage/CoreImage.h>
#import <CoreImage/CIFilterBuiltins.h>
```

The type-safe approach returns a non-optional filter. Because the returned filter conforms to the relevant protocol—for example, [`CIFalseColor`](cifalsecolor.md) in the case of [`falseColorFilter`](cifilter-swift.class/falsecolorfilter.md)—the parameters are available as properties. The following creates and applies a false color filter:

```swift
- (CIImage *) falseColorImage:(CIImage*) inputImage {
    CIFilter<CIFalseColor> *falseColorFilter = CIFilter.falseColorFilter;
    falseColorFilter.color0 = [CIColor colorWithRed:1 green:1 blue:0];
    falseColorFilter.color1 = [CIColor colorWithRed:0 green:0 blue:1];
    falseColorFilter.inputImage = inputImage;
    return falseColorFilter.outputImage;
}
```

The false color filter maps luminance to a color ramp of two colors:

![Two photographs showing a flower. The image on the left shows the original version of the flower. The image on the right shows the false color version of the flower.](https://docs-assets.developer.apple.com/published/31bc2cc68e11100dbfd10afe19552daa/media-4336877%402x.png)

##### Subclassing Notes

You can subclass `CIFilter` in order to create custom filter effects:

- By chaining together two or more built-in Core Image filters
- By using an image-processing kernel that you write

Regardless of whether your subclass provides its effect by chaining filters or implementing its own kernel, you should:

- Declare any input parameters as properties whose names are prefixed with `input`, such as `inputImage`.
- Override the [`setDefaults()`](cifilter-swift.class/setdefaults().md) methods to provide default values for any input parameters you’ve declared.
- Implement an `outputImage` method to create a new `CIImage` with your filter’s effect.

The `CIFilter` class automatically manages input parameters when archiving, copying, and deallocating filters. For this reason, your subclass must obey the following guidelines to ensure proper behavior:

- Store input parameters in instance variables whose names are prefixed with `input`.

Don’t use auto-synthesized instance variables, because their names are automatically prefixed with an underscore. Instead, synthesize the property manually. For example:

`@synthesize inputMyParameter;`

- If using manual reference counting, don’t release input parameter instance variables in your [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) method implementation. The [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) implementation in the `CIFilter` class uses [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) to automatically set the values of all input parameters to `nil`.

## Topics

### Creating a filter
- [init?(name: String)](cifilter-swift.class/init(name:).md)
  Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter.
- [init?(name: String, withInputParameters: [String : Any]?)](cifilter-swift.class/init(name:withinputparameters:).md)
  Creates a [`CIFilter`](cifilter-swift.class.md) object for a specific kind of filter and initializes the input values.
### Configuring type-safe filters
- [protocol CIFilterProtocol](cifilterprotocol.md)
  The properties you use to configure a Core Image filter.
- [Blur Filters](blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md)
  Apply distortion to images.
- [Generator Filters](generator-filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.
### Accessing registered filters
- [class func filterNames(inCategories: [String]?) -> [String]](cifilter-swift.class/filternames(incategories:).md)
  Returns an array of all published filter names that match all the specified categories.
- [class func filterNames(inCategory: String?) -> [String]](cifilter-swift.class/filternames(incategory:).md)
  Returns an array of all published filter names in the specified category.
### Registering a filter
- [class func registerName(String, constructor: any CIFilterConstructor, classAttributes: [String : Any])](cifilter-swift.class/registername(_:constructor:classattributes:).md)
  Publishes a custom filter that is not packaged as an image unit.
### Getting filter parameters and attributes
- [var name: String](cifilter-swift.class/name.md)
  A name associated with a filter.
- [var isEnabled: Bool](cifilter-swift.class/isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](cifilter-swift.class/attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](cifilter-swift.class/inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter-swift.class/outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](cifilter-swift.class/outputimage.md)
  Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.
### Setting default values
- [func setDefaults()](cifilter-swift.class/setdefaults.md)
  Sets all input values for a filter to default values.
### Applying a filter
- [func apply(CIKernel, arguments: [Any]?, options: [String : Any]?) -> CIImage?](cifilter-swift.class/apply(_:arguments:options:).md)
  Produces a [`CIImage`](ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.
### Getting localized information for registered filters
- [class func localizedName(forFilterName: String) -> String?](cifilter-swift.class/localizedname(forfiltername:).md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](cifilter-swift.class/localizedname(forcategory:).md)
  Returns  the localized name for the specified filter category.
- [class func localizedDescription(forFilterName: String) -> String?](cifilter-swift.class/localizeddescription(forfiltername:).md)
  Returns the localized description of a filter for display in the user interface.
- [class func localizedReferenceDocumentation(forFilterName: String) -> URL?](cifilter-swift.class/localizedreferencedocumentation(forfiltername:).md)
  Returns the location of the localized reference documentation that describes the filter.
### Creating a configuration view for a filter
- [func view(forUIConfiguration: [AnyHashable : Any]!, excludedKeys: [Any]!) -> IKFilterUIView!](cifilter-swift.class/view(foruiconfiguration:excludedkeys:).md)
  Returns a filter view for the filter.
### Applying system tone mapping modes
- [struct CIDynamicRangeOption](cidynamicrangeoption.md)
  An enum string type that your code can use to select different System Tone Mapping modes. These options are consistent with the analogous options available in Core Graphics, Core Animation, AppKit, UIKit, and SwiftUI, In Core Image, this option can be set on the `CISystemToneMap` filter.
### Constants
- [Filter Attribute Keys](filter-attribute-keys.md)
  Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md)
  Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md)
  Vector data types.
- [Color Attribute Keys](color-attribute-keys.md)
  Color types.
- [Image Attribute Keys](image-attribute-keys.md)
  Image Types
- [Filter Category Keys](filter-category-keys.md)
  Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md)
  Options that control the application of a custom Core Image filter.
- [User Interface Control Options](user-interface-control-options.md)
  Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md)
  Keys for input parameters to filters.
- [RAW Image Options](raw-image-options.md)
  Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.
### Deprecated
- [init!(CVPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(cvpixelbuffer:properties:options:).md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imagedata:options:).md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter-swift.class/init(imageurl:options:).md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter-swift.class/serializedxmp(from:inputimageextent:).md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter-swift.class/filterarray(fromserializedxmp:inputimageextent:error:).md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter-swift.class/supportedrawcameramodels.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CIRAWFilter](cirawfilter.md)
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

## See Also

- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.
- [class CIVector](civector.md)
  A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class)*