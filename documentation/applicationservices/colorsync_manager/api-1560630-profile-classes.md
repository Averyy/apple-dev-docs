# Profile Classes

**Framework**: Application Services

Specify profile class enumerations.

#### Overview

The ColorSync Manager supports seven classes, or types, of profiles. 

A profile creator specifies the profile class in the profile header’s `profileClass` field. For a description of the profile header, see [`CM2Header`](cm2header.md). This enumeration defines the profile class signatures. 

## Topics

### Constants
- [var cmInputClass: Int](cminputclass.md)
  An input device profile defined for a scanner.
- [var cmDisplayClass: Int](cmdisplayclass.md)
  A display device profile defined for a monitor. 
- [var cmOutputClass: Int](cmoutputclass.md)
  An output device profile defined for a printer. 
- [var cmLinkClass: Int](cmlinkclass.md)
  A device link profile.
- [var cmAbstractClass: Int](cmabstractclass.md)
  An abstract profile. 
- [var cmColorSpaceClass: Int](cmcolorspaceclass.md)
  A color space profile.
- [var cmNamedColorClass: Int](cmnamedcolorclass.md)
  A named color space profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1560630-profile_classes)*