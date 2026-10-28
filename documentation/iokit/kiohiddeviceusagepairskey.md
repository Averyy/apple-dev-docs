# kIOHIDDeviceUsagePairsKey

**Framework**: IOKit  
**Kind**: macro  
**Role**: Macro

A key that contains the top-level usages of the device.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.3+

## Declaration

```c
#define kIOHIDDeviceUsagePairsKey
```

## Discussion

The value of this key is an array of dictionaries. The keys and values of each dictionary are the usage pages and usages for which to match your driver. Use this key when the device supports multiple behaviors and you want to match your driver against more than one of these behaviors. 

## See Also

### Usage Keys
- [kIOHIDDeviceUsageKey](./kiohiddeviceusagekey.md)
  A key that specifies a usage type of the device.
- [kIOHIDDeviceUsagePageKey](./kiohiddeviceusagepagekey.md)
  A key that specifies a usage page of the device.
- [kIOHIDPrimaryUsageKey](./kiohidprimaryusagekey.md)
  A key that specifies the primary usage type of the device.
- [kIOHIDPrimaryUsagePageKey](./kiohidprimaryusagepagekey.md)
  A key that specifies the primary usage page of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/kiohiddeviceusagepairskey)*