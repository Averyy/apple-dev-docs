# VSAutoSignInTokenUpdateContext

**Framework**: Video Subscriber Account  
**Kind**: class  
**Role**: Class

An object that contains information about a person’s choice in the Automatic Sign-In prompt.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```objc
@interface VSAutoSignInTokenUpdateContext : NSObject
```

#### Overview

The framework returns an instance of this structure when your app calls [`requestAutoSignInAuthorizationWithCompletionHandler:`](./vsuseraccountmanager/requestautosigninauthorizationwithcompletionhandler_.md) to prompt a person for approval to opt in to Automatic Sign-In.

Check the [`authorization`](./vsautosignintokenupdatecontext/authorization.md) property of this structure to determine the persons choice. If the value is [`VSAutoSignInAuthorizationGranted`](./vsautosigninauthorization/vsautosigninauthorizationgranted.md), generate a sign in token and pass the instance of this structure and the token to the framework using the [`updateAutoSignInToken:updateContext:completionHandler:`](./vsuseraccountmanager/updateautosignintoken_updatecontext_completionhandler_.md) method.

## Topics

### Determining status
- [authorization](./vsautosignintokenupdatecontext/authorization.md)
  A state that represents a person’s approval of Automatic Sign-In.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Signing people in automatically
- [VSAutoSignInToken](./vsautosignintoken.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
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

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosignintokenupdatecontext)*