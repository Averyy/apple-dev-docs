# cmIterateCustomDeviceProfiles

**Framework**: Application Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- macOS 10.0+

## Declaration

```c
cmIterateCustomDeviceProfiles = 0x00000002
```

#### Discussion

Iterate profiles that are meant to take the place of the factory profiles, as a result of customization or calibration. To retrieve only custom profiles for all devices, use the `cmIterateCustomDeviceProfiles`, as the flags value when calling `CMIterateDeviceProfiles`. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecustomdeviceprofiles)*