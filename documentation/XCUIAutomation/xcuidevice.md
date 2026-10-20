# XCUIDevice

**Framework**: XCUIAutomation  
**Kind**: class  
**Role**: Class

A proxy that can simulate physical buttons, device orientation, and Siri interaction for an iOS, watchOS, or tvOS device.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
@MainActor
class XCUIDevice
```

```objc
@interface XCUIDevice : NSObject
```

#### Overview

Use the `XCUIDevice` [`shared`](./xcuidevice/shared.md) instance to perform the following interactions with a simulated iOS, watchOS, or tvOS device during a UI test:

- Press the volume, home, camera, and action buttons.
- Rotate the device.
- Turn the Digital Crown on a watchOS device.
- Determine whether the iOS device supports pointer interaction.
- Activate Siri.

This example shows a test that determines whether the action button is available on the shared device and, if it is, simulates pressing the button:

```swift
@MainActor
func testPressingActionButton() throws {
    let device = XCUIDevice.shared
    try XCTSkipUnless(device.hasHardwareButton(.action),
                  "The device doesn't have an action button.")
    let app = XCUIApplication()
    app.launch()
    device.press(.action)
    // Assert that your app responds correctly.
}
```

`XCUIDevice` is available in iOS, watchOS, and tvOS.

## Topics

### Accessing the current device
- [class var shared: XCUIDevice](./xcuidevice/shared.md)
  The current device.
- [var supportsPointerInteraction: Bool](./xcuidevice/supportspointerinteraction.md)
  A Boolean value that indicates if the device supports pointer interaction.
- [var supportsHandGestures: Bool](./xcuidevice/supportshandgestures.md)
  A Boolean value that indicates if the device supports hand gestures.
### Interacting with buttons and the Digital Crown
- [func press(XCUIDevice.Button)](./xcuidevice/press%28_%29.md)
  Simulates the user pressing a physical button.
- [func hasHardwareButton(XCUIDevice.Button) -> Bool](./xcuidevice/hashardwarebutton%28_%29.md)
  Determines whether the device supports the button type you provide.
- [XCUIDevice.Button](./xcuidevice/button.md)
  A physical button on an iOS device.
- [func rotateDigitalCrown(delta: CGFloat)](./xcuidevice/rotatedigitalcrown%28delta%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount.
- [func rotateDigitalCrown(delta: CGFloat, velocity: XCUIGestureVelocity)](./xcuidevice/rotatedigitalcrown%28delta,velocity%29.md)
  Simulates the user rotating the Digital Crown on an Apple Watch by the delta amount and speed you provide.
### Performing gestures
- [func perform(handGesture: XCUIDeviceHandGesture)](./xcuidevice/perform%28handgesture%29.md)
- [enum XCUIDeviceHandGesture](./xcuidevicehandgesture.md)
  A hand gesture on a watchOS device.
### Rotating and changing location
- [var orientation: UIDeviceOrientation](./xcuidevice/orientation.md)
  The orientation of the device.
- [var location: XCUILocation?](./xcuidevice/location.md)
  The proxy location a test uses to simulate longitude, latitude, and course information for the device.
- [class XCUILocation](./xcuilocation.md)
  A proxy that simulates a device’s location in terms of its longitude, latitude, and course information.
### Interacting with the OS
- [var system: XCUISystem](./xcuidevice/system.md)
  An object that provides an interface to OS-specific properties and actions.
- [var appearance: XCUIDevice.Appearance](./xcuidevice/appearance-swift.property.md)
  The interface style of the device.
- [XCUIDevice.Appearance](./xcuidevice/appearance-swift.enum.md)
  Constants that indicate an interface style.
### Interacting with Siri
- [var siriService: XCUISiriService](./xcuidevice/siriservice.md)
  An object that represents the Siri interface on the device.
### Deprecated
- [init()](./xcuidevice/init%28%29.md)
  Creates an instance that represents the current device.
### Instance Properties
- [var voiceOverService: XCUIVoiceOverService](./xcuidevice/voiceoverservice.md)
  Provides access to VoiceOver for UI testing.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Device simulation
- [class XCUISystem](./xcuisystem.md)
  A proxy that provides an interface to OS-specific properties and actions.
- [class XCUISiriService](./xcuisiriservice.md)
  A proxy that simulates a device’s Siri interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuidevice)*