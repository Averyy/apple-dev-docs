# sessionCompanionAppInstalledDidChange(_:)

**Framework**: Watchconnectivity  
**Kind**: method

Indicates a change to the companion app’s installed state.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
optional func sessionCompanionAppInstalledDidChange(_ session: WCSession)
```

#### Discussion

The system calls this method on the watchOS app’s session delegate when the user installs or uninstalls the iOS companion app. This is only valid on independent watchOS apps.

## Parameters

- `session`: The session object with the changed companion app.

## See Also

- [func sessionWatchStateDidChange(WCSession)](wcsessiondelegate/sessionwatchstatedidchange(_:).md)
  Indicates a change to the counterpart’s information.
- [func sessionReachabilityDidChange(WCSession)](wcsessiondelegate/sessionreachabilitydidchange(_:).md)
  Indicates a change to the counterpart’s reachability status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/sessioncompanionappinstalleddidchange(_:))*