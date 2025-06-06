# Filter Attribute Keys

**Framework**: Core Image

Attributes for a filter and its parameters.

#### Overview

Attribute keys are used for the attribute dictionary of a filter.  Most entries in the attribute dictionary are optional. The attribute [`kCIAttributeFilterName`](kciattributefiltername.md) is mandatory. For a parameter, the attribute [`kCIAttributeClass`](kciattributeclass.md) is mandatory because it specifies the class name of the filter.

A parameter of type [`NSNumber`](https://developer.apple.com/documentation/foundation/nsnumber) does not necessarily need the attributes [`kCIAttributeMin`](kciattributemin.md) and [`kCIAttributeMax`](kciattributemax.md). These attributes are not present when the parameter has no upper or lower bounds. For example, the Gaussian blur filter has a radius parameter with a minimum of `0` but no maximum value to indicate that all nonnegative values are valid.

## Topics

### Constants
- [let kCIAttributeFilterName: String](kciattributefiltername.md)
  The filter name, specified as an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) object.
- [let kCIAttributeFilterDisplayName: String](kciattributefilterdisplayname.md)
  The localized version of the filter name that is displayed in the user interface.
- [let kCIAttributeDescription: String](kciattributedescription.md)
  The localized description of the filter. This description should inform the user what the filter does and be short enough to display in the user interface for the filter. It is not intended to be technically detailed.
- [let kCIAttributeFilterAvailable_Mac: String](kciattributefilteravailable_mac.md)
  The macOS version in which the filter first became available, specified as an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) object.
- [let kCIAttributeFilterAvailable_iOS: String](kciattributefilteravailable_ios.md)
  The iOS version in which the filter first became available, specified as an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) object.
- [let kCIAttributeReferenceDocumentation: String](kciattributereferencedocumentation.md)
  The localized reference documentation for the filter. The reference should provide developers with technical details.
- [let kCIAttributeFilterCategories: String](kciattributefiltercategories.md)
  An array of filter category keys that specifies all the categories in which the filter is a member.
- [let kCIAttributeClass: String](kciattributeclass.md)
  The class name of the filter.
- [let kCIAttributeType: String](kciattributetype.md)
  One of the attribute types described in [`Data Type Attributes`](cifilter/data_type_attributes.md). 
- [let kCIAttributeMin: String](kciattributemin.md)
  The minimum value for a filter parameter, specified as a floating-point value. 
- [let kCIAttributeMax: String](kciattributemax.md)
  The maximum value for a filter parameter, specified as a floating-point value.
- [let kCIAttributeSliderMin: String](kciattributeslidermin.md)
  The minimum value, specified as a floating-point value, to use for a slider that controls input values for a filter parameter.
- [let kCIAttributeSliderMax: String](kciattributeslidermax.md)
  The maximum value, specified as a floating-point value, to use for a slider that controls input values for a filter parameter.
- [let kCIAttributeDefault: String](kciattributedefault.md)
  The default value, specified as a floating-point value, for a filter parameter.
- [let kCIAttributeIdentity: String](kciattributeidentity.md)
  If supplied as a value for a parameter, the parameter has no effect on the input image.
- [let kCIAttributeName: String](kciattributename.md)
  The name of the attribute.
- [let kCIAttributeDisplayName: String](kciattributedisplayname.md)
  The localized display name of the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/filter_attribute_keys)*