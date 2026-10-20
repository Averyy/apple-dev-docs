# WKInterfaceDeviceCrownOrientation

**Framework**: WatchKit  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the crown orientation from the user’s perspective.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
enum WKInterfaceDeviceCrownOrientation
```

```c
enum WKInterfaceDeviceCrownOrientation : NSInteger;
```

## Topics

### Constants
- [WKInterfaceDeviceCrownOrientation.left](./wkinterfacedevicecrownorientation/left.md)
  The left side of the device.
- [WKInterfaceDeviceCrownOrientation.right](./wkinterfacedevicecrownorientation/right.md)
  The right side of the device.
### Initializers
- [init?(rawValue: Int)](./wkinterfacedevicecrownorientation/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Reading the Device Settings
- [var name: String](./wkinterfacedevice/name.md)
  The name of the device.
- [var model: String](./wkinterfacedevice/model.md)
  The model information for the device.
- [var localizedModel: String](./wkinterfacedevice/localizedmodel.md)
  The localized version of the model information.
- [var wristLocation: WKInterfaceDeviceWristLocation](./wkinterfacedevice/wristlocation.md)
  The wrist on which the user wears the Apple Watch.
- [enum WKInterfaceDeviceWristLocation](./wkinterfacedevicewristlocation.md)
  Constants indicating the wrist on which the user wears the Apple Watch.
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](./wkinterfacedevice/crownorientation.md)
  The side on which the crown is positioned.
- [var preferredContentSizeCategory: String](./wkinterfacedevice/preferredcontentsizecategory.md)
  The preferred font-sizing option.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevicecrownorientation)*