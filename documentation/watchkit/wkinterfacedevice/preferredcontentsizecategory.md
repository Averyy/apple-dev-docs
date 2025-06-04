# preferredContentSizeCategory

**Framework**: WatchKit  
**Kind**: property

The preferred font-sizing option.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var preferredContentSizeCategory: String { get }
```

#### Discussion

Users can request that apps display fonts in a size that is larger or smaller than the normal font size defined by the system. For example, a user with a visual impairment might request a larger default font size to make it easier to read text. Font objects returned by the system automatically scale based on the user’s preference. When requesting font objects from code, use the value of this property to request a font object of the appropriate size.

For a list of possible values, see “Content Size Category Constants” in [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication).

## See Also

- [var name: String](name.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/name))
  The name of the device.
- [var model: String](model.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/model))
  The model information for the device.
- [var localizedModel: String](localizedmodel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/localizedmodel))
  The localized version of the model information.
- [var wristLocation: WKInterfaceDeviceWristLocation](wristlocation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/wristlocation))
  The wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceWristLocation](wkinterfacedevicewristlocation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicewristlocation))
  Constants indicating the wrist on which the user wears the Apple Watch.
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](crownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation))
  The side on which the crown is positioned.
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation))
  Constants indicating the crown orientation from the user’s perspective.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/preferredcontentsizecategory)*