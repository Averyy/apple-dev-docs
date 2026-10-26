# Profile Location Type

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Defines profile location kinds.

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
- [cmNoProfileBase](./api-1560599-profile_location_type/cmnoprofilebase.md)
  The profile is temporary. It will not persist in memory after its use for a color session. You can specify this type of profile location with the `CMNewProfile` and the `CMCopyProfile` functions.
- [cmPathBasedProfile](./api-1560599-profile_location_type/cmpathbasedprofile.md)
- [cmBufferBasedProfile](./api-1560599-profile_location_type/cmbufferbasedprofile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560599-profile_location_type)*