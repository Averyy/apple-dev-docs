# Element Tags and Signatures for Version 1.0 Profiles

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Define tags and signatures used for version 1.0 profiles.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmCS1ChromTag](./api-1560273-0_profiles/cmcs1chromtag.md)
  The tag signature for the profile chromaticities tag whose element data specifies the XYZ chromaticities for the six primary and secondary colors (red, green, blue, cyan, magenta, and yellow).
- [cmCS1TRCTag](./api-1560273-0_profiles/cmcs1trctag.md)
  The tag signature for profile tonal response curve data for the associated device.
- [cmCS1NameTag](./api-1560273-0_profiles/cmcs1nametag.md)
  The tag signature for the profile name string. This is an international string consisting of a Macintosh script code followed by a 63-byte text string identifying the profile.
- [cmCS1CustTag](./api-1560273-0_profiles/cmcs1custtag.md)
  Private data for a custom CMM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles)*