# allowsFullScreen

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the scene can appear full screen.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 16.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsFullScreen: Bool { get set }
```

#### Discussion

The system only checks the value of this property in Mac Catalyst apps.

## See Also

- [var minimumSize: CGSize](uiscenesizerestrictions/minimumsize.md)
  The minimum width and height supported by your app’s windows.
- [var maximumSize: CGSize](uiscenesizerestrictions/maximumsize.md)
  The maximum width and height supported by your app’s windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscenesizerestrictions/allowsfullscreen)*