# Profile Concatenation Values

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify values to use when concatenating profiles.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : int {
    ...
};
```

## Topics

### Constants
- [kNoTransform](./api-1560373-profile_concatenation_values/knotransform.md)
  Not used.
- [kUseAtoB](./api-1560373-profile_concatenation_values/kuseatob.md)
  Use 'A2B*' tag from this profile or equivalent
- [kUseBtoA](./api-1560373-profile_concatenation_values/kusebtoa.md)
  Use 'B2A*' tag from this profile or equivalent
- [kUseBtoB](./api-1560373-profile_concatenation_values/kusebtob.md)
  Use 'pre*' tag from this profile or equivalent
- [kDeviceToPCS](./api-1560373-profile_concatenation_values/kdevicetopcs.md)
  Device Dependent to Device Independent
- [kPCSToDevice](./api-1560373-profile_concatenation_values/kpcstodevice.md)
  Device Independent to Device Dependent 
- [kPCSToPCS](./api-1560373-profile_concatenation_values/kpcstopcs.md)
  Independent, through device's gamut
- [kUseProfileIntent](./api-1560373-profile_concatenation_values/kuseprofileintent.md)
  For renderingIntent in NCMConcatProfileSpec


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values)*