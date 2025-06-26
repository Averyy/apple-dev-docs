# WKApplicationState.inactive

**Framework**: WatchKit  
**Kind**: case

The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
case inactive
```

## Mentions

- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md)
- [Handling Common State Transitions](handling-common-state-transitions.md)

#### Discussion

Typically, apps transition quickly through the [`WKApplicationState.inactive`](wkapplicationstate/inactive.md) state when becoming active or going to the background. A newly launched watchOS app starts in the [`WKApplicationState.inactive`](wkapplicationstate/inactive.md) state and then quickly transitions to the [`WKApplicationState.active`](wkapplicationstate/active.md) state.

An active app also transition to this state when the user dismisses the app or stops interacting with it. The app remains in the [`WKApplicationState.inactive`](wkapplicationstate/inactive.md) state as long as it is the frontmost app (see `Understand Frontmost App State`). Then the system transitions the app to the [`WKApplicationState.background`](wkapplicationstate/background.md) state before suspending it.

In some situations, the app may run for extended periods in the inactive state. For example, this occurs when the app is running in the dock, or when it is the frontmost app.

When the user scrolls to the app in the dock, the system initially displays the app’s most recent snapshot. Then the app transitions to the foreground, but remains in the [`WKApplicationState.inactive`](wkapplicationstate/inactive.md) state. The system displays a running preview of the app in the dock, but the app doesn’t respond to actions or gestures.

## See Also

- [WKApplicationState.active](wkapplicationstate/active.md)
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.background](wkapplicationstate/background.md)
  The Watch app is running in the background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive)*