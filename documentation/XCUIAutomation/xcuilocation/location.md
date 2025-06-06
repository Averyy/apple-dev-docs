# location

**Framework**: Xcuiautomation  
**Kind**: property

Returns the object that contains the latitude, longitude, and course information this proxy simulates for the device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Xcode 16.3+

## Declaration

```swift
@NSCopying
@MainActor var location: CLLocation { get }
```

#### Discussion

Use this property to access the underlying [`CLLocation`](https://developer.apple.com/documentation/CoreLocation/CLLocation) this object wraps.

## See Also

- [var debugDescription: String](xcuilocation/debugdescription.md)
  A textual description of the location suitable for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcuiautomation/xcuilocation/location)*