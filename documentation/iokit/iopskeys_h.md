# IOPSKeys.h

**Framework**: IOKit  
**Role**: API Collection

IOPSKeys.h defines C strings for use accessing power source data in IOPowerSource CFDictionaries, as returned by [`IOPSGetPowerSourceDescription`](./api-1523867-iopsgetpowersourcedescription.md) Note that all of these C strings must be converted to CFStrings before use. You can wrap them with the CFSTR() macro, or create a CFStringRef (that you must later CFRelease()) using CFStringCreateWithCString().

## Topics

### Constants
- [Defines](./iopskeys_h/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopskeys_h)*