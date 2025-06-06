# crownOrientation

**Framework**: Watchkit  
**Kind**: property

The side on which the crown is positioned.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
var crownOrientation: WKInterfaceDeviceCrownOrientation { get }
```

#### Discussion

Users specify the Digital Crown orientation during the initial setup of Apple Watch, and this property reflects the information provided by the user.

## See Also

- [var name: String](wkinterfacedevice/name.md)
  The name of the device.
- [var model: String](wkinterfacedevice/model.md)
  The model information for the device.
- [var localizedModel: String](wkinterfacedevice/localizedmodel.md)
  The localized version of the model information.
- [var wristLocation: WKInterfaceDeviceWristLocation](wkinterfacedevice/wristlocation.md)
  The wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceWristLocation](wkinterfacedevicewristlocation.md)
  Constants indicating the wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md)
  Constants indicating the crown orientation from the user’s perspective.
- [var preferredContentSizeCategory: String](wkinterfacedevice/preferredcontentsizecategory.md)
  The preferred font-sizing option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/crownorientation)*