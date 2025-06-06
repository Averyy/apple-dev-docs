# sessionReachabilityDidChange(_:)

**Framework**: Watchconnectivity  
**Kind**: method

Indicates a change to the counterpart’s reachability status.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func sessionReachabilityDidChange(_ session: WCSession)
```

#### Discussion

A session is reachable when the iOS app or WatchKit extension to which it belongs is active and running. This method is called to let the current process know that its counterpart session’s reachability changed. Use that information to make decisions about how you want to send information to the counterpart. For example, when the counterpart is reachable, you might send messages immediately rather than post them as an update.

## Parameters

- `session`: The session object of the current process. Use the   property of this object to determine the reachability of the counterpart session.

## See Also

- [func sessionWatchStateDidChange(WCSession)](wcsessiondelegate/sessionwatchstatedidchange(_:).md)
  Indicates a change to the counterpart’s information.
- [func sessionCompanionAppInstalledDidChange(WCSession)](wcsessiondelegate/sessioncompanionappinstalleddidchange(_:).md)
  Indicates a change to the companion app’s installed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/sessionreachabilitydidchange(_:))*