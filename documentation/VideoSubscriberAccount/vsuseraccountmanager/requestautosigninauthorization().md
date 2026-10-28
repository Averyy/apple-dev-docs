# requestAutoSignInAuthorization()

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Presents a modal sheet that offers a person to opt in to Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```swift
func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext
```

## Mentions

- [Signing people in to their media accounts automatically](../signing-people-in-to-media-apps-automatically.md)

## Discussion

Call this method after a successful sign in to your streaming service. You might also call this method through custom UI that your app implements to offer Automatic Sign-In.

If the person approves the prompt, the framework sets the [`authorization`](./autosignintokenupdatecontext/authorization.md) status to [`VSUserAccountManager.AutoSignInAuthorization.granted`](./autosigninauthorization/granted.md). If the person dismisses the prompt without approving, the system leaves the authorization status [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](./autosigninauthorization/notdetermined.md) and the framework doesn’t prompt them again until the app calls [`requestAutoSignInAuthorization()`](./requestautosigninauthorization%28%29.md) once more.

> ❗ **Important**: Avoid calling this method when the person might not expect a prompt, for example, while they’re viewing streaming media.

For more information, see [Signing people in to their media accounts automatically](../signing-people-in-to-media-apps-automatically.md).

## See Also

### Signing people in automatically
- [VSUserAccountManager.AutoSignInToken](./autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](./autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](./autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](./autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func deleteAutoSignInToken() async throws](./deleteautosignintoken%28%29.md)
  Deletes the value of the current Automatic Sign-In token.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](./updateautosignintoken%28_,updatecontext%29.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/requestautosigninauthorization())*