# orientation

**Framework**: Xcuiautomation  
**Kind**: property

The orientation of the device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- Xcode 16.3+

## Declaration

```swift
@MainActor
var orientation: UIDeviceOrientation { get set }
```

#### Discussion

To simulate a change in the physical orientation of a device under test, set the value of the [`orientation`](xcuidevice/orientation.md) property for the shared [`XCUIDevice`](xcuidevice.md) object to one of the [`UIDeviceOrientation`](https://developer.apple.com/documentation/UIKit/UIDeviceOrientation) constants UIKit defines. This impacts the [`orientation`](https://developer.apple.com/documentation/UIKit/UIDevice/orientation) property UIKit uses to identify a device’s physical orientation. These constants aren’t tied directly to the orientation of your app’s user interface. The example below sets the device orientation to landscape right:

```swift
XCUIDevice.shared.orientation = .landscapeRight
```

Set the property once in your test fixture’s setup or intialization code to set an orientation for all the test methods in that fixture.

Available in iOS.

## See Also

- [var location: XCUILocation?](xcuidevice/location.md)
  The proxy location a test uses to simulate longitude, latitude, and course information for the device.
- [class XCUILocation](xcuilocation.md)
  A proxy that simulates a device’s location in terms of its longitude, latitude, and course information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice/orientation)*