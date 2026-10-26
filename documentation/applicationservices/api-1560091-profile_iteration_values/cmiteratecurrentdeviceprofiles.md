# cmIterateCurrentDeviceProfiles

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmIterateCurrentDeviceProfiles = 0x00000003
```

#### Discussion

Iterate profiles registered through the routing `CMSetDeviceProfiles`. To get the profiles in use for all devices, use `cmIterateCurrentDeviceProfiles` as the flags value. This will replace the factory profiles with any overrides, yielding the currently used set.I


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecurrentdeviceprofiles)*