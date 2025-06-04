# WKApplicationState.inactive

**Framework**: Watchkit  
**Kind**: case

The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
case inactive
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))

## Overview

Typically, apps transition quickly through the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state when becoming active or going to the background. A newly launched watchOS app starts in the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state and then quickly transitions to the [`WKApplicationState.active`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active) state.

An active app also transition to this state when the user dismisses the app or stops interacting with it. The app remains in the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state as long as it is the frontmost app (see `Understand Frontmost App State`). Then the system transitions the app to the [`WKApplicationState.background`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background) state before suspending it.

In some situations, the app may run for extended periods in the inactive state. For example, this occurs when the app is running in the dock, or when it is the frontmost app.

When the user scrolls to the app in the dock, the system initially displays the app’s most recent snapshot. Then the app transitions to the foreground, but remains in the [`WKApplicationState.inactive`](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive) state. The system displays a running preview of the app in the dock, but the app doesn’t respond to actions or gestures.

## See Also

- [WKApplicationState.active](active.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active))
- [WKApplicationState.background](background.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive)*