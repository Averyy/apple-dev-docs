# sourceView

**Framework**: UIKit  
**Kind**: property

The view that the sheet centers itself over.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sourceView: UIView? { get set }
```

#### Discussion

The default value is `nil`, which means the system centers edge-attached sheets on the edge they attach to, and centers floating sheets vertically and horizontally in the window.

To customize the sheet’s position, set a view within the view hierarchy of the presenting view controller as the [`sourceView`](uisheetpresentationcontroller/sourceview.md) of the sheet. The sheet attempts to visually center itself over this view. The system only positions the sheet within system-defined margins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/sourceview)*