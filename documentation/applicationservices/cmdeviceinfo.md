# CMDeviceInfo

**Framework**: Application Services  
**Kind**: struct

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct CMDeviceInfo
```

## Topics

### Initializers
- [init()](cmdeviceinfo/1458828-init.md)
- [init(dataVersion: UInt32, deviceClass: CMDeviceClass, deviceID: UInt32, deviceScope: CMDeviceScope, deviceState: UInt32, defaultProfileID: UInt32, deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, profileCount: UInt32, reserved: UInt32)](cmdeviceinfo/1461251-init.md)
### Instance Properties
- [var dataVersion: UInt32](cmdeviceinfo/1464698-dataversion.md)
- [var defaultProfileID: UInt32](cmdeviceinfo/1461755-defaultprofileid.md)
- [var deviceClass: CMDeviceClass](cmdeviceinfo/1463209-deviceclass.md)
- [var deviceID: UInt32](cmdeviceinfo/1458888-deviceid.md)
- [var deviceName: UnsafeMutablePointer<Unmanaged<CFDictionary>?>!](cmdeviceinfo/1460441-devicename.md)
  See the CFDictionary documentation for a description of the `CFDictionaryRef` data type.
- [var deviceScope: CMDeviceScope](cmdeviceinfo/1458913-devicescope.md)
- [var deviceState: UInt32](cmdeviceinfo/1460889-devicestate.md)
- [var profileCount: UInt32](cmdeviceinfo/1462497-profilecount.md)
- [var reserved: UInt32](cmdeviceinfo/1459154-reserved.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo)*