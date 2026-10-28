# WKApplicationState.background

**Framework**: WatchKit  
**Kind**: case  
**Role**: Case

The Watch app is running in the background.

**Availability**:
- watchOS 3.0+

## Declaration

```swift
case background
```

```c
WKApplicationStateBackground
```

## Mentions

- [Handling Common State Transitions](../handling-common-state-transitions.md)
- [Working with the watchOS app life cycle](../working-with-the-watchos-app-life-cycle.md)

## Discussion

The system can wake suspended apps in the background. It can also launch apps that are not running in the background to perform background tasks.

## See Also

### Constants
- [WKApplicationState.active](./active.md)
  The Watch app is running in the foreground and currently receiving events.
- [WKApplicationState.inactive](./inactive.md)
  The Watch app is running in the foreground, but is not yet responding to actions from controls or gestures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/wkapplicationstate/background)*