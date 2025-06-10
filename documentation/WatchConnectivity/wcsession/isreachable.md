# isReachable

**Framework**: Watch Connectivity  
**Kind**: property

A Boolean value indicating whether the counterpart app is available for live messaging.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isReachable: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/swift/true) when the WatchKit extension and the iOS app can communicate with each other.

Specifically: 

-  The iOS device is within range, so communication can occur and the WatchKit extension is running in the foreground, or is running with a high priority in the background (for example, during a workout session or when a complication is loading its initial timeline data).
-  A paired and active Apple Watch is in range, the corresponding WatchKit extension is running, and the WatchKit extension’s [`isReachable`](wcsession/isreachable.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

In all other cases, the value is [`false`](https://developer.apple.com/documentation/swift/false).

The counterpart must be reachable in order for you to send messages using the [`sendMessage(_:replyHandler:errorHandler:)`](wcsession/sendmessage(_:replyhandler:errorhandler:).md) and [`sendMessageData(_:replyHandler:errorHandler:)`](wcsession/sendmessagedata(_:replyhandler:errorhandler:).md) methods. Sending messages to a counterpart that is not reachable results in an error.

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](wcsession/activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/isreachable)*