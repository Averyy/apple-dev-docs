# VSUserAccountManager.AutoSignInTokenUpdateContext

**Framework**: Video Subscriber Account  
**Kind**: struct

An object that contains information about a person’s choice in the Automatic Sign-In prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```swift
struct AutoSignInTokenUpdateContext
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Overview

The framework returns an instance of this structure when your app calls [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md) to prompt a person for approval to opt in to Automatic Sign-In.

Check the [`authorization`](vsautosignintokenupdatecontext/authorization.md) property of this structure to determine the person’s answer to the prompt. If the value is [`VSUserAccountManager.AutoSignInAuthorization.granted`](vsuseraccountmanager/autosigninauthorization/granted.md), generate a sign in token and pass the instance of this structure and the newly-generated token to the framework using the [`updateAutoSignInToken(_:updateContext:)`](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md) method.

## Topics

### Determining status
- [var authorization: VSUserAccountManager.AutoSignInAuthorization](vsuseraccountmanager/autosignintokenupdatecontext/authorization.md)
  A state that represents a person’s approval of Automatic Sign-In.

## See Also

- [VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintokenupdatecontext)*