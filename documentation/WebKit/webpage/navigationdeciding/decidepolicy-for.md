# decidePolicy(for:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Determines permission to navigate to new content after the response to the navigation request is known.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

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