# Life cycles

**Framework**: Watchkit

Receive and respond to life-cycle notifications.

## Overview

The system reports changes in your app’s execution state to your SwiftUI environment and your extension delegate object. State changes correspond to major events in the lifetime of your app, such as the app launching or moving into the background. Use the state changes to trigger relevant tasks, such as loading shared resources and configuring your initial user interface. The table below shows the possible states and their implications for your app.

| r | o | w |
| --- | --- | --- |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'State', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Description'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Not running'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The watchOS app isn’t running.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'Inactive'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The watchOS app is running in the foreground, but isn’t receiving actions from controls or gestures.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Active', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'type': 'text', 'text': 'The watchOS app is running in the foreground and receiving actions from controls and gestures. This is the normal mode for apps running on screen.'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Background', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The system has given the watchOS app a small amount of background execution time.', 'type': 'text'}]}] |
| [{'type': 'paragraph', 'inlineContent': [{'text': 'Suspended', 'type': 'text'}]}] | [{'type': 'paragraph', 'inlineContent': [{'text': 'The app is in memory but isn’t executing code. The system may purge suspended apps at any time to make room for other apps.', 'type': 'text'}]}] |

For more information, see [`Handling Common State Transitions`](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions).

When the system receives background data, it may not immediately wake the watchOS app to process that data. Instead, it may delay delivery of the data to preserve battery life.

If the app is currently running—either active and onscreen, or inactive and the frontmost app—the system immediately delivers the data to the app. If the app is in the background, the system wakes the app within 10 minutes to deliver the data.

## Topics

### Responding to life cycle events
- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))
  Detect and respond to common state transitions.
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))
  Learn how the watchOS app life cycle operates and responds to life cycle notification methods.
- [Handling User Activity](handling-user-activity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-user-activity))
  Detect and respond to user activity information from Handoff or a complication.
- [Taking Advantage of Frontmost App State](taking-advantage-of-frontmost-app-state.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/taking-advantage-of-frontmost-app-state))
  Understand the frontmost app state, and the features it provides to your app.

## See Also

- [Background execution](background-execution.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/background-execution))
- [Using extended runtime sessions](using-extended-runtime-sessions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/using-extended-runtime-sessions))
- [class WKExtendedRuntimeSession](wkextendedruntimesession.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkextendedruntimesession))
- [Interacting with Bluetooth peripherals during background app refresh](interacting-with-bluetooth-peripherals-during-background-app-refresh.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/interacting-with-bluetooth-peripherals-during-background-app-refresh))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/life-cycles)*