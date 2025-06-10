# decidePolicy(for:preferences:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Determines permission to navigate to new content based on the specified preferences and action information.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

## Declaration

```swift
@MainActor
mutating func decidePolicy(for action: WebPage.NavigationAction, preferences: inout WebPage.NavigationPreferences) async -> WKNavigationActionPolicy
```

#### Return Value

The navigation policy for the action.

#### Discussion

The web page calls this method after the interaction occurs but before it attempts to load any content.

## Parameters

- `action`: Details about the action that triggered the navigation request.
- `preferences`: The preferences to use when displaying the new webpage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decidepolicy(for:preferences:))*