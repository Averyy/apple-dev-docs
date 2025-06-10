# WKInterfaceDevice

**Framework**: WatchKit  
**Kind**: class

An object that provides information about the user’s Apple Watch.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
class WKInterfaceDevice
```

#### Overview

You can use the information from [`WKInterfaceDevice`](wkinterfacedevice.md)  to make decisions about the content you display in your app. You can also use this object to play haptic feedback when your app is active.

Do not subclass or create instances of this class yourself. Always call the [`current()`](wkinterfacedevice/current().md) class method to get the shared device object.

## Topics

### Accessing the Shared Device Object
- [class func current() -> WKInterfaceDevice](wkinterfacedevice/current.md)
  Returns the shared device object.
### Reading the Screen Information
- [var screenBounds: CGRect](wkinterfacedevice/screenbounds.md)
  The bounding rectangle of the screen.
- [var screenScale: CGFloat](wkinterfacedevice/screenscale.md)
  The number of pixels per point for the current screen.
### Reading the Device Settings
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
- [var crownOrientation: WKInterfaceDeviceCrownOrientation](wkinterfacedevice/crownorientation.md)
  The side on which the crown is positioned.
- [enum WKInterfaceDeviceCrownOrientation](wkinterfacedevicecrownorientation.md)
  Constants indicating the crown orientation from the user’s perspective.
- [var preferredContentSizeCategory: String](wkinterfacedevice/preferredcontentsizecategory.md)
  The preferred font-sizing option.
### Reading System Information
- [var systemName: String](wkinterfacedevice/systemname.md)
  The name of the operating system.
- [var systemVersion: String](wkinterfacedevice/systemversion.md)
  The version of the operating system.
### Accessing the Layout Direction
- [var layoutDirection: WKInterfaceLayoutDirection](wkinterfacedevice/layoutdirection.md)
  The layout direction of the user interface.
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](wkinterfacedevice/interfacelayoutdirection(for:).md)
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceSemanticContentAttribute](wkinterfacesemanticcontentattribute.md)
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md)
  Specifies the directional flow of the user interface.
### Reading Information About the Battery
- [var isBatteryMonitoringEnabled: Bool](wkinterfacedevice/isbatterymonitoringenabled.md)
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](wkinterfacedevice/batterylevel.md)
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](wkinterfacedevice/batterystate.md)
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md)
  The battery’s charging state.
### Accessing Water Resistance and Lock
- [var waterResistanceRating: WKWaterResistanceRating](wkinterfacedevice/waterresistancerating.md)
  The Apple Watch water-resistance rating.
- [enum WKWaterResistanceRating](wkwaterresistancerating.md)
  Values indicating the water-resistance rating.
- [var isWaterLockEnabled: Bool](wkinterfacedevice/iswaterlockenabled.md)
  A Boolean value that indicates whether the water lock is enabled.
- [func enableWaterLock()](wkinterfacedevice/enablewaterlock.md)
  Disables the Apple Watch touch screen to prevent accidental taps while submerged.
### Playing Haptic Feedback
- [func play(WKHapticType)](wkinterfacedevice/play(_:).md)
  Gives haptic feedback to the user.
- [enum WKHapticType](wkhaptictype.md)
  Constant indicating the style of feedback to deliver using haptics.
### Streaming Audio
- [var supportsAudioStreaming: Bool](wkinterfacedevice/supportsaudiostreaming.md)
  A Boolean value that indicates whether the device supports audio streaming.
### Validating In-App Purchases
- [var identifierForVendor: UUID?](wkinterfacedevice/identifierforvendor.md)
  An alphanumeric string that uniquely identifies a device to the app’s vendor.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md)
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](wkapplication.md)
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md)
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md)
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [protocol WKExtensionDelegate](wkextensiondelegate.md)
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md)
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- [WKPrefersNetworkUponForeground](../BundleResources/Information-Property-List/WKPrefersNetworkUponForeground.md)
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)*