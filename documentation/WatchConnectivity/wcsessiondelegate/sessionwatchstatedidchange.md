# sessionWatchStateDidChange(_:)

**Framework**: Watch Connectivity  
**Kind**: method

Indicates a change to the counterpart’s information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func sessionWatchStateDidChange(_ session: WCSession)
```

#### Discussion

The session object calls this method when the value in the [`isPaired`](wcsession/ispaired.md), [`isWatchAppInstalled`](wcsession/iswatchappinstalled.md), [`isComplicationEnabled`](wcsession/iscomplicationenabled.md), or [`watchDirectoryURL`](wcsession/watchdirectoryurl.md) properties of the [`WCSession`](wcsession.md) object changes. Use this state to update the state of your iOS app. For example, when the complication is disabled, make a note of that fact and do not send any more data updates for the complication.

## Parameters

- `session`: The session object whose state changed.

## See Also

- [func sessionReachabilityDidChange(WCSession)](wcsessiondelegate/sessionreachabilitydidchange(_:).md)
  Indicates a change to the counterpart’s reachability status.
- [func sessionCompanionAppInstalledDidChange(WCSession)](wcsessiondelegate/sessioncompanionappinstalleddidchange(_:).md)
  Indicates a change to the companion app’s installed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsessiondelegate/sessionwatchstatedidchange(_:))*