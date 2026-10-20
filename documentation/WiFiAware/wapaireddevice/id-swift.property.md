# id

**Framework**: Wi-Fi Aware  
**Kind**: property  
**Role**: Instance Property

A stable ID that you can use to uniquely identify a device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
let id: WAPairedDevice.ID
```

#### Discussion

The ID is stable for the lifetime of a single app install on a single device. This value is the same as the value provided in [AccessorySetupKit](../../AccessorySetupKit/AccessorySetupKit.md)’s `ASAccessory/wifiAwarePairedDeviceID`.

## See Also

### Getting the app-specific identifier
- [WAPairedDevice.ID](./id-swift.typealias.md)
  A type of value that uniquely identifies the paired device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/wifiaware/wapaireddevice/id-swift.property)*