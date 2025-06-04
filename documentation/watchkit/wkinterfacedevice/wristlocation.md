# wristLocation

**Framework**: WatchKit  
**Kind**: property

The wrist on which the user wears the Apple Watch.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var wristLocation: WKInterfaceDeviceWristLocation { get }
```

#### Discussion

Users specify the wrist placement during the initial setup of Apple Watch, and this property reflects the information provided by the user.

## See Also

- [var name: String](name.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/name))
  The name of the device.
- [var model: String](model.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/model))
  The model information for the device.
- [var localizedModel: String](localizedmodel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/localizedmodel))
  The localized version of the model information.
- [enum WKInterfaceDeviceWristLocation](wkinterfacedevicewristlocation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation))
  Constants indicating the wrist on which the user wears the Apple Watch.
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](crownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation))
  The side on which the crown is positioned.
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation))
  Constants indicating the crown orientation from the user’s perspective.
- [var preferredContentSizeCategory: String](preferredcontentsizecategory.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/preferredcontentsizecategory))
  The preferred font-sizing option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation)*