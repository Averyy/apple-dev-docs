# performBatchUpdates(_:)

**Framework**: UIKit  
**Kind**: method

Animates multiple tab changes as a single update.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func performBatchUpdates(_ updates: () -> Void)
```

#### Discussion

Use this method when you need to make several changes to tab properties simultaneously. Changes made inside the `updates` block are coalesced into a single animated layout pass, preventing intermediate states from being visible to the user.

The `updates` block is called synchronously. You can safely read and write any mutable tab properties inside this block.

## See Also

- [var tabs: [UITab]](uitabbarcontroller/tabs.md)
  An array of tabs that the tab bar displays.
- [func setTabs([UITab], animated: Bool)](uitabbarcontroller/settabs(_:animated:).md)
  Sets the root tabs of the tab bar controller, with an option to animate the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitabbarcontroller/performbatchupdates(_:))*