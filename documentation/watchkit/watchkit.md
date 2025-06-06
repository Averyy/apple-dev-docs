# WatchKit

**Framework**: Watchkit  
**Kind**: module

Build watchOS apps that use features the app delegate monitors or controls, such as background tasks and extended runtime sessions.

**Availability**:
- watchOS 2.0+

#### Overview

The WatchKit framework provides infrastructure for creating watchOS apps, including an extension delegate that manages background tasks, extended runtime sessions, and Siri intents. The framework also performs other support tasks, such as accessing information about the user’s Apple Watch.

![An illustration showing a blueprint. The central image displays a drawing of an Apple Watch with gears inside it. There are sketches of icons on either side of the watch.](https://docs-assets.developer.apple.com/published/66915464f240eff7cbd25784f1bb497e/media-3987848%402x.png)

You can also use WatchKit to design your app’s user interface in a storyboard, connecting UI elements to an interface controller.

> **Note**:  Building your app with SwiftUI gives you more control over the user interface than designing it in a storyboard. When creating a new watchOS app, strongly consider using [`SwiftUI`](https://developer.apple.com/documentation/SwiftUI). For more information, see [`Building a watchOS app`](https://developer.apple.com/documentation/watchOS-Apps/building_a_watchos_app).

For more information on building watchOS apps, see [`watchOS apps`](https://developer.apple.com/documentation/watchOS-Apps).

## Topics

### App structure
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
- [class WKInterfaceDevice](wkinterfacedevice.md)
  An object that provides information about the user’s Apple Watch.
- [WKPrefersNetworkUponForeground](../BundleResources/Information-Property-List/WKPrefersNetworkUponForeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
### Runtime management
- [Background execution](background-execution.md)
  Manage background sessions and tasks.
- [Life cycles](life-cycles.md)
  Receive and respond to life-cycle notifications.
- [Using extended runtime sessions](using-extended-runtime-sessions.md)
  Create an extended runtime session that continues running your app after the user stops interacting with it.
- [class WKExtendedRuntimeSession](wkextendedruntimesession.md)
  A session that continues to run your app after the user has stopped interacting.
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md)
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.
### User interface
- [Storyboard support](storyboard-support.md)
  Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.
- [struct NowPlayingView](nowplayingview.md)
  A view that displays the system’s Now Playing interface so that the user can control audio.
### Errors
- [struct WatchKitError](watchkiterror.md)
  An error reported by WatchKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WatchKit)*