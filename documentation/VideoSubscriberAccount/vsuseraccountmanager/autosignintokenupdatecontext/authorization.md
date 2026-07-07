# authorization

**Framework**: Video Subscriber Account  
**Kind**: property

A state that represents a person’s approval of Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```swift
var authorization: VSUserAccountManager.AutoSignInAuthorization { get }
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

The system prompts the person to opt in to Automatic Sign-In when the app calls   [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md). If the person approves the prompt, the framework sets the [`authorization`](vsuseraccountmanager/autosignintokenupdatecontext/authorization.md) status to [`VSUserAccountManager.AutoSignInAuthorization.granted`](vsuseraccountmanager/autosigninauthorization/granted.md). If the person dismisses the prompt without approving, the system leaves the authorization status [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md) and the framework doesn’t prompt them again until the app calls [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) once more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintokenupdatecontext/authorization)*