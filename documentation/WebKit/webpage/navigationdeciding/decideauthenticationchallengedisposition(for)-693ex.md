# decideAuthenticationChallengeDisposition(for:)

**Framework**: WebKit  
**Kind**: method  
**Role**: Instance Method

By default, this method immediately returns with a disposition of `performDefaultHandling` and a `nil` credential.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
func decideAuthenticationChallengeDisposition(for challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decideauthenticationchallengedisposition(for:)-693ex)*