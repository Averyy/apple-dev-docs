# authorization

**Framework**: Video Subscriber Account  
**Kind**: property

A state that represents a person’s approval of Automatic Sign-In.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var authorization: VSUserAccountManager.AutoSignInAuthorization { get }
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

The default value is [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md). The framework updates the value based on a person’s answer to the prompt to opt in to Automatic Sign-In (see [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintoken-swift.struct/authorization)*