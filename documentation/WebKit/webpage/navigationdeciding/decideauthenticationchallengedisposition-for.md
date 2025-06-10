# decideAuthenticationChallengeDisposition(for:)

**Framework**: WebKit  
**Kind**: method  
**Required**: Yes

Determines the response to an authentication challenge.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst ?+
- macOS 15.4+
- visionOS 2.4+

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