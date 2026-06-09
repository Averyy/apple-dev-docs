# isCollapsedByDefault

**Framework**: UIKit  
**Kind**: property

Whether the group is initially displayed in a collapsed state in the sidebar.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst 26.1+
- visionOS 26.1+

## Declaration

```swift
var isCollapsedByDefault: Bool { get set }
```

#### Discussion

When true, the group renders collapsed the first time it appears in the sidebar. The user can expand the group manually, and any subsequent user interactions or customization changes take precedence over this default.

This property has no effect in contexts where groups are not collapsible, such as when `sidebarAppearance == .inline`.

Default is `NO`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabgroup/iscollapsedbydefault)*