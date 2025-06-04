# WKApplicationState.background

**Framework**: WatchKit  
**Kind**: case

The Watch app is running in the background.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
case background
```

## Mentions

- [Handling Common State Transitions](handling-common-state-transitions.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/handling-common-state-transitions))
- [Working with the watchOS app life cycle](working-with-the-watchos-app-life-cycle.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/working-with-the-watchos-app-life-cycle))

#### Discussion

The system can wake suspended apps in the background. It can also launch apps that are not running in the background to perform background tasks.

## See Also

- [WKApplicationState.active](active.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/active))
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.inactive](inactive.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkapplicationstate/inactive))
  The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background)*