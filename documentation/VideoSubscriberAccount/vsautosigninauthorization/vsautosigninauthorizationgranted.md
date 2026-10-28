# VSAutoSignInAuthorizationGranted

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Enumeration Case

A state that indicates the person opts in to Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
VSAutoSignInAuthorizationGranted
```

## Discussion

This authorization state indicates that a person approves the prompt to opt in to Automatic Sign-In.

For more information, see [`requestAutoSignInAuthorization()`](../vsuseraccountmanager/requestautosigninauthorization%28%29.md).

## See Also

### Possible states
- [VSAutoSignInAuthorizationNotDetermined](./vsautosigninauthorizationnotdetermined.md)
  A state that indicates the framework needs to reauthorize Automatic Sign-In.
- [VSAutoSignInAuthorizationDenied](./vsautosigninauthorizationdenied.md)
  A state that indicates the person denied authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsautosigninauthorization/vsautosigninauthorizationgranted)*