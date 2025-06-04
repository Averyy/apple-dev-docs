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

You can use the information from [`WKInterfaceDevice`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)  to make decisions about the content you display in your app. You can also use this object to play haptic feedback when your app is active.

Do not subclass or create instances of this class yourself. Always call the [`current()`](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/current()) class method to get the shared device object.

## Topics

### Accessing the Shared Device Object
- [class func current() -> WKInterfaceDevice](current().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/current()))
  Returns the shared device object.
### Reading the Screen Information
- [var screenBounds: CGRect](screenbounds.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/screenbounds))
  The bounding rectangle of the screen.
- [var screenScale: CGFloat](screenscale.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/screenscale))
  The number of pixels per point for the current screen.
### Reading the Device Settings
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
- [var preferredContentSizeCategory: String](preferredcontentsizecategory.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/preferredcontentsizecategory))
  The preferred font-sizing option.
### Reading System Information
- [var systemName: String](systemname.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/systemname))
  The name of the operating system.
- [var systemVersion: String](systemversion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/systemversion))
  The version of the operating system.
### Accessing the Layout Direction
- [var layoutDirection: WKInterfaceLayoutDirection](layoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/layoutdirection))
  The layout direction of the user interface.
- [class func interfaceLayoutDirection(for: WKInterfaceSemanticContentAttribute) -> WKInterfaceLayoutDirection](interfacelayoutdirection(for:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/interfacelayoutdirection(for:)))
  Returns the user interface direction for the given semantic content attribute.
- [enum WKInterfaceSemanticContentAttribute](wkinterfacesemanticcontentattribute.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacesemanticcontentattribute))
  A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [enum WKInterfaceLayoutDirection](wkinterfacelayoutdirection.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelayoutdirection))
  Specifies the directional flow of the user interface.
### Reading Information About the Battery
- [var isBatteryMonitoringEnabled: Bool](isbatterymonitoringenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/isbatterymonitoringenabled))
  A Boolean value that determines whether the app can monitor the device’s battery.
- [var batteryLevel: Float](batterylevel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterylevel))
  The battery’s current percent charge.
- [var batteryState: WKInterfaceDeviceBatteryState](batterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/batterystate))
  The device’s battery state.
- [enum WKInterfaceDeviceBatteryState](wkinterfacedevicebatterystate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevicebatterystate))
  The battery’s charging state.
### Accessing Water Resistance and Lock
- [var waterResistanceRating: WKWaterResistanceRating](waterresistancerating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/waterresistancerating))
  The Apple Watch water-resistance rating.
- [enum WKWaterResistanceRating](wkwaterresistancerating.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkwaterresistancerating))
  Values indicating the water-resistance rating.
- [var isWaterLockEnabled: Bool](iswaterlockenabled.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/iswaterlockenabled))
  A Boolean value that indicates whether the water lock is enabled.
- [func enableWaterLock()](enablewaterlock().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/enablewaterlock()))
  Disables the Apple Watch touch screen to prevent accidental taps while submerged.
### Playing Haptic Feedback
- [func play(WKHapticType)](play(_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/play(_:)))
  Gives haptic feedback to the user.
- [enum WKHapticType](wkhaptictype.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkhaptictype))
  Constant indicating the style of feedback to deliver using haptics.
### Streaming Audio
- [var supportsAudioStreaming: Bool](supportsaudiostreaming.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/supportsaudiostreaming))
  A Boolean value that indicates whether the device supports audio streaming.
### Validating In-App Purchases
- [var identifierForVendor: UUID?](identifierforvendor.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedevice/identifierforvendor))
  An alphanumeric string that uniquely identifies a device to the app’s vendor.

## Relationships

### Inherits From
- NSObject ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class))
### Conforms To
- CVarArg ([Apple Docs](https://developer.apple.com/documentation/Swift/CVarArg))
- CustomDebugStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomDebugStringConvertible))
- CustomStringConvertible ([Apple Docs](https://developer.apple.com/documentation/Swift/CustomStringConvertible))
- Equatable ([Apple Docs](https://developer.apple.com/documentation/Swift/Equatable))
- Hashable ([Apple Docs](https://developer.apple.com/documentation/Swift/Hashable))
- NSObjectProtocol ([Apple Docs](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol))

## See Also

- [Setting up a watchOS project](setting-up-a-watchos-project.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/setting-up-a-watchos-project))
  Create a new watchOS project or add a watch target to an existing iOS project.
- [class WKApplication](wkapplication.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplication))
  The centralized point of control and coordination for apps with a single watchOS app target.
- [protocol WKApplicationDelegate](wkapplicationdelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate))
  A collection of methods that manages the app-level behavior for a single-target watchOS app.
- [class WKExtension](wkextension.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextension))
  The centralized point of control and coordination for extension-based apps running in watchOS.
- [protocol WKExtensionDelegate](wkextensiondelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextensiondelegate))
  A collection of methods that manages the app-level behavior of a WatchKit extension.
- [func WKApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>, String?) -> Int32](wkapplicationmain(_:_:_:).md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationmain(_:_:_:)))
  Creates the application object and the application delegate, and sets up the app’s event cycle.
- WKPrefersNetworkUponForeground ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WKPrefersNetworkUponForeground))
  A Boolean value that indicates whether an app requires network access on launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkinterfacedevice)*