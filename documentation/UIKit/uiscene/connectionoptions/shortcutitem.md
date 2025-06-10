# shortcutItem

**Framework**: UIKit  
**Kind**: property

The user-selected action to perform.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var shortcutItem: UIApplicationShortcutItem? { get }
```

#### Discussion

If the user selected one of your app’s quick actions, this property contains the selected action. You use quick actions to provide access to frequently used features of your app, and the user accesses those actions through interactions with your app’s icon in the Home Screen. If the user didn’t select a quick action, this property is `nil`.

For an example of how to set up quick actions for your app, see [`Add Home Screen quick actions`](add-home-screen-quick-actions.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/shortcutitem)*