# debugDescription

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

A textual description of the location suitable for debugging.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Xcode 16.3+

## Declaration

```swift
var debugDescription: String { get }
```

```objc
@property (copy, readonly) NSString * debugDescription;
```

## Discussion

Use this property to access debugging information about this object and the underlying [`CLLocation`](../../CoreLocation/cllocation.md) this object wraps.

## See Also

### Determining the location
- [var location: CLLocation](./location.md)
  Returns the object that contains the latitude, longitude, and course information this proxy simulates for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuilocation/debugdescription)*