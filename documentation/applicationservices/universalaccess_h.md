# UniversalAccess.h

**Framework**: Application Services  
**Role**: API Collection

This header file contains functions that give applications the ability to control the zoom focus. Using these functions, an application can tell the macOS Universal Access zoom feature what part of its user interface needs focus.

#### Overview

See the Overview section above for header-level documentation.

##### Overview

###### Included Headers

- <CoreGraphics/CoreGraphics.h>
- <AvailabilityMacros.h>

## Topics

### Miscellaneous
- [func UAZoomChangeFocus(UnsafePointer<CGRect>!, UnsafePointer<CGRect>!, UAZoomChangeFocusType) -> OSStatus](./api-1458830-uazoomchangefocus.md)
  Tells the Universal Access zoom feature where it should focus.
- [func UAZoomEnabled() -> Bool](./api-1462288-uazoomenabled.md)
  Determines if the Universal Access zoom feature is enabled.
### Data Types
- [typealias UAZoomChangeFocusType](./uazoomchangefocustype.md)
  Defines the Universal Access zoom change focus type.
### Constants
- [UAZoomFocusTypes](./universalaccess_h/api-1553162-uazoomfocustypes.md)
  Values that tell the Universal Access zoom feature what type of event is causing the change in zoom focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/universalaccess_h)*