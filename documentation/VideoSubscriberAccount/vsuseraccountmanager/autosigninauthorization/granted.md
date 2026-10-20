# VSUserAccountManager.AutoSignInAuthorization.granted

**Framework**: Video Subscriber Account  
**Kind**: case  
**Role**: Case

A state that indicates the person opts in to Automatic Sign-In.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
case granted
```

## Mentions

- [Signing people in to their media accounts automatically](../../signing-people-in-to-media-apps-automatically.md)

#### Discussion

This authorization state indicates that a person approves the prompt to opt in to Automatic Sign-In.

For more information, see [`requestAutoSignInAuthorization()`](../requestautosigninauthorization%28%29.md).

## See Also

### Possible states
- [VSUserAccountManager.AutoSignInAuthorization.notDetermined](./notdetermined.md)
  A state that indicates the framework needs to reauthorize Automatic Sign-In.
- [VSUserAccountManager.AutoSignInAuthorization.denied](./denied.md)
  A state that indicates denied authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosigninauthorization/granted)*