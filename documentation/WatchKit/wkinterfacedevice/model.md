# model

**Framework**: WatchKit  
**Kind**: property  
**Role**: Instance Property

The model information for the device.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var model: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * model;
```

## Discussion

For Apple Watch, the value of this string is `Apple Watch`.

## See Also

### Reading the Device Settings
- [var name: String](./name.md)
  The name of the device.
- [var localizedModel: String](./localizedmodel.md)
  The localized version of the model information.
- [var wristLocation: WKInterfaceDeviceWristLocation](./wristlocation.md)
  The wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceWristLocation](../wkinterfacedevicewristlocation.md)
  Constants indicating the wrist on which the user wears the Apple Watch.
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](./crownorientation.md)
  The side on which the crown is positioned.
- [enum WKInterfaceDeviceCrownOrientation](../wkinterfacedevicecrownorientation.md)
  Constants indicating the crown orientation from the user’s perspective.
- [var preferredContentSizeCategory: String](./preferredcontentsizecategory.md)
  The preferred font-sizing option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/model)*