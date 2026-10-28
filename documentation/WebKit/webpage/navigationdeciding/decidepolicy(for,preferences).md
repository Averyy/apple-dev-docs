# decidePolicy(for:preferences:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines permission to navigate to new content based on the specified preferences and action information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
mutating func decidePolicy(for action: WebPage.NavigationAction, preferences: inout WebPage.NavigationPreferences) async -> WKNavigationActionPolicy
```

## Return Value

The navigation policy for the action.

## Discussion

The web page calls this method after the interaction occurs but before it attempts to load any content.

## Parameters

- `action`: Details about the action that triggered the navigation request.
- `preferences`: The preferences to use when displaying the new webpage.

## Default Implementations

### WebPage.NavigationDeciding Implementations
- [func decidePolicy(for: WebPage.NavigationAction, preferences: inout WebPage.NavigationPreferences) async -> WKNavigationActionPolicy](./decidepolicy%28for,preferences%29-3lqmr.md)
  By default, this method immediately returns with a policy of `.allow`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decidepolicy(for:preferences:))*