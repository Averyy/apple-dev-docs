# Handling Common State Transitions

**Framework**: WatchKit

Detect and respond to common state transitions.

#### Overview

A watchOS app runs in different states depending on the app’s current context. At any time, the app is in one of the following states: not running, inactive, active, background, or suspended. The app changes state over time based on events triggered by the user and the system.

![A figure showing the state changes for a watchOS app.](https://docs-assets.developer.apple.com/published/9de6b80655861e54b065d429c36d2980/media-3693091%402x.png)

The figure shows the three main types of transitions that occur during an app’s life cycle.

-  Launching from not running to either the inactive or background state.
-  Switching between the inactive and active states.

Switching between the background and inactive states.

##### Launch and Enter the Active State

An app begins in the  state. The user hasn’t launched the watchOS app, or the system suspended and then purged the app from memory.

When the user or the system launches the app, it starts in the  state. The app runs in the foreground but isn’t receiving actions from controls or gestures; however, it may be executing other code. A newly launched app usually stays in this state only briefly as it transitions to the active state. When an active app transitions to this state, it should quiet itself and prepare to go to the background.

The app then enters the  state. It runs in the foreground and receiving actions from controls and gestures. This is the normal mode for apps running on screen.

##### Transition to the Background

If the user lowers their arm or stops interacting with the app, it enters the  state. The system can also launch apps into the background when running background sessions or performing background tasks. While in the background state, the system gives the app a small amount of background execution time before suspending the app.

Because the system can purge suspended apps without warning, use SwiftUI’s [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment `value`, or your extension delegate’s [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) method to determine when your app transitions from the active state to the background. Save any data you need to recreate your app’s current state. If needed, you can request additional background execution time by calling the [`ProcessInfo`](https://developer.apple.com/documentation/Foundation/ProcessInfo) class’s [`performExpiringActivity(withReason:using:)`](https://developer.apple.com/documentation/foundation/processinfo/1617030-performexpiringactivity) method.

##### Transition to the Suspended State

Finally, the app transitions from the background state to the  state. The system keeps the app in memory but isn’t executing its code. The system suspends apps that are in the background and don’t have any pending tasks to complete.

The system may purge suspended apps at any time to make room for other apps. The system silently purges suspended apps. The suspended apps don’t wake, and don’t receive any notifications before the system purges them.

The system tries to keep frequently used apps in memory, allowing them to resume as quickly as possible. Specifically, the system preserves the most recently executed app, any apps that are in the Dock, and any apps that have a complication on the currently active watch face. If memory constraints force the system to purge one of these apps, the system relaunches the app as soon as more memory becomes available.

##### Handle App State Changes

SwiftUI updates the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value as your app changes from state to state. To respond to these changes, start by reading the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) out of the environment by using the [`Environment`](https://developer.apple.com/documentation/SwiftUI/Environment) property wrapper.

```swift
@Environment(\.scenePhase) private var scenePhase
```

Then use the [`onChange(of:perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onChange(of:perform:)) modifier to respond to changes in the app’s state.

```swift
MyView()
    .onChange(of: scenePhase) { phase in
        switch phase {
        case .active:
            // The app has become active.
            break
        case .inactive:
            // The app has become inactive.
            break
        case .background:
            // The app has moved to the background.
            break
        @unknown default:
            fatalError("The app has entered an unknown state.")
        }
    }
```

For watchOS 7 and later, the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment value replaces many of the life cycle events previously handled by the WatchKit extension delegate, such as [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) and [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()).

##### Understand Common Transitions

There is no direct relationship between the app’s state and the interface’s state. For example, the app may be inactive while the interface is active. The following table shows the app and interface states in most common situations.

| Situation | App state | Interface state |
| --- | --- | --- |
| Running on screen | Active | Active |
| Running in the dock | Inactive, and the extension’s [`isApplicationRunningInDock`](https://developer.apple.com/documentation/watchkit/wkextension/isapplicationrunningindock) property is [`true`](https://developer.apple.com/documentation/swift/true) | Active, shown in the dock |
| Running as the frontmost app | Inactive | Inactive |
| Displaying a dynamic notification interface | Inactive or background | Notification interface is active |
| Processing a snapshot background task | Background | Active, but not shown on screen |
| Processing another background task | Background | Inactive |
| Running a background session | Background | Inactive |

When transitioning between both app and interface states, the exact flow depends on the app’s starting and ending conditions, as well as other considerations (for example, if the app has a complication in the current watch face, or if the app is currently the frontmost app). Some of the most common transitions include launching the app, going to the background, and resuming.

The app launches when it isn’t running, and the user explicitly starts the app—for example, by tapping the app icon on the home screen.

1.  transitions to the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state.  calls the extension delegate’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()) method and sets the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) environment variable to [`ScenePhase.inactive`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/inactive).
2.  instantiates the app’s initial scene, and its root view and calls the extension delegate’s [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()) method.
3.  transitions to the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.  calls the extension delegate’s [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) method and sets the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) value to [`ScenePhase.active`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/active).
4.  appears on screen. The system calls the root view’s [`onAppear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onAppear(perform:)) method.

The app goes to the background when it is running on screen in the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.

1.  calls the extension delegate’s [`applicationWillResignActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()) method.
2.  transitions to the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state, calls the view’s [`onDisappear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onDisappear(perform:)) method, and sets the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) value to [`ScenePhase.inactive`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/inactive). The app may continue to run in an inactive state as long as the app is the frontmost app. For more information, see [`Taking Advantage of Frontmost App State`](https://developer.apple.com/documentation/watchkit/taking-advantage-of-frontmost-app-state).
3.  transitions to the [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) state.  calls the extension delegate’s [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) method and sets the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) value to [`ScenePhase.background`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/background).
4.  suspends the app.****

The app resumes when the app is running in the background, or is suspended, and the user activates the app, for example, by tapping its complication on the active watch face.

1. If suspended but in memory,  restarts in the [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) state.
2.  calls the extension delegate’s [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()) method.
3.  transitions to the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.  calls the extension delegate’s [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) method and sets the [`scenePhase`](https://developer.apple.com/documentation/SwiftUI/EnvironmentValues/scenePhase) value to [`ScenePhase.active`](https://developer.apple.com/documentation/SwiftUI/ScenePhase/active).
4. The system calls the current view’s [`onAppear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onAppear(perform:)) method.

Except for [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()), the system only calls the extension delegate’s life cycle methods for the watchOS app’s main interface. It doesn’t call them when the system displays any other supplementary interfaces. For example, they don’t occur when the system launches the app to update complications or to display custom notification interfaces. For notifications, use the root view’s [`onAppear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onAppear(perform:)) and [`onDisappear(perform:)`](https://developer.apple.com/documentation/SwiftUI/View/onDisappear(perform:)) methods to track the state of the interface.

## See Also

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [Handling User Activity](handling-user-activity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-user-activity))
  Detect and respond to user activity information from Handoff or a complication.
- [Taking Advantage of Frontmost App State](taking-advantage-of-frontmost-app-state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/taking-advantage-of-frontmost-app-state))
  Understand the frontmost app state, and the features it provides to your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions)*