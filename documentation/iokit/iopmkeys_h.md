# IOPMKeys.h

**Framework**: IOKit  
**Role**: API Collection

IOPMKeys.h defines C strings for use accessing power management data. Note that all of these C strings must be converted to CFStrings before use. You can wrap them with the CFSTR() macro, or create a CFStringRef (that you must later CFRelease()) using CFStringCreateWithCString()

## Topics

### Constants
- [Defines](./iopmkeys_h/defines.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/iopmkeys_h)*