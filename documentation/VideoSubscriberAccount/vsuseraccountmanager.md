# VSUserAccountManager

**Framework**: Video Subscriber Account  
**Kind**: class

The object that coordinates your app’s user account actions.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
class VSUserAccountManager
```

#### Overview

Don’t create `VSUserAccountManager` directly; use [`shared`](vsuseraccountmanager/shared.md).

## Topics

### Getting the account manager
- [class var shared: VSUserAccountManager](vsuseraccountmanager/shared.md)
  A shared instance of the user account manager class.
### Getting user accounts
- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](vsuseraccountmanager/useraccounts(options:).md)
  Returns a list of registered user accounts for your app.
- [VSUserAccountManager.QueryOptions](vsuseraccountmanager/queryoptions.md)
  Constants that represent options you use to fetch a list of user accounts.
### Updating a user account
- [func update(VSUserAccount) async throws](vsuseraccountmanager/update(_:).md)
  Registers a new user account.
### Signing people in automatically
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
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](vsuseraccountmanager/updateautosignintoken(_:updatecontext:).md)
  Sets the current Automatic Sign-In token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Signing people in to their media accounts automatically](signing-people-in-to-media-apps-automatically.md)
  Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.
- [struct VSUserAccount](vsuseraccount-swift.struct.md)
  An object that represents a user’s account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager)*