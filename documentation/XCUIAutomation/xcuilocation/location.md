# location

**Framework**: XCUIAutomation  
**Kind**: property  
**Role**: Instance Property

Returns the object that contains the latitude, longitude, and course information this proxy simulates for the device.

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
@NSCopying
var location: CLLocation { get }
```

```objc
@property (copy, readonly) CLLocation * location;
```

#### Discussion

Use this property to access the underlying [`CLLocation`](../../CoreLocation/cllocation.md) this object wraps.

## See Also

### Determining the location
- [var debugDescription: String](./debugdescription.md)
  A textual description of the location suitable for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuilocation/location)*