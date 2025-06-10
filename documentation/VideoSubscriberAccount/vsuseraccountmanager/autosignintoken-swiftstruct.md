# VSUserAccountManager.AutoSignInToken

**Framework**: Video Subscriber Account  
**Kind**: struct

A value that represents a person’s account and their consent to Automatic Sign-In.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct AutoSignInToken
```

#### Overview

Automatic Sign-In tokens implement a single sign-on experience for media streaming services for a signed-in Apple Account.

The framework sets [`autoSignInToken`](vsuseraccountmanager/autosignintoken-swift.property.md) to an instance of this structure. The source of the information inside depends on whether the person approves the prompt to opt in to Automatic Sign-In. For more information, see [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md).

Alternatively, if you delete the token value by calling [`deleteAutoSignInToken()`](vsuseraccountmanager/deleteautosignintoken().md), the framework sets [`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md) to `nil` and [`authorization`](vsuseraccountmanager/autosignintoken-swift.struct/authorization.md) to [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](vsuseraccountmanager/autosigninauthorization/notdetermined.md).

> ❗ **Important**: Only use an Automatic Sign-In token to turn on media streaming. For example, avoid using the token itself as a gate that lets the person manage their account.

For more information about Automatic Sign-In tokens, see [`Signing people in to their media accounts automatically`](signing-people-in-to-media-apps-automatically.md).

## Topics

### Defining the token value
- [var value: String?](vsuseraccountmanager/autosignintoken-swift.struct/value.md)
  A string that represents a person’s account.
### Determining status
- [var authorization: VSUserAccountManager.AutoSignInAuthorization](vsuseraccountmanager/autosignintoken-swift.struct/authorization.md)
  A state that represents a person’s approval of Automatic Sign-In.

## See Also

- [VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](vsuseraccountmanager/autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func deleteAutoSignInToken() async throws](vsuseraccountmanager/deleteautosignintoken.md)
  Deletes the value of the current Automatic Sign-In token.
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/requestautosigninauthorization.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintoken-swift.struct)*