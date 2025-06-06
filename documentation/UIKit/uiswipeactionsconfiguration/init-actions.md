# init(actions:)

**Framework**: UIKit  
**Kind**: init

Creates a swipe action configuration object with the specified set of actions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(actions: [UIContextualAction])
```

#### Return Value

A newly initialized swipe action configuration object.

## Parameters

- `actions`: The swipe actions to display. The first item in the array represents the outermost action. For example, when the user swipes from right-to-left, the first action is rightmost. The first action is also the default action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiswipeactionsconfiguration/init(actions:))*