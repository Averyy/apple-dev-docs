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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/user_interface_control_options)*