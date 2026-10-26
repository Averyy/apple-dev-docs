# Profile Iteration Values

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify profiles to iterate.

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
- [cmIterateFactoryDeviceProfiles](./api-1560091-profile_iteration_values/cmiteratefactorydeviceprofiles.md)
  Iterate profiles registered through the routine `CMSetDeviceFactoryProfiles`. To retrieve all factory profiles for all devices, use `cmIterateFactoryDeviceProfiles` as the flags value when calling `CMIterateDeviceProfiles`. I
- [cmIterateCustomDeviceProfiles](./api-1560091-profile_iteration_values/cmiteratecustomdeviceprofiles.md)
- [cmIterateCurrentDeviceProfiles](./api-1560091-profile_iteration_values/cmiteratecurrentdeviceprofiles.md)
- [cmIterateAllDeviceProfiles](./api-1560091-profile_iteration_values/cmiteratealldeviceprofiles.md)
  Iterate all profiles, without replacement.
- [cmIterateDeviceProfilesMask](./api-1560091-profile_iteration_values/cmiteratedeviceprofilesmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values)*