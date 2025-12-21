# decidePolicy(for:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Determines permission to navigate to new content after the response to the navigation request is known.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
mutating func decidePolicy(for response: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy
```

#### Return Value

The navigation policy for the response.

## Parameters

- `response`: Descriptive information about the navigation response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decidepolicy(for:))*