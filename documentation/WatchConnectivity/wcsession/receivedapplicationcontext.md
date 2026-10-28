# receivedApplicationContext

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSDictionary<NSString *,id> * receivedApplicationContext;
```

## Discussion

Use this method to access the most recently received update dictionary. The session object also sends a newly arrived dictionary to the [`session(_:didReceiveApplicationContext:)`](../wcsessiondelegate/session%28_,didreceiveapplicationcontext%29.md) method of its delegate.

## See Also

### Managing Background Updates
- [func updateApplicationContext([String : Any]) throws](./updateapplicationcontext%28_%29.md)
  Sends a dictionary of values that a paired and active device can use to synchronize its state.
- [var applicationContext: [String : Any]](./applicationcontext.md)
  The most recent contextual data sent to the paired and active device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/receivedapplicationcontext)*