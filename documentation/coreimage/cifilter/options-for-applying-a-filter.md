# Options for Applying a Filter

**Framework**: Core Image

Options that control the application of a custom Core Image filter.

#### Overview

Use these constants only when creating a custom filter for which you are writing the kernel. For more information, see [`Core Image Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185). The example on creating a custom filter shows how to use these options.

## Topics

### Constants
- [let kCIApplyOptionExtent: String](kciapplyoptionextent.md)
  The size of the produced image. The associated value is a four-element array ([`NSArray`](https://developer.apple.com/documentation/foundation/nsarray)) that specifies the x-value of the rectangle origin, the y-value of the rectangle origin, and the width and height.
- [let kCIApplyOptionDefinition: String](kciapplyoptiondefinition.md)
  The domain of definition (DOD) of the produced image. The associated value is either a Core Image filter shape or a four-element array ([`NSArray`](https://developer.apple.com/documentation/foundation/nsarray)) that specifies a rectangle.
- [let kCIApplyOptionUserInfo: String](kciapplyoptionuserinfo.md)
  Information needed by a callback. The associated value is an object that Core Image will pass to any callbacks invoked for that filter.
- [let kCIApplyOptionColorSpace: String](kciapplyoptioncolorspace.md)
  The color space of the produced image. The associated value must be an RGB [`CGColorSpace`](https://developer.apple.com/documentation/coregraphics/cgcolorspace) object. If not specified, the output of the kernel is in the working color space of the Core Image context used to render the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter/options_for_applying_a_filter)*