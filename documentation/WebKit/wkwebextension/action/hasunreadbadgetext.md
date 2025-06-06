# hasUnreadBadgeText

**Framework**: Webkit  
**Kind**: property

A Boolean value indicating whether the badge text is unread.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
var hasUnreadBadgeText: Bool { get set }
```

#### Discussion

This property is automatically set to `YES` when [`badgeText`](wkwebextension/action/badgetext.md) changes and is not empty. If [`badgeText`](wkwebextension/action/badgetext.md) becomes empty or the popup associated with the action is presented, this property is automatically set to `NO`. Additionally, it should be set to `NO` by the app when the badge has been presented to the user. This property is useful for higher-level notification badges when extensions might be hidden behind an action sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/wkwebextension/action/hasunreadbadgetext)*