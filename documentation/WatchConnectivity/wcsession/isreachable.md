# isReachable

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isReachable) BOOL reachable;
```

#### Discussion

This property is [`true`](../../Swift/true.md) when the WatchKit extension and the iOS app can communicate with each other.

Specifically: 

- **WatchKit extension.** The iOS device is within range, so communication can occur and the WatchKit extension is running in the foreground, or is running with a high priority in the background (for example, during a workout session or when a complication is loading its initial timeline data).
- **iOS app.** A paired and active Apple Watch is in range, the corresponding WatchKit extension is running, and the WatchKit extension’s [`isReachable`](./isreachable.md) property is [`true`](../../Swift/true.md).

In all other cases, the value is [`false`](../../Swift/false.md).

The counterpart must be reachable in order for you to send messages using the [`sendMessage(_:replyHandler:errorHandler:)`](./sendmessage%28_,replyhandler,errorhandler%29.md) and [`sendMessageData(_:replyHandler:errorHandler:)`](./sendmessagedata%28_,replyhandler,errorhandler%29.md) methods. Sending messages to a counterpart that is not reachable results in an error.

The value in this property is valid only for a configured session that has been activated successfully. If the [`activationState`](./activationstate.md) property is available, its value must be [`WCSessionActivationState.activated`](../wcsessionactivationstate/activated.md). When the session becomes inactive or deactivated, you should ignore the value in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/isreachable)*