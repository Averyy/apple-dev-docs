# autoSignInToken

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

The current Automatic Sign-In token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var autoSignInToken: VSUserAccountManager.AutoSignInToken { get async throws }
```

## Mentions

- [Signing people in to their media accounts automatically](../signing-people-in-to-media-apps-automatically.md)

## Discussion

The framework sets this property to the current Automatic Sign-In token value and authorization status according to information on the person’s Account Account.

For more information, see [Signing people in to their media accounts automatically](../signing-people-in-to-media-apps-automatically.md).

## See Also

### Signing people in automatically
- [VSUserAccountManager.AutoSignInToken](./autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](./autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](./autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [func deleteAutoSignInToken() async throws](./deleteautosignintoken%28%29.md)
  Deletes the value of the current Automatic Sign-In token.
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](./requestautosigninauthorization%28%29.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](./updateautosignintoken%28_,updatecontext%29.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosignintoken-swift.property)*