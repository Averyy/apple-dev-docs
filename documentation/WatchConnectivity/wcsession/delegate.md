# delegate

**Framework**: Watch Connectivity  
**Kind**: property

The delegate for the session object

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var delegate: (any WCSessionDelegate)? { get set }
```

#### Discussion

You must assign an object conforming to the [`WCSessionDelegate`](wcsessiondelegate.md) protocol to this property before calling the [`activate()`](wcsession/activate().md) method. The delegate is responsible for responding to session-related changes, for processing incoming data, and for responding to errors.

For more information about implementing your delegate object, see [`WCSessionDelegate`](wcsessiondelegate.md).

## See Also

- [func activate()](wcsession/activate.md)
  Activates the session asynchronously.
- [var activationState: WCSessionActivationState](wcsession/activationstate.md)
  The current activation state of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/delegate)*