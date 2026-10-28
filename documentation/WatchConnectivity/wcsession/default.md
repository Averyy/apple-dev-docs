# default

**Framework**: Watch Connectivity  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, readonly) WCSession * defaultSession;
```

## Return Value

The session object for the current device.

## Discussion

Call the [`isSupported()`](./issupported%28%29.md) method before calling this method to make sure you can use session objects for communication.

## See Also

### Getting the Default Session
- [class func isSupported() -> Bool](./issupported%28%29.md)
  Returns a Boolean value indicating whether the current iOS device is able to use a session object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchconnectivity/wcsession/default)*