# requestAutoSignInAuthorization()

**Framework**: Video Subscriber Account  
**Kind**: method

Presents a modal sheet that offers a person to opt in to Automatic Sign-In.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

Call this method after a successful sign in to your streaming service. You might also call this method through custom UI that your app implements to offer Automatic Sign-In.

If the person approves the prompt, the framework sets the [`authorization`](vsuseraccountmanager/autosignintokenupdatecontext/authorization.md) status to [`VSUserAccountManager.AutoSignInAuthorization.granted`](vsuseraccountmanager/autosigninauthorization/granted.md). If the person dismisses the prompt without approving, the system leaves the authorization status [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md) and the framework doesn’t prompt them again until the app calls [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) once more.

> ❗ **Important**: Avoid calling this method when the person might not expect a prompt, for example, while they’re viewing streaming media.

For more information, see [`Signing people in to their media accounts automatically`](signing-people-in-to-media-apps-automatically.md).

## See Also

- [VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](vsuseraccountmanager/autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func deleteAutoSignInToken() async throws](vsuseraccountmanager/deleteautosignintoken.md)
  Deletes the value of the current Automatic Sign-In token.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/requestautosigninauthorization())*