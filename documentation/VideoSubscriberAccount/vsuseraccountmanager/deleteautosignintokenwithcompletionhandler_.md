# deleteAutoSignInTokenWithCompletionHandler:

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Deletes the value of the current Automatic Sign-In token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) deleteAutoSignInTokenWithCompletionHandler:(void (^)(NSError *error)) completion;
```

## Discussion

This method sets the contents of [`value`](./autosignintoken-swift.struct/value.md) to `nil` for the current [`autoSignInToken`](./autosignintoken-swift.property.md).

You might delete an Automatic Sign-In token, for example, if:

- Your app provides its own UI that lets the person opt out of Automatic Sign-In.
- The person changes their password and wants to sign out from all of their devices.
- Your app implements conditions to invalidate a token, such as if a person flags a specific log in as unauthorized.

## See Also

### Signing people in automatically
- [VSAutoSignInToken](../vsautosignintoken.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSAutoSignInTokenUpdateContext](../vsautosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSAutoSignInAuthorization](../vsautosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [- queryAutoSignInTokenWithCompletionHandler:](./queryautosignintokenwithcompletionhandler_.md)
  Retrieves the current Automatic Sign-In token.
- [- requestAutoSignInAuthorizationWithCompletionHandler:](./requestautosigninauthorizationwithcompletionhandler_.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [- updateAutoSignInToken:updateContext:completionHandler:](./updateautosignintoken_updatecontext_completionhandler_.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/deleteautosignintokenwithcompletionhandler:)*