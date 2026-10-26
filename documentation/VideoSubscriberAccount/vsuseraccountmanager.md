# VSUserAccountManager

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

The object that coordinates your app’s user account actions.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+

## Declaration

```swift
class VSUserAccountManager
```

```objc
@interface VSUserAccountManager : NSObject
```

#### Overview

Don’t create `VSUserAccountManager` directly; use [`shared`](./vsuseraccountmanager/shared.md).

## Topics

### Getting the account manager
- [class var shared: VSUserAccountManager](./vsuseraccountmanager/shared.md)
  A shared instance of the user account manager class.
### Getting user accounts
- [func userAccounts(options: VSUserAccountManager.QueryOptions) async throws -> [VSUserAccount]](./vsuseraccountmanager/useraccounts%28options%29.md)
  Returns a list of registered user accounts for your app.
- [VSUserAccountManager.QueryOptions](./vsuseraccountmanager/queryoptions.md)
  Constants that represent options you use to fetch a list of user accounts.
- [- queryUserAccountsWithOptions:completion:](./vsuseraccountmanager/queryuseraccountswithoptions_completion_.md)
  Returns a list of registered user accounts for your app.
### Updating a user account
- [func update(VSUserAccount) async throws](./vsuseraccountmanager/update%28_%29.md)
  Registers a new user account.
- [- updateUserAccount:completion:](./vsuseraccountmanager/updateuseraccount_completion_.md)
  Registers a new user account.
### Signing people in automatically
- [VSUserAccountManager.AutoSignInToken](./vsuseraccountmanager/autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](./vsuseraccountmanager/autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSUserAccountManager.AutoSignInAuthorization](./vsuseraccountmanager/autosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](./vsuseraccountmanager/autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func deleteAutoSignInToken() async throws](./vsuseraccountmanager/deleteautosignintoken%28%29.md)
  Deletes the value of the current Automatic Sign-In token.
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](./vsuseraccountmanager/requestautosigninauthorization%28%29.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](./vsuseraccountmanager/updateautosignintoken%28_,updatecontext%29.md)
  Sets the current Automatic Sign-In token.
- [VSAutoSignInToken](./vsautosignintoken.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSAutoSignInTokenUpdateContext](./vsautosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSAutoSignInAuthorization](./vsautosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [- queryAutoSignInTokenWithCompletionHandler:](./vsuseraccountmanager/queryautosignintokenwithcompletionhandler_.md)
  Retrieves the current Automatic Sign-In token.
- [- deleteAutoSignInTokenWithCompletionHandler:](./vsuseraccountmanager/deleteautosignintokenwithcompletionhandler_.md)
  Deletes the value of the current Automatic Sign-In token.
- [- requestAutoSignInAuthorizationWithCompletionHandler:](./vsuseraccountmanager/requestautosigninauthorizationwithcompletionhandler_.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [- updateAutoSignInToken:updateContext:completionHandler:](./vsuseraccountmanager/updateautosignintoken_updatecontext_completionhandler_.md)
  Sets the current Automatic Sign-In token.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### User account management
- [Signing people in to their media accounts automatically](./signing-people-in-to-media-apps-automatically.md)
  Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.
- [struct VSUserAccount](./vsuseraccount-swift.struct.md)
  An object that represents a user’s account.
- [VSUserAccount](./vsuseraccount-c.class.md)
  An object that represents a user’s account with a TV provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager)*