# activationState

**Framework**: Watch Connectivity  
**Kind**: property

The current activation state of the session.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.2+

## Declaration

```swift
var activationState: WCSessionActivationState { get }
```

#### Discussion

Check the value of this property before attempting to transfer data or files using the methods of this object. When the value is [`WCSessionActivationState.activated`](wcsessionactivationstate/activated.md) you may initiate the transfer of data and files normally. If it is any other value, do not initiate any transfers.

The value of this property is valid even when the session itself is not activated, so you can access it at any time. Use the  [`sessionDidBecomeInactive(_:)`](wcsessiondelegate/sessiondidbecomeinactive(_:).md) and [`sessionDidDeactivate(_:)`](wcsessiondelegate/sessiondiddeactivate(_:).md) methods of your session delegate to monitor changes in the session’s activation state. You can also use key-value observing to monitor changes to this property.

## See Also

- [var delegate: (any WCSessionDelegate)?](wcsession/delegate.md)
  The delegate for the session object
- [func activate()](wcsession/activate.md)
  Activates the session asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/activationstate)*