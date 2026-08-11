# isAvailable

**Framework**: UIKit  
**Kind**: property

Whether the associated scene accessory is available for display by the system or not.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var isAvailable: Bool { get }
```

## Mentions

- [Presenting content on a connected display](presenting-content-on-a-connected-display.md)

#### Discussion

This value is observable during the `updateProperties` and `layoutSubviews` lifecycle events.

## See Also

- [var isEnabled: Bool](uisceneaccessoryregistration/isenabled.md)
  Whether the content defined by this scene accessory should be displayed or not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration/isavailable)*