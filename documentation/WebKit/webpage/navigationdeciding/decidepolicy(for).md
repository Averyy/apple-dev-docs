# decidePolicy(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines permission to navigate to new content after the response to the navigation request is known.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
mutating func decidePolicy(for response: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy
```

## Return Value

The navigation policy for the response.

## Parameters

- `response`: Descriptive information about the navigation response.

## Default Implementations

### WebPage.NavigationDeciding Implementations
- [func decidePolicy(for: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy](./decidepolicy%28for%29-6v2aq.md)
  By default, this method immediately returns with a policy of `.allow`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decidepolicy(for:))*