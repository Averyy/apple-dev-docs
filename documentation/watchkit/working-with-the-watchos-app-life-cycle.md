# Working with the watchOS app life cycle

**Framework**: Watchkit

Learn how the watchOS app life cycle operates and responds to life cycle notification methods.

## Overview

WatchKit reports changes in your app’s execution state to your extension delegate object. State changes correspond to major events in the lifetime of your app, and the state changes in a watchOS app are analogous to the state changes of an iOS app. For each state change, perform relevant tasks, such as loading shared resources and configuring your initial user interface. The following table lists the possible state of the app and the implications for your app.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'State'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Description'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Not running', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The watchOS app isn’t running. The user hasn’t launched the watchOS app, or the system suspended and then purged the app.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Inactive'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The watchOS app is running in the foreground, but isn’t receiving actions from controls or gestures; however, it may be executing other code. A newly launched app usually stays in this state only briefly as it transitions to the active state. An active app that transitions to this state should quiet itself and prepare to transition to the background.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Active', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The watchOS app is running in the foreground and receiving actions from controls and gestures. This is the normal mode for apps running onscreen.', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Background'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'The system has given the watchOS app a small amount of background execution time. The system gives apps background execution time when running a background session, when performing background tasks, and before suspending the app. '}, {'identifier': 'spacer', 'type': 'image'}, {'type': 'text', 'text': '  Because the system can purge suspended apps without warning, use the extension delegate’s '}, {'isActive': True, 'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKExtensionDelegate/applicationDidEnterBackground()', 'type': 'reference'}, {'type': 'text', 'text': ' method to save any data you need to re-create your app’s current state. If needed, you can request additional background execution time by calling the '}, {'isActive': True, 'identifier': 'doc://com.apple.documentation/documentation/Foundation/ProcessInfo', 'type': 'reference'}, {'type': 'text', 'text': ' class’s '}, {'isActive': True, 'identifier': 'doc://com.apple.documentation/documentation/foundation/processinfo/1617030-performexpiringactivity', 'type': 'reference'}, {'type': 'text', 'text': ' method.'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Suspended'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'The app is in memory but isn’t executing code. The system suspends apps that are in the background and don’t have any pending tasks to complete. The system may purge suspended apps at any time to make room for other apps. The system silently purges suspended apps. The suspended apps don’t wake, and don’t receive any notifications before the system purges them. ', 'type': 'text'}, {'type': 'image', 'identifier': 'spacer'}, {'text': ' The system tries to keep frequently used apps in memory, allowing them to resume as quickly as possible. Specifically, the system preserves the most recently executed app, any apps that are in the Dock, and any apps that have a complication on the currently active watch face. If memory constraints force the system to purge one of these apps, the system relaunches the app as soon as more memory becomes available.', 'type': 'text'}], 'type': 'paragraph'}] |

The following diagram shows the state changes that occur for a watchOS app and the delegate methods that watchOS calls when those changes occur.

In the preceding diagram:

-  When transitioning from not running to either the inactive or background state, the system calls the extension delegate’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()) method.
-  When transitioning between the inactive and active states, the system calls either the [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) or [`applicationWillResignActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()) method.
-  When transitioning between the background and inactive states, the system calls either the [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()) or [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) method.

Except for [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()), the system only calls the extension delegate’s life cycle methods for the watchOS app’s main interface. The system doesn’t call the delegate methods when it displays any other supplementary interfaces. For example, it doesn’t call the methods when it launches the app to update complications or to display custom notification interfaces. For notifications, use the notification controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) and [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) methods to track the state of the interface.

The watch app runs in different states depending on the app’s current context. Also, there’s no direct relationship between the app’s state and the interface’s state. For example, the app may be inactive while the interface is active. The following table shows the app and interface states in most common situations.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Situation'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'App state', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Interface state'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Running onscreen', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Active', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Active', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Running in the dock'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Inactive, and the extension’s '}, {'identifier': 'doc://com.apple.watchkit/documentation/WatchKit/WKExtension/isApplicationRunningInDock', 'type': 'reference', 'isActive': True}, {'type': 'text', 'text': ' property is '}, {'identifier': 'doc://com.apple.documentation/documentation/swift/true', 'type': 'reference', 'isActive': True}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Active, shown in the dock.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Running as the frontmost app', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Inactive', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Inactive', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Displaying a dynamic notification interface', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Inactive or background', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Notification interface is active'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Processing a snapshot background task'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Background'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'Active, but not shown onscreen', 'type': 'text'}]}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Processing another background task'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Background'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Inactive'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Running a background session'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Background', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Inactive'}], 'type': 'paragraph'}] |

When transitioning between states, the exact flow depends on the app’s starting and ending conditions, as well as other considerations — for example, if the app has a complication in the current watch face, or if the app is currently the frontmost app, and so on. Some of the most common transitions include when an app launches, goes to the background, or resumes.

The app launches when it isn’t running, and the user explicitly starts the app — for example tapping the app icon on the home screen.

1. The app_ _transitions to the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state. The system calls the extension delegate’s [`applicationDidFinishLaunching()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidfinishlaunching()) method.
2. The system instantiates the initial interface controller and calls its [`awake(withContext:)`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/awake(withcontext:)) method.
3. The app transitions to the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state. The system calls the extension delegate’s [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) method.
4. The system calls the initial interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method.
5.  appears onscreen. The system calls the initial interface controller’s [`didAppear()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/didappear()) method.

The app goes to the background when it’s running onscreen in the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state, and the user lowers their arm or the screen turns off. If the user explicitly closes the app, by pressing the digital crown or covering the screen, the app doesn’t become the frontmost app, and doesn’t remain in the inactive state, but transitions quickly to the background instead.

1.  calls the extension delegate’s [`applicationWillResignActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillresignactive()) method.
2.  transitions to the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state. The app remains in this state as long as it’s the frontmost app (by default, 2 minutes).
3.  transitions to the [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) state.  calls the extension delegate’s [`applicationDidEnterBackground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidenterbackground()) method.
4.  calls the presented interface controller’s [`didDeactivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/diddeactivate()) method.
5.  suspends the app.****

The app resumes when the app is running in the background, or is suspended, and the user activates the app, for example, by tapping its complication on the active watch face.

1. If suspended but in memory,  restarts in the [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) state.
2.  calls the extension delegate’s [`applicationWillEnterForeground()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationwillenterforeground()) method.
3.  transitions to the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.  calls the extension delegate’s [`applicationDidBecomeActive()`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/applicationdidbecomeactive()) method.
4.  calls the initial interface controller’s [`willActivate()`](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller/willactivate()) method.

When the system receives background data, it may not immediately wake the watchOS app to process that data. Instead, it may delay delivery of the data to preserve battery life.

If the app is currently running—either active and onscreen, or inactive and the frontmost app—the system immediately delivers the data to the app. If the app is in the background, the system wakes the app within 10 minutes to deliver the data.

## See Also

- [static func main()](main().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/main()))
- [func applicationDidFinishLaunching()](applicationdidfinishlaunching().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidfinishlaunching()))
- [func applicationDidBecomeActive()](applicationdidbecomeactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidbecomeactive()))
- [func applicationWillResignActive()](applicationwillresignactive().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillresignactive()))
- [func applicationWillEnterForeground()](applicationwillenterforeground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationwillenterforeground()))
- [func applicationDidEnterBackground()](applicationdidenterbackground().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/applicationdidenterbackground()))
- [func deviceOrientationDidChange()](deviceorientationdidchange().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationdelegate/deviceorientationdidchange()))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle)*