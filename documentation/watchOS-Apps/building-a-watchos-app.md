# Building a watchOS app

**Framework**: watchOS apps

Set up your app’s life cycle and create its user interface with SwiftUI.

#### Overview

Develop powerful, personal apps for Apple Watch using SwiftUI, a declarative framework for building user interfaces on all of Apple’s platforms. You can create rich user interfaces by composing simple views — which perform a single, focused task — into larger, more complex layouts. Your app describes the correct layout for its views based on its current state. SwiftUI detects changes to the state and updates the views accordingly.

On watchOS, SwiftUI gives you considerably more freedom, power, and control than user interfaces laid out and designed in a storyboard. For example, [`List`](https://developer.apple.com/documentation/swiftui/list) has a number of features that aren’t supported by [`WKInterfaceTable`](https://developer.apple.com/documentation/watchkit/wkinterfacetable), such as the platter style, swipe actions (shown below), and row reordering.

![A screenshot of a watch face displaying a list. The middle row shows the list’s delete swipe action. The row shifts to the left, revealing a large X.](/images/com.apple.watchOS-Apps/building_a_watchos_app-1@2x.png)

Additionally, you can preview your SwiftUI code in Xcode’s canvas. You can design, build, and test your interfaces without ever running your app.

![A screenshot showing Xcode with the circle image selected in the preview.](/images/com.apple.watchOS-Apps/building_a_watchos_app-2@2x.png)

SwiftUI also provides watch-specific representations of tab and navigation views, with fully customizable navigation bars and customizable toolbar items for confirmation, cancellation, and destructive actions. You can also use SwiftUI to manage your app’s life cycle. To learn more about SwiftUI, see [`Introducing SwiftUI`](https://developer.apple.com/tutorials/swiftui).

##### Set Up the Root View

To manage your app’s life cycle with SwiftUI, create a structure that adopts the [`App`](https://developer.apple.com/documentation/swiftui/app) protocol in your watchOS app target.

```swift
import SwiftUI

@main
struct MyProject_Watch_App: App {
}
```

The [`@main`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes) attribute indicates this is the entry point for your app. Each app can have only one entry point.

Inside the structure, define the app’s [`body`](https://developer.apple.com/documentation/swiftui/app/body-swift.property). The `body` automatically composes a collection of [`Scene`](https://developer.apple.com/documentation/swiftui/scene) instances into a single, compound `Scene`.

```swift
@main
struct MyProject_Watch_App: App {
    var body: some Scene {
    }
}
```

Next, add a `Scene` or your app’s root view. For a watchOS app, you typically create a [`WindowGroup`](https://developer.apple.com/documentation/swiftui/windowgroup) scene that wraps a [`NavigationView`](https://developer.apple.com/documentation/swiftui/navigationview) around your app’s root view. The `NavigationView` provides a navigation stack and title area for your app.

```swift
@main
struct MyProject_Watch_App: App {
    var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
        }
    }
}
```

When your app launches, it displays the view hierarchy defined by the window group.

You can also add scenes for notification categories.

```swift
var body: some Scene {
    WindowGroup {
        NavigationView {
            ContentView()
        }
    }

    WKNotificationScene(controller: NotificationController.self, category: "myCategory")
}
```

When the system receives a notification with a matching category, it displays a dynamic view specified by the notification controller. You can create a [`WKUserNotificationHostingController`](https://developer.apple.com/documentation/swiftui/wkusernotificationhostingcontroller) subclass for each notification category supported by your app.

```swift
import SwiftUI
import UserNotifications

class NotificationController: WKUserNotificationHostingController<NotificationLongLook> {

    var content:UNNotificationContent!
    var date:Date!

    override var body: NotificationLongLook{
        NotificationLongLook(content: content, date: date)
    }

    override class var isInteractive: Bool { true }

    override func didReceive(_ notification: UNNotification) {
        content = notification.request.content
        date = notification.date
    }
}
```

For more information, see [`Customizing your long-look interface`](customizing-your-long-look-interface.md).

##### Respond to App Events in Swiftui

Your app can respond to many app events directly in SwiftUI.

SwiftUI updates the [`scenePhase`](https://developer.apple.com/documentation/swiftui/environmentvalues/scenephase) environment value as your app changes state. To update a view based on these changes, you can use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/swiftui/view/onchange(of:perform:)) modifier. For more information, see [`Handling Common State Transitions`](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions).

SwiftUI also provides view modifiers for handling user activity and background tasks:

- Use [`onContinueUserActivity(_:perform:)`](https://developer.apple.com/documentation/swiftui/view/oncontinueuseractivity(_:perform:)) to handle incoming [`NSUserActivity`](https://developer.apple.com/documentation/foundation/nsuseractivity) objects. For more information, see [`Handling User Activity`](https://developer.apple.com/documentation/watchkit/handling-user-activity).
- Use [`backgroundTask(_:action:)`](https://developer.apple.com/documentation/swiftui/scene/backgroundtask(_:action:)) to handle incoming [`BackgroundTask`](https://developer.apple.com/documentation/swiftui/backgroundtask) instances. For more information, see [`Using background tasks`](https://developer.apple.com/documentation/watchkit/using-background-tasks).

##### Respond to App Events Using an App Delegate

You need an app delegate to handle the following events:

- Life cycle events, like [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()), that aren’t handled by the [`scenePhase`](https://developer.apple.com/documentation/swiftui/environmentvalues/scenephase) environment variable
- `userInfo` dictionaries from either handoff or complications
- Remote Now Playing activity
- Workout configurations and recovery
- Extended runtime sessions
- Registration of remote notifications

To add an app delegate to your app, create a class that adopts the [`WKApplicationDelegate`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate) protocol. In this class, implement the methods needed to handle your app’s events. Then use the [`WKApplicationDelegateAdaptor`](https://developer.apple.com/documentation/swiftui/wkapplicationdelegateadaptor) property wrapper to declare a variable for your delegate.

```swift
import SwiftUI
import WatchKit

@main
struct MyProject_Watch_App: App {

    @WKApplicationDelegateAdaptor var appDelegate: MyAppDelegate

    var body: some Scene {
        WindowGroup {
            NavigationView {
                ContentView()
            }
        }

        WKNotificationScene(controller: NotificationController.self, category: "myCategory")
    }
}
```

When your app launches, the system instantiates your delegate class and calls [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()). Use this method to perform any additional configuration that your delegate requires. After it returns, the system begins calling your delegate methods when the corresponding events occur.

## See Also

- [Creating a watchOS app](https://developer.apple.com/tutorials/swiftui/creating-a-watchos-app)
- [Life cycles](../watchkit/life-cycles.md)
  Receive and respond to life-cycle notifications.
- [Creating an intuitive and effective UI in watchOS 10](creating-an-intuitive-and-effective-ui-in-watchos-10.md)
  Provide an even more streamlined, consistent, and glanceable user experience with new design features.
- [Updating your app and widgets for watchOS 10](updating-your-app-and-widgets-for-watchos-10.md)
  Integrate SwiftUI elements and watch-specific features, and build widgets for the Smart Stack.
- [watchOS updates](../updates/watchos.md)
  Learn about important changes to watchOS.
- [Migrating to a single-target watchOS app](migrating-to-a-single-target-watchos-app.md)
  Adopt the single-target configuration to simplify your project and avoid ambiguity about where to store resources and apply entitlements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-apps/building_a_watchos_app)*