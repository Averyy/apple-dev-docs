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

## Overview

The default value of this property varies according to the device’s operating system version number:

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'OS'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Default value', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Example'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'watchOS 8 and earlier'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'User-assigned device name'}]}] | [{'type': 'paragraph', 'inlineContent': [{'code': '"Ravi’s Apple Watch Ultra (49mm)"', 'type': 'codeVoice'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'watchOS 9 and later', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Generic device name'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'codeVoice', 'code': '"Apple Watch Ultra (49mm)"'}]}] |

In watchOS, the  is available in the Settings app under General > About > Name. To access the user-assigned device name through this property in watchOS 9 and later, your app must meet certain criteria and be assigned an entitlement. For information, see [`com.apple.developer.device-information.user-assigned-device-name`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.device-information.user-assigned-device-name).

> **Note**:  Session 10096: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10096)

 Session 10096: [`What’s new in privacy`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2022/10096)

## See Also

- [var model: String](model.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/model))
- [var localizedModel: String](localizedmodel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/localizedmodel))
- [var wristLocation: WKInterfaceDeviceWristLocation](wristlocation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation))
- [enum WKInterfaceDeviceWristLocation](wkinterfacedevicewristlocation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation))
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](crownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation))
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation))
- [var preferredContentSizeCategory: String](preferredcontentsizecategory.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/preferredcontentsizecategory))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/name)*