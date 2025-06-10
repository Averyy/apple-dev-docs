# systemFrame

**Framework**: UIKit  
**Kind**: property

The preferred frame of the scene, in system coordinates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS ?+

## Declaration

```swift
var systemFrame: CGRect? { get set }
```

#### Discussion

This property represents the preferred frame of the scene in the system coordinate space, where an origin of `(0, 0)` corresponds to the top-left corner of the main display. The default value is [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull), which indicates no preferred frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiwindowscene/geometrypreferences/mac/systemframe)*