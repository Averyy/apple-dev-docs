# User Interface Control Options

**Framework**: Core Image

Sets of controls for various user scenarios.

#### Overview

You can use these constants to specify the controls that you want associated with each user scenario. For example, for a filter that has many input parameters you can choose a small set of input parameters that the typical consumer can control and set the other input parameters to default values. For the same filter, however, you can choose to allow professional customers to control all the input parameters.

## Topics

### Constants
- [let kCIUIParameterSet: String](kciuiparameterset.md)
  The set of input parameters to use. The associated value can be [`kCIUISetBasic`](kciuisetbasic.md), [`kCIUISetIntermediate`](kciuisetintermediate.md), [`kCIUISetAdvanced`](kciuisetadvanced.md), or [`kCIUISetDevelopment`](kciuisetdevelopment.md).
- [let kCIUISetBasic: String](kciuisetbasic.md)
  Controls that are appropriate for a basic user scenario, that is, the minimum of settings to control the filter.
- [let kCIUISetIntermediate: String](kciuisetintermediate.md)
  Controls that are appropriate for an intermediate user scenario.
- [let kCIUISetAdvanced: String](kciuisetadvanced.md)
  Controls that are appropriate for an advanced user scenario.
- [let kCIUISetDevelopment: String](kciuisetdevelopment.md)
  Controls that should be visible  only for development purposes.

## See Also

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
- [User Interface Options](user-interface-options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md)
  Keys for input parameters to filters.
- [RAW Image Options](raw-image-options.md)
  Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/user-interface-control-options)*