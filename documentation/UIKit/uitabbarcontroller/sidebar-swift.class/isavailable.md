# isAvailable

**Framework**: UIKit  
**Kind**: property

Indicates when the tab sidebar is available to be displayed in the current context. When available, the sidebar is either visible, or can become visible depending on `isHidden`. Use this property to gate behaviors or UI that is dependent on the availability of the sidebar (like child tabs, or landing pages for groups).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var isAvailable: Bool { get }
```

#### Discussion

Implement the delegate method `tabBarController:sidebarAvailabilityDidChange:` to be notified when the value of this property changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/sidebar-swift.class/isavailable)*