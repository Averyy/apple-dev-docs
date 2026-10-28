# authorization

**Framework**: Video Subscriber Account  
**Kind**: property  
**Role**: Instance Property

A state that represents a person’s approval of Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
@property (nonatomic, readonly) VSAutoSignInAuthorization authorization;
```

## Discussion

The default value is [`VSUserAccountManager.AutoSignInAuthorization.notDetermined`](../vsuseraccountmanager/autosigninauthorization/notdetermined.md). The framework updates the value based on a person’s answer to the prompt to opt in to Automatic Sign-In (see [`requestAutoSignInAuthorization()`](../vsuseraccountmanager/requestautosigninauthorization%28%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosignintoken/authorization)*