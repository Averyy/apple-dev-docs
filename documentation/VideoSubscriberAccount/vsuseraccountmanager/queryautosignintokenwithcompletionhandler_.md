# queryAutoSignInTokenWithCompletionHandler:

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Retrieves the current Automatic Sign-In token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) queryAutoSignInTokenWithCompletionHandler:(void (^)(VSAutoSignInToken *token, NSError *error)) completion;
```

## Discussion

The framework sets this property to the current Automatic Sign-In token value and authorization status according to information on the person’s Account Account.

For more information, see [Signing people in to their media accounts automatically](../signing-people-in-to-media-apps-automatically.md).

## See Also

### Signing people in automatically
- [VSAutoSignInToken](../vsautosignintoken.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSAutoSignInTokenUpdateContext](../vsautosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [VSAutoSignInAuthorization](../vsautosigninauthorization.md)
  The possible states the framework sets for Automatic Sign-In.
- [- deleteAutoSignInTokenWithCompletionHandler:](./deleteautosignintokenwithcompletionhandler_.md)
  Deletes the value of the current Automatic Sign-In token.
- [- requestAutoSignInAuthorizationWithCompletionHandler:](./requestautosigninauthorizationwithcompletionhandler_.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [- updateAutoSignInToken:updateContext:completionHandler:](./updateautosignintoken_updatecontext_completionhandler_.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/queryautosignintokenwithcompletionhandler:)*