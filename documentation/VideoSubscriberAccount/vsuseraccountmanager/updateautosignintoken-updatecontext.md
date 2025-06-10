# updateAutoSignInToken(_:updateContext:)

**Framework**: Video Subscriber Account  
**Kind**: method

Sets the current Automatic Sign-In token.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)

## Declaration

```swift
func updateAutoSignInToken(_ newToken: String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws
```

## Mentions

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)

#### Discussion

Call this method when generating a new token value for an account. To update the token, request the person’s authorization for Automatic Sign-In. For more information, see [`requestAutoSignInAuthorization()`](vsuseraccountmanager/requestautosigninauthorization().md).

## Parameters

- `newToken`: The new token value to store in the person’s Apple Account. Your app determines the contents of this string using a mechanism you determine fitting to identify the account. In addition, ensure its value is of sufficient length, complexity, and security. For more information on setting this property, see  .
- `updateContext`: The object the framework provides that reflects the person’s choice in the authorization prompt; pass the result of the   method.

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
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](vsuseraccountmanager/requestautosigninauthorization.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/updateautosignintoken(_:updatecontext:))*