# Flag Mask Definitions for Version 2.x Profiles

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Define masks your application can use to set or test various bits in the `flags` field of the `CM2Header` structure.

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
- [cmICCReservedFlagsMask](./api-1560699-x_profiles/cmiccreservedflagsmask.md)
- [cmEmbeddedMask](./api-1560699-x_profiles/cmembeddedmask.md)
  This mask provides access to bit 0 of the `flags` field, which specifies whether the profile is embedded. It has the value 1 if the profile is embedded, 0 if it is not.
- [cmEmbeddedUseMask](./api-1560699-x_profiles/cmembeddedusemask.md)
- [cmCMSReservedFlagsMask](./api-1560699-x_profiles/cmcmsreservedflagsmask.md)
- [cmQualityMask](./api-1560699-x_profiles/cmqualitymask.md)
- [cmInterpolationMask](./api-1560699-x_profiles/cminterpolationmask.md)
- [cmGamutCheckingMask](./api-1560699-x_profiles/cmgamutcheckingmask.md)
- [cmBlackPointCompensationMask](./api-1560699-x_profiles/cmblackpointcompensationmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles)*