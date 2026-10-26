# decidePolicy(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

By default, this method immediately returns with a policy of `.allow`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func decidePolicy(for response: WebPage.NavigationResponse) async -> WKNavigationResponsePolicy
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decidepolicy(for:)-6v2aq)*