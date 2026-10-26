# updateAutoSignInToken:updateContext:completionHandler:

**Framework**: Video Subscriber Account  
**Kind**: method  
**Role**: Instance Method

Sets the current Automatic Sign-In token.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```objc
- (void) updateAutoSignInToken:(NSString *) autoSignInToken updateContext:(VSAutoSignInTokenUpdateContext *) context completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

Call this method when generating a new token value for an account. To update the token, request the person’s authorization for Automatic Sign-In. For more information, see [`requestAutoSignInAuthorization()`](./requestautosigninauthorization%28%29.md).

## Parameters

- `autoSignInToken`: The new token value to store in the person’s Apple Account. Your app determines the contents of this string using a mechanism you determine fitting to identify the account. In addition, ensure its value is of sufficient length, complexity, and security. For more information on setting this property, see [`value`](../vsautosignintoken/value.md).
- `context`: The object the framework provides that reflects the person’s choice in the authorization prompt; pass the result of the [`requestAutoSignInAuthorizationWithCompletionHandler:`](./requestautosigninauthorizationwithcompletionhandler_.md) method.
- `completion`: Code you supply that the framework runs after storing the updated token.

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
- [- deleteAutoSignInTokenWithCompletionHandler:](./deleteautosignintokenwithcompletionhandler_.md)
  Deletes the value of the current Automatic Sign-In token.
- [- requestAutoSignInAuthorizationWithCompletionHandler:](./requestautosigninauthorizationwithcompletionhandler_.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/updateautosignintoken:updatecontext:completionhandler:)*