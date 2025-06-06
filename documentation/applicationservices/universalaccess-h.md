# UniversalAccess.h

**Framework**: Application Services

This header file contains functions that give applications the ability to control the zoom focus. Using these functions, an application can tell the macOS Universal Access zoom feature what part of its user interface needs focus.

#### Overview

See the Overview section above for header-level documentation.

##### 1681428

###### 1681434

- <CoreGraphics/CoreGraphics.h>
- <AvailabilityMacros.h>

## Topics

### Miscellaneous
- [func UAZoomChangeFocus(UnsafePointer<CGRect>!, UnsafePointer<CGRect>!, UAZoomChangeFocusType) -> OSStatus](1458830-uazoomchangefocus.md)
  Tells the Universal Access zoom feature where it should focus.
- [func UAZoomEnabled() -> Bool](1462288-uazoomenabled.md)
  Determines if the Universal Access zoom feature is enabled.
### Data Types
- [typealias UAZoomChangeFocusType](uazoomchangefocustype.md)
  Defines the Universal Access zoom change focus type.
### Constants
- [UAZoomFocusTypes](universalaccess_h/1553162-uazoomfocustypes.md)
  Values that tell the Universal Access zoom feature what type of event is causing the change in zoom focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/universalaccess_h)*