# authorization

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A state that represents a person’s approval of Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- tvOS 26.0+

## Declaration

```objc
@property (nonatomic, readonly) VSAutoSignInAuthorization authorization;
```

#### Discussion

If the person approves the prompt to enable Automatic Sign-In, the framework sets the value to [`VSAutoSignInAuthorizationGranted`](../vsautosigninauthorization/vsautosigninauthorizationgranted.md). If the person denies the prompt, the framework sets the value to [`VSAutoSignInAuthorizationDenied`](../vsautosigninauthorization/vsautosigninauthorizationdenied.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosignintokenupdatecontext/authorization)*