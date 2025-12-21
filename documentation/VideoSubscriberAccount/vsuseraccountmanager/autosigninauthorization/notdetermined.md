# VSUserAccountManager.AutoSignInAuthorization.notDetermined

**Framework**: Video Subscriber Account  
**Kind**: case

A state that indicates the framework needs to reauthorize Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case notDetermined
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

This authorization state indicates that either a person hasn’t answered the prompt to opt in to Automatic Sign-In, or that the app (or server) deletes the token value.

When [`authorization`](vsuseraccountmanager/autosignintoken-swift.struct/authorization.md) for the current Automatic Sign-In token is this state, the app needs to call [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) again before creating a token value for the account.

For more information, see [`Signing people in to their media accounts automatically`](signing-people-in-to-media-apps-automatically.md).

## See Also

- [VSUserAccountManager.AutoSignInAuthorization.granted](vsuseraccountmanager/autosigninauthorization/granted.md)
  A state that indicates the person opts in to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInAuthorization.denied](vsuseraccountmanager/autosigninauthorization/denied.md)
  A state that indicates denied authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosigninauthorization/notdetermined)*