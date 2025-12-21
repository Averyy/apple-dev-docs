# isSidebarDestination

**Framework**: UIKit  
**Kind**: property

Determines if the tab group itself can be selected as a destination in the sidebar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
var isSidebarDestination: Bool { get set }
```

#### Discussion

By default, tab groups are not destinations when displayed in the sidebar, and cannot be selected directly by users. When enabled, the tab group becomes a selectable item in the sidebar, and will no longer perform automatic selection for a default child if no child is currently selected. The default value is NO.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/issidebardestination)*