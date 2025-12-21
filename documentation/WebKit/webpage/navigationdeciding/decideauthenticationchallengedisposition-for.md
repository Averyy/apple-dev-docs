# decideAuthenticationChallengeDisposition(for:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Determines the response to an authentication challenge.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
mutating func decideAuthenticationChallengeDisposition(for challenge: URLAuthenticationChallenge) async -> (URLSession.AuthChallengeDisposition, URLCredential?)
```

#### Return Value

The option to use to handle the challenge, and the credential to use for authentication when the disposition is `URLSession/AuthChallengeDisposition/useCredential`.

## Parameters

- `challenge`: The authentication challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/webpage/navigationdeciding/decideauthenticationchallengedisposition(for:))*