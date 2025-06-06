# Using extended runtime sessions

**Framework**: Watchkit

Create an extended runtime session that continues running your app after the user stops interacting with it.

#### Overview

An app running on Apple Watch normally transitions to the background and becomes suspended when the user lowers their wrist. However, your app can use both background sessions and extended runtime sessions to continue running after the user stops interacting with it.

With background sessions, your app continues to run in the background, but the sessions can only monitor workouts, track the user’s location, or play audio files. Extended runtime sessions, on the other hand, expand on this ability and give your app several different session types to choose from. Not all of these sessions run in the background. Some keep your app active and running as the frontmost app instead. Extended runtime sessions support the following session types:

Select a session type based on the app’s intended use—not based on the features that the session provides. Extended runtime sessions let the app continue to communicate with a Bluetooth device, process data, or play sounds or haptics, even after the watch’s screen turns off.

> ❗ **Important**:  To maintain high performance on Apple Watch, limit the amount of work performed during an extended runtime session. If your app sustains high CPU usage over a period of time, the system may cancel the session (see [`WKExtendedRuntimeSessionErrorCode.exceededResourceLimits`](wkextendedruntimesessionerrorcode/exceededresourcelimits.md)). Use Xcode’s CPU report tool or the time profiler in Instruments to test and minimize your app’s CPU usage.

 To maintain high performance on Apple Watch, limit the amount of work performed during an extended runtime session. If your app sustains high CPU usage over a period of time, the system may cancel the session (see [`WKExtendedRuntimeSessionErrorCode.exceededResourceLimits`](wkextendedruntimesessionerrorcode/exceededresourcelimits.md)). Use Xcode’s CPU report tool or the time profiler in Instruments to test and minimize your app’s CPU usage.

##### Set Up the Session

Before starting an extended runtime session, enable your WatchKit extension’s Background Modes capability and select your app’s session type (see [`Figure 1`](using_extended_runtime_sessions#3189143.md)). Each app can only support one type of extended runtime session, although it’s possible to support other background modes in combination with extended runtime.

![A screenshot showing the Session Type setting for the Background Modes capability.](https://docs-assets.developer.apple.com/published/451eab875e5b686824dd5c24b4cfe380/media-3189143%402x.png)

A physical therapy app, for example, might use a [`WKExtendedRuntimeSession`](wkextendedruntimesession.md) for range-of-motion exercises and an [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) for vigorous cross-training. Using separate sessions keeps the range-of-motion exercise from impacting the user’s Move and Exercise rings, but the user still gets full credit for the cross-training.

To set up the session, instantiate a [`WKExtendedRuntimeSession`](wkextendedruntimesession.md) object, and assign your delegate. The system automatically creates a session based on the session type specified in your Background Modes capabilities.

```swift
// Create the session object.
session = WKExtendedRuntimeSession()

// Assign the delegate.
session.delegate = self
```

Implement the [`WKExtendedRuntimeSessionDelegate`](wkextendedruntimesessiondelegate.md) methods to track your session.

```swift
// MARK:- Extended Runtime Session Delegate Methods
func extendedRuntimeSessionDidStart(_ extendedRuntimeSession: WKExtendedRuntimeSession) {
    // Track when your session starts.
}

func extendedRuntimeSessionWillExpire(_ extendedRuntimeSession: WKExtendedRuntimeSession) {
    // Finish and clean up any tasks before the session ends. 
}
    
func extendedRuntimeSession(_ extendedRuntimeSession: WKExtendedRuntimeSession, didInvalidateWith reason: WKExtendedRuntimeSessionInvalidationReason, error: Error?) {
    // Track when your session ends.
    // Also handle errors here.
}
```

Finally, start your session. For most session types, you start the session immediately by calling [`start()`](wkextendedruntimesession/start().md). For alarm sessions, you can schedule the session to start any time within the next 36 hours by calling [`start(at:)`](wkextendedruntimesession/start(at:).md).

```swift
session.start()
```

You must always start or schedule the extended runtime session when your app state is in the [`WKApplicationState.active`](wkapplicationstate/active.md) state.

The session automatically stops when its allotted time expires. You can track the time remaining using its [`expirationDate`](wkextendedruntimesession/expirationdate.md) property. You can also stop a session by calling [`invalidate()`](wkextendedruntimesession/invalidate().md).

For sessions started with [`start(at:)`](wkextendedruntimesession/start(at:).md), you can only call [`invalidate()`](wkextendedruntimesession/invalidate().md) when the app is active. For all other sessions, you can call [`invalidate()`](wkextendedruntimesession/invalidate().md) to end a session at any time.

```swift
@IBAction func stopButton() {
    session.invalidate()
}
```

##### Understand Session Behaviors

Extended runtime sessions gain the following features, based on the session type.

| Session type | Runtime | Schedulable | Time limit |
| --- | --- | --- | --- |
| Self care | Frontmost | No | 10 minutes |
| Mindfulness | Frontmost | No | 1 hour |
| Physical therapy | Background | No | 1 hour |
| Smart alarm | Background | Yes | 30 minutes |

 sessions continue to run in the foreground. The watch screen doesn’t need to remain on to keep your app alive. The session continues until the time limit expires, your app invalidates the session, or the user explicitly leaves your app (for example, by pressing the digital crown or switching to a different app).

 sessions continue to run in the background, even if the user dismisses the app or launches another app. Background sessions continue to run until the time limit expires, or your app invalidates the session.

Finally, s_chedulable_ sessions can start any time within the next 36 hours. You must schedule the session by calling [`start(at:)`](wkextendedruntimesession/start(at:).md) while your app is in the [`WKApplicationState.active`](wkapplicationstate/active.md) state. The system can then suspend or terminate your app without affecting the session. The system relaunches your app as needed to handle a scheduled session, calling your extension delegate’s [`handle(_:)`](wkextensiondelegate/handle(_:)-4qxgv.md) method. If you don’t set the session’s delegate in the [`handle(_:)`](wkextensiondelegate/handle(_:)-4qxgv.md) method, the system ends the session. Additionally, you can only schedule one session at a time; if you need to reschedule a session, invalidate the current session, and schedule a new one.

After the session starts, the app continues to run in the background until the time limit expires, or your app invalidates the session. During the session, your app must trigger the alarm by calling the session’s [`notifyUser(hapticType:repeatHandler:)`](wkextendedruntimesession/notifyuser(haptictype:repeathandler:).md) method. If your app isn’t active, playing the haptic displays a system alarm alert to the user.

If you fail to play a haptic during the session, the system displays a warning and offers to disable future sessions.

## See Also

- [Background execution](background-execution.md)
  Manage background sessions and tasks.
- [Life cycles](life-cycles.md)
  Receive and respond to life-cycle notifications.
- [class WKExtendedRuntimeSession](wkextendedruntimesession.md)
  A session that continues to run your app after the user has stopped interacting.
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md)
  Keep your complications up-to-date by reading values from a Bluetooth peripheral while your app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions)*