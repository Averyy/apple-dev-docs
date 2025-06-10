# sizeRestrictions

**Framework**: UIKit  
**Kind**: property

The minimum and maximum size of the app’s windows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sizeRestrictions: UISceneSizeRestrictions? { get }
```

#### Discussion

When the value of this property is not `nil`, use it to change the default minimum and maximum window sizes for your app. If the value of this property is `nil,` the system doesn’t allow you to set window size restrictions.

## See Also

- [var traitCollection: UITraitCollection](uiwindowscene/traitcollection.md)
  The traits that describe the current environment of the scene.
- [class UISceneSizeRestrictions](uiscenesizerestrictions.md)
  An object that specifies the minimum and maximum sizes for resizable windows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/sizerestrictions)*