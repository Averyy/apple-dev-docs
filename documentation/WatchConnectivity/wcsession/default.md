# default

**Framework**: Watch Connectivity  
**Kind**: property

Returns the singleton session object for the current device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var `default`: WCSession { get }
```

#### Return Value

The session object for the current device.

#### Discussion

Call the [`isSupported()`](wcsession/issupported().md) method before calling this method to make sure you can use session objects for communication.

## See Also

- [class func isSupported() -> Bool](wcsession/issupported.md)
  Returns a Boolean value indicating whether the current iOS device is able to use a session object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/default)*