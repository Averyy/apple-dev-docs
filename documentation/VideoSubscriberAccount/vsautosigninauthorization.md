# VSAutoSignInAuthorization

**Framework**: Video Subscriber Account  
**Kind**: enum  
**Role**: Enumeration

The possible states the framework sets for Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
enum VSAutoSignInAuthorization : NSInteger;
```

## Overview

The framework sets the [`authorization`](./vsautosignintoken/authorization.md) property to one of these values depending on how a person responds to the framework prompt that offers to enable Automatic Sign-In.

## Topics

### Possible states
- [VSAutoSignInAuthorizationNotDetermined](./vsautosigninauthorization/vsautosigninauthorizationnotdetermined.md)
  A state that indicates the framework needs to reauthorize Automatic Sign-In.
- [VSAutoSignInAuthorizationGranted](./vsautosigninauthorization/vsautosigninauthorizationgranted.md)
  A state that indicates the person opts in to Automatic Sign-In.
- [VSAutoSignInAuthorizationDenied](./vsautosigninauthorization/vsautosigninauthorizationdenied.md)
  A state that indicates the person denied authorization.

## See Also

### Signing people in automatically
- [VSAutoSignInToken](./vsautosignintoken.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSAutoSignInTokenUpdateContext](./vsautosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [- queryAutoSignInTokenWithCompletionHandler:](./vsuseraccountmanager/queryautosignintokenwithcompletionhandler_.md)
  Retrieves the current Automatic Sign-In token.
- [- deleteAutoSignInTokenWithCompletionHandler:](./vsuseraccountmanager/deleteautosignintokenwithcompletionhandler_.md)
  Deletes the value of the current Automatic Sign-In token.
- [- requestAutoSignInAuthorizationWithCompletionHandler:](./vsuseraccountmanager/requestautosigninauthorizationwithcompletionhandler_.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [- updateAutoSignInToken:updateContext:completionHandler:](./vsuseraccountmanager/updateautosignintoken_updatecontext_completionhandler_.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosigninauthorization)*