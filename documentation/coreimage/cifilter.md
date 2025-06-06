# CIFilter

**Framework**: Core Image  
**Kind**: cl

An image processor that produces an image by manipulating one or more input images or by generating new image data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CIFilter : NSObject
```

#### Overview

The [`CIFilter`](cifilter.md) class produces a [`CIImage`](ciimage.md) object as output. Typically, a filter takes one or more images as input. Some filters, however, generate an image based on other types of input parameters. The parameters of a [`CIFilter`](cifilter.md) object are set and retrieved through the use of key-value pairs.

You use the [`CIFilter`](cifilter.md) object in conjunction with other Core Image classes, such as  [`CIImage`](ciimage.md), [`CIContext`](cicontext.md), and [`CIColor`](cicolor.md), to take advantage of the built-in Core Image filters when processing images, creating filter generators, or writing custom filters.

[`CIFilter`](cifilter.md) objects are mutable, and thus cannot be shared safely among threads. Each thread must create its own [`CIFilter`](cifilter.md) objects, but you can pass a filter’s immutable input and output [`CIImage`](ciimage.md) objects between threads.

To get a quick overview of how to set up and use Core Image filters, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185).

##### 4336878

Core Image provides methods that create type-safe [`CIFilter`](cifilter.md) instances. Use these filters to avoid run-time errors that can occur when relying on Core Image’s string-based API.

To use the type-safe API, import `CoreImage.CIFilterBuiltins`:

```swift
import CoreImage
import CoreImage.CIFilterBuiltins
```

The type-safe approach returns a non-optional filter. Because the returned filter conforms to the relevant protocol—for example, [`CIFalseColor`](cifalsecolor.md) in the case of [`falseColor()`](cifilter/3228325-falsecolor.md)—the parameters are available as properties. The following creates and applies a false color filter:

```swift
func falseColor(inputImage: CIImage) -> CIImage? {
    let falseColorFilter = CIFilter.falseColor()
    falseColorFilter.color0 = CIColor(red: 1, green: 1, blue: 0)
    falseColorFilter.color1 = CIColor(red: 0, green: 0, blue: 1)
    falseColorFilter.inputImage = inputImage
    return falseColorFilter.outputImage
}
```

The false color filter maps luminance to a color ramp of two colors:

![Two photographs showing a flower. The image on the left shows the original version of the flower. The image on the right shows the false color version of the flower.](https://docs-assets.developer.apple.com/published/93c7683dae/e23ecc5d-52d4-4368-a7da-8fe363616922.png)

##### 1770534

You can subclass [`CIFilter`](cifilter.md) in order to create custom filter effects:

- By chaining together two or more built-in Core Image filters
- By using an image-processing kernel that you write

Regardless of whether your subclass provides its effect by chaining filters or implementing its own kernel, you should:

- Declare any input parameters as properties whose names are prefixed with `input`, such as `inputImage`.
- Override the [`setDefaults()`](cifilter/1437902-setdefaults.md) methods to provide default values for any input parameters you’ve declared.
- Implement an `outputImage` method to create a new [`CIImage`](ciimage.md) with your filter’s effect.

The [`CIFilter`](cifilter.md) class automatically manages input parameters when archiving, copying, and deallocating filters. For this reason, your subclass must obey the following guidelines to ensure proper behavior:

- Store input parameters in instance variables whose names are prefixed with `input`. Don’t use auto-synthesized instance variables, because their names are automatically prefixed with an underscore. Instead, synthesize the property manually. For example: `@synthesize inputMyParameter;`
- If using manual reference counting, don’t release input parameter instance variables in your [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) method implementation. The [`dealloc`](https://developer.apple.com/documentation/objectivec/nsobject/1571947-dealloc) implementation in the [`CIFilter`](cifilter.md) class uses [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) to automatically set the values of all input parameters to `nil`.

## Topics

### Creating a Filter
- [init?(name: String)](cifilter/1438255-init.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter. 
- [init?(name: String, parameters: [String : Any]?)](cifilter/1437894-init.md)
  Creates a [`CIFilter`](cifilter.md) object for a specific kind of filter and initializes the input values.
### Configuring Type-Safe Filters
- [protocol CIFilterProtocol](cifilterprotocol.md)
  The properties you use to configure a Core Image filter.
- [Blur Filters](cifilter/blur_filters.md)
- [Color Adjustment Filters](cifilter/color_adjustment_filters.md)
- [Color Effect Filters](cifilter/color_effect_filters.md)
- [Composite Operations](cifilter/composite_operations.md)
- [Convolution Filters](cifilter/convolution_filters.md)
- [Distortion Filters](cifilter/distortion_filters.md)
- [Generator Filters](cifilter/generator_filters.md)
- [Geometry Adjustment Filters](cifilter/geometry_adjustment_filters.md)
- [Gradient Filters](cifilter/gradient_filters.md)
- [Halftone Effect Filters](cifilter/halftone_effect_filters.md)
- [Reduction Filters](cifilter/reduction_filters.md)
- [Sharpening Filters](cifilter/sharpening_filters.md)
- [Stylizing Filters](cifilter/stylizing_filters.md)
- [Tile Effect Filters](cifilter/tile_effect_filters.md)
- [Transition Filters](cifilter/transition_filters.md)
### Accessing Registered Filters
- [class func filterNames(inCategories: [String]?) -> [String]](cifilter/1437595-filternames.md)
  Returns an array of all published filter names that match all the specified categories.
- [class func filterNames(inCategory: String?) -> [String]](cifilter/1438145-filternames.md)
  Returns an array of all published filter names in the specified category.
### Registering a Filter
- [class func registerName(String, constructor: any CIFilterConstructor, classAttributes: [String : Any])](cifilter/1437889-registername.md)
  Publishes a custom filter that is not packaged as an image unit.
### Getting Filter Parameters and Attributes
- [var name: String](cifilter/1437997-name.md)
  A name associated with a filter.
- [var isEnabled: Bool](cifilter/1438276-isenabled.md)
  A Boolean value that determines whether the filter is enabled. Animatable.
- [var attributes: [String : Any]](cifilter/1437661-attributes.md)
  A dictionary of key-value pairs that describe the filter.
- [var inputKeys: [String]](cifilter/1438013-inputkeys.md)
  The names of all input parameters to the filter.
- [var outputKeys: [String]](cifilter/1438122-outputkeys.md)
  The names of all output parameters from the filter.
- [var outputImage: CIImage?](cifilter/1438169-outputimage.md)
  Returns a [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.
### Setting Default Values
- [func setDefaults()](cifilter/1437902-setdefaults.md)
  Sets all input values for a filter to default values.
### Applying a Filter
- [func apply(CIKernel, arguments: [Any]?, options: [String : Any]?) -> CIImage?](cifilter/1438077-apply.md)
  Produces a [`CIImage`](ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.
### Getting Localized Information for Registered Filters
- [class func localizedName(forFilterName: String) -> String?](cifilter/1437697-localizedname.md)
  Returns the localized name for the specified filter name.
- [class func localizedName(forCategory: String) -> String](cifilter/1438057-localizedname.md)
  Returns  the localized name for the specified filter category.
- [class func localizedDescription(forFilterName: String) -> String?](cifilter/1437591-localizeddescription.md)
  Returns the localized description of a filter for display in the user interface.
- [class func localizedReferenceDocumentation(forFilterName: String) -> URL?](cifilter/1437642-localizedreferencedocumentation.md)
  Returns the location of the localized reference documentation that describes the filter. 
### Creating a Configuration View for a Filter
- [func view(forUIConfiguration: [AnyHashable : Any]!, excludedKeys: [Any]!) -> IKFilterUIView!](cifilter/1427521-view.md)
  Returns a filter view for the filter.
### Constants
- [Filter Attribute Keys](cifilter/filter_attribute_keys.md)
  Attributes for a filter and its parameters.
- [Data Type Attributes](cifilter/data_type_attributes.md)
  Numeric data types.
- [Vector Quantity Attributes](cifilter/vector_quantity_attributes.md)
  Vector data types.
- [Color Attribute Keys](cifilter/color_attribute_keys.md)
  Color types.
- [Image Attribute Keys](cifilter/image_attribute_keys.md)
  Image Types
- [Filter Category Keys](cifilter/filter_category_keys.md)
  Categories of filters.
- [Options for Applying a Filter](cifilter/options_for_applying_a_filter.md)
  Options that control the application of a custom Core Image filter.
- [User Interface Control Options](cifilter/user_interface_control_options.md)
  Sets of controls for various user scenarios.
- [User Interface Options](cifilter/user_interface_options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](cifilter/filter_parameter_keys.md)
  Keys for input parameters to filters.
- [RAW Image Options](cifilter/raw_image_options.md)
  Options for creating a [`CIFilter`](cifilter.md) object from RAW image data.
### Deprecated
- [init!(cvPixelBuffer: CVPixelBuffer!, properties: [AnyHashable : Any]!, options: [CIRAWFilterOption : Any]!)](cifilter/2138288-init.md)
  Creates a filter from a Core Video pixel buffer.
- [init!(imageData: Data!, options: [CIRAWFilterOption : Any]!)](cifilter/1437879-init.md)
  Creates a filter that allows the processing of RAW images.
- [init!(imageURL: URL!, options: [CIRAWFilterOption : Any]!)](cifilter/1438096-init.md)
  Creates a filter that allows the processing of RAW images.
- [struct CIRAWFilterOption](cirawfilteroption.md)
- [class func serializedXMP(from: [CIFilter], inputImageExtent: CGRect) -> Data?](cifilter/1438006-serializedxmp.md)
  Serializes filter parameters into XMP form that is suitable for embedding in an image.
- [class func filterArray(fromSerializedXMP: Data, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter]](cifilter/1438237-filterarray.md)
  Returns an array of filter objects de-serialized from XMP data.
- [class func supportedRawCameraModels() -> [String]!](cifilter/3242782-supportedrawcameramodels.md)
### Type Methods
- [class func areaAlphaWeightedHistogram() -> any CIFilter & CIAreaHistogram](cifilter/4401846-areaalphaweightedhistogram.md)
- [class func areaBoundsRed() -> any CIFilter & CIAreaBoundsRed](cifilter/4401847-areaboundsred.md)
- [class func maximumScaleTransform() -> any CIFilter & CIMaximumScaleTransform](cifilter/4401870-maximumscaletransform.md)
- [class func toneMapHeadroom() -> any CIFilter & CIToneMapHeadroom](cifilter/4401878-tonemapheadroom.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../foundation/nscopying.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class CIRAWFilter](cirawfilter.md)
  A filter subclass that produces an image by manipulating RAW image sensor data from a digital camera or scanner.
- [class CIColor](cicolor.md)
  The component values defining a color in a specific color space.
- [class CIVector](civector.md)
  A container for coordinate values, direction vectors, matrices, and other non-scalar values, typically used in Core Image for filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter)*