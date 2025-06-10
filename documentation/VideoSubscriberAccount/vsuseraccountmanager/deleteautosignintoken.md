# deleteAutoSignInToken()

**Framework**: Video Subscriber Account  
**Kind**: method

Deletes the value of the current Automatic Sign-In token.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func deleteAutoSignInToken() async throws
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

This method sets the contents of [`value`](vsuseraccountmanager/autosignintoken-swift.struct/value.md) to `nil` for the current [`autoSignInToken`](vsuseraccountmanager/autosignintoken-swift.property.md).

You might delete an Automatic Sign-In token, for example, if:

- Your app provides its own UI that lets the person opt out of Automatic Sign-In.
- The person changes their password and wants to sign out from all of their devices.
- Your app implements conditions to invalidate a token, such as if a person flags a specific log in as unauthorized.

## See Also

- [VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](vsuseraccountmanager/autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](vsuseraccountmanager/autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/requestautosigninauthorization.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/deleteautosignintoken())*