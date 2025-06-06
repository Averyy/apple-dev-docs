# receivedApplicationContext

**Framework**: Watchconnectivity  
**Kind**: property

A dictionary containing the last update data received from a paired and active device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var receivedApplicationContext: [String : Any] { get }
```

#### Discussion

Use this method to access the most recently received update dictionary. The session object also sends a newly arrived dictionary to the [`session(_:didReceiveApplicationContext:)`](wcsessiondelegate/session(_:didreceiveapplicationcontext:).md) method of its delegate.

## See Also

- [func updateApplicationContext([String : Any]) throws](wcsession/updateapplicationcontext(_:).md)
  Sends a dictionary of values that a paired and active device can use to synchronize its state.
- [var applicationContext: [String : Any]](wcsession/applicationcontext.md)
  The most recent contextual data sent to the paired and active device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/receivedapplicationcontext)*