# VSAutoSignInToken

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

A value that represents a person’s account and their consent to Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@interface VSAutoSignInToken : NSObject
```

#### Overview

Automatic Sign-In tokens implement a single sign-on experience for media streaming services for a signed-in Apple Account.

The framework sets [`autoSignInToken`](./vsuseraccountmanager/autosignintoken-swift.property.md) to an instance of this structure. The source of the information inside depends on whether the person approves the prompt to opt in to Automatic Sign-In. For more information, see [`requestAutoSignInAuthorization()`](./vsuseraccountmanager/requestautosigninauthorization%28%29.md).

Alternatively, if you delete the token value by calling [`deleteAutoSignInToken()`](./vsuseraccountmanager/deleteautosignintoken%28%29.md), the framework sets [`value`](./vsautosignintoken/value.md) to `nil` and [`authorization`](./vsautosignintoken/authorization.md) to [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](./vsuseraccountmanager/autosigninauthorization/notdetermined.md).

> ❗ **Important**: Only use an Automatic Sign-In token to turn on media streaming. For example, avoid using the token itself as a gate that lets the person manage their account.

For more information about Automatic Sign-In tokens, see [Signing people in to their media accounts automatically](./signing-people-in-to-media-apps-automatically.md).

## Topics

### Defining the token value
- [value](./vsautosignintoken/value.md)
  A string that represents a person’s account.
### Determining status
- [authorization](./vsautosignintoken/authorization.md)
  A state that represents a person’s approval of Automatic Sign-In.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Signing people in automatically
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosignintoken)*