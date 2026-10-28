# isSupported()

**Framework**: Watch Connectivity  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value indicating whether the current iOS device is able to use a session object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func isSupported() -> Bool
```

```objc
+ (BOOL) isSupported;
```

## Return Value

[`true`](../../Swift/true.md) if a session object is available or [`false`](../../Swift/false.md) if it is not.

## Discussion

Before retrieving the default session object, call this method to verify that the current device supports watch connectivity. Session objects are always available on Apple Watch. They are also available on iPhones that support pairing with an Apple Watch. For all other devices, this method returns [`false`](../../Swift/false.md) to indicate that you cannot use the classes and methods of this framework.

## See Also

### Getting the Default Session
- [class var `default`: WCSession](./default.md)
  Returns the singleton session object for the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/issupported())*