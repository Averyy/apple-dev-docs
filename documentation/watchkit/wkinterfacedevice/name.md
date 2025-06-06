# name

**Framework**: Watchkit  
**Kind**: property

The name of the device.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

The default value of this property varies according to the device’s operating system version number:

| OS | Default value | Example |
| --- | --- | --- |
| watchOS 8 and earlier | User-assigned device name | `"Ravi’s Apple Watch Ultra (49mm)"` |
| watchOS 9 and later | Generic device name | `"Apple Watch Ultra (49mm)"` |

In watchOS, the  is available in the Settings app under General > About > Name. To access the user-assigned device name through this property in watchOS 9 and later, your app must meet certain criteria and be assigned an entitlement. For information, see [`com.apple.developer.device-information.user-assigned-device-name`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.device-information.user-assigned-device-name).

> **Note**:  Session 10096: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10096)

 Session 10096: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10096)

## See Also

- [var model: String](wkinterfacedevice/model.md)
  The model information for the device.
- [var localizedModel: String](wkinterfacedevice/localizedmodel.md)
  The localized version of the model information.
- [var wristLocation: WKInterfaceDeviceWristLocation](wkinterfacedevice/wristlocation.md)
  The wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceWristLocation](wkinterfacedevicewristlocation.md)
  Constants indicating the wrist on which the user wears the Apple Watch.
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](wkinterfacedevice/crownorientation.md)
  The side on which the crown is positioned.
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md)
  Constants indicating the crown orientation from the user’s perspective.
- [var preferredContentSizeCategory: String](wkinterfacedevice/preferredcontentsizecategory.md)
  The preferred font-sizing option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/name)*