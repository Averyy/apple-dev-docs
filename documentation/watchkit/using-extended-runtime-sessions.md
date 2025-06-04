# Using extended runtime sessions

**Framework**: Watchkit

Create an extended runtime session that continues running your app after the user stops interacting with it.

## Overview

An app running on Apple Watch normally transitions to the background and becomes suspended when the user lowers their wrist. However, your app can use both background sessions and extended runtime sessions to continue running after the user stops interacting with it.

With background sessions, your app continues to run in the background, but the sessions can only monitor workouts, track the user’s location, or play audio files. Extended runtime sessions, on the other hand, expand on this ability and give your app several different session types to choose from. Not all of these sessions run in the background. Some keep your app active and running as the frontmost app instead. Extended runtime sessions support the following session types:

Select a session type based on the app’s intended use—not based on the features that the session provides. Extended runtime sessions let the app continue to communicate with a Bluetooth device, process data, or play sounds or haptics, even after the watch’s screen turns off.

> ❗ **Important**:  To maintain high performance on Apple Watch, limit the amount of work performed during an extended runtime session. If your app sustains high CPU usage over a period of time, the system may cancel the session (see [`WKExtendedRuntimeSessionErrorCode.exceededResourceLimits`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits)). Use Xcode’s CPU report tool or the time profiler in Instruments to test and minimize your app’s CPU usage.

 To maintain high performance on Apple Watch, limit the amount of work performed during an extended runtime session. If your app sustains high CPU usage over a period of time, the system may cancel the session (see [`WKExtendedRuntimeSessionErrorCode.exceededResourceLimits`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessionerrorcode/exceededresourcelimits)). Use Xcode’s CPU report tool or the time profiler in Instruments to test and minimize your app’s CPU usage.

Before starting an extended runtime session, enable your WatchKit extension’s Background Modes capability and select your app’s session type (see [`Figure 1`](https://developer.apple.com/documentation/watchkit/using_extended_runtime_sessions#3189143)). Each app can only support one type of extended runtime session, although it’s possible to support other background modes in combination with extended runtime.

A physical therapy app, for example, might use a [`WKExtendedRuntimeSession`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession) for range-of-motion exercises and an [`HKWorkoutSession`](https://developer.apple.com/documentation/HealthKit/HKWorkoutSession) for vigorous cross-training. Using separate sessions keeps the range-of-motion exercise from impacting the user’s Move and Exercise rings, but the user still gets full credit for the cross-training.

To set up the session, instantiate a [`WKExtendedRuntimeSession`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession) object, and assign your delegate. The system automatically creates a session based on the session type specified in your Background Modes capabilities.

```swift
// Create the session object.
session = WKExtendedRuntimeSession()

// Assign the delegate.
session.delegate = self
```

Implement the [`WKExtendedRuntimeSessionDelegate`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesessiondelegate) methods to track your session.

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

Finally, start your session. For most session types, you start the session immediately by calling [`start()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start()). For alarm sessions, you can schedule the session to start any time within the next 36 hours by calling [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)).

```swift
session.start()
```

You must always start or schedule the extended runtime session when your app state is in the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.

The session automatically stops when its allotted time expires. You can track the time remaining using its [`expirationDate`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/expirationdate) property. You can also stop a session by calling [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()).

For sessions started with [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)), you can only call [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) when the app is active. For all other sessions, you can call [`invalidate()`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/invalidate()) to end a session at any time.

```swift
@IBAction func stopButton() {
    session.invalidate()
}
```

Extended runtime sessions gain the following features, based on the session type.

| r | o | w |
| --- | --- | --- |
| [{'inlineContent': [{'type': 'text', 'text': 'Session type'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Runtime'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Schedulable', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Time limit', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Self care', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Frontmost'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'No'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': '10 minutes', 'type': 'text'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'type': 'text', 'text': 'Mindfulness'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Frontmost', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'No', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': '1 hour'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Physical therapy', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Background', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'No', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': '1 hour'}], 'type': 'paragraph'}] |
| [{'inlineContent': [{'text': 'Smart alarm', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'text': 'Background', 'type': 'text'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': 'Yes'}], 'type': 'paragraph'}] | [{'inlineContent': [{'type': 'text', 'text': '30 minutes'}], 'type': 'paragraph'}] |

 sessions continue to run in the foreground. The watch screen doesn’t need to remain on to keep your app alive. The session continues until the time limit expires, your app invalidates the session, or the user explicitly leaves your app (for example, by pressing the digital crown or switching to a different app).

 sessions continue to run in the background, even if the user dismisses the app or launches another app. Background sessions continue to run until the time limit expires, or your app invalidates the session.

Finally, s_chedulable_ sessions can start any time within the next 36 hours. You must schedule the session by calling [`start(at:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/start(at:)) while your app is in the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state. The system can then suspend or terminate your app without affecting the session. The system relaunches your app as needed to handle a scheduled session, calling your extension delegate’s [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method. If you don’t set the session’s delegate in the [`handle(_:)`](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/handle(_:)-4qxgv) method, the system ends the session. Additionally, you can only schedule one session at a time; if you need to reschedule a session, invalidate the current session, and schedule a new one.

After the session starts, the app continues to run in the background until the time limit expires, or your app invalidates the session. During the session, your app must trigger the alarm by calling the session’s [`notifyUser(hapticType:repeatHandler:)`](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession/notifyuser(haptictype:repeathandler:)) method. If your app isn’t active, playing the haptic displays a system alarm alert to the user.

If you fail to play a haptic during the session, the system displays a warning and offers to disable future sessions.

## Code Examples

### Example

```swift
// Create the session object.
session = WKExtendedRuntimeSession()

// Assign the delegate.
session.delegate = self
```

### Example

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

### Example

```swift
session.start()
```

### Example

```swift
@IBAction func stopButton() {
    session.invalidate()
}
```

## See Also

- [Background execution](background-execution.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/background-execution))
- [Life cycles](life-cycles.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/life-cycles))
- [class WKExtendedRuntimeSession](wkextendedruntimesession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession))
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions)*