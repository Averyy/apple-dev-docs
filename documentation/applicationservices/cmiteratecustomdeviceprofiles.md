# cmIterateCustomDeviceProfiles

**Framework**: Application Services  
**Kind**: data

**Availability**:
- macOS 10.0+

## Declaration

```swift
var cmIterateCustomDeviceProfiles: Int { get }
```

#### Discussion

Iterate profiles that are meant to take the place of the factory profiles, as a result of customization or calibration. To retrieve only custom profiles for all devices, use the `cmIterateCustomDeviceProfiles`, as the flags value when calling `CMIterateDeviceProfiles`. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmiteratecustomdeviceprofiles)*