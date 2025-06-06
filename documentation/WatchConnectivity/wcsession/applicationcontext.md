# applicationContext

**Framework**: Watchconnectivity  
**Kind**: property

The most recent contextual data sent to the paired and active device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var applicationContext: [String : Any] { get }
```

#### Discussion

After calling the [`updateApplicationContext(_:)`](wcsession/updateapplicationcontext(_:).md) method, the session object places a copy of your dictionary in this property so that you can determine what data you last sent to the counterpart.

## See Also

- [func updateApplicationContext([String : Any]) throws](wcsession/updateapplicationcontext(_:).md)
  Sends a dictionary of values that a paired and active device can use to synchronize its state.
- [var receivedApplicationContext: [String : Any]](wcsession/receivedapplicationcontext.md)
  A dictionary containing the last update data received from a paired and active device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/applicationcontext)*