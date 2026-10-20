# VSUserAccountManager.AutoSignInAuthorization

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

```swift
enum AutoSignInAuthorization
```

#### Overview

The framework sets the [`authorization`](./autosignintoken-swift.struct/authorization.md) property to one of these values depending on how a person responds to the Automatic Sign-In opt-in prompt.

## Topics

### Possible states
- [VSUserAccountManager.AutoSignInAuthorization.notDetermined](./autosigninauthorization/notdetermined.md)
  A state that indicates the framework needs to reauthorize Automatic Sign-In.
- [VSUserAccountManager.AutoSignInAuthorization.granted](./autosigninauthorization/granted.md)
  A state that indicates the person opts in to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInAuthorization.denied](./autosigninauthorization/denied.md)
  A state that indicates denied authorization.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)

## See Also

### Signing people in automatically
- [VSUserAccountManager.AutoSignInToken](./autosignintoken-swift.struct.md)
  A value that represents a person’s account and their consent to Automatic Sign-In.
- [VSUserAccountManager.AutoSignInTokenUpdateContext](./autosignintokenupdatecontext.md)
  An object that contains information about a person’s choice in the Automatic Sign-In prompt.
- [var autoSignInToken: VSUserAccountManager.AutoSignInToken](./autosignintoken-swift.property.md)
  The current Automatic Sign-In token.
- [func deleteAutoSignInToken() async throws](./deleteautosignintoken%28%29.md)
  Deletes the value of the current Automatic Sign-In token.
- [func requestAutoSignInAuthorization() async throws -> VSUserAccountManager.AutoSignInTokenUpdateContext](./requestautosigninauthorization%28%29.md)
  Presents a modal sheet that offers a person to opt in to Automatic Sign-In.
- [func updateAutoSignInToken(String, updateContext: VSUserAccountManager.AutoSignInTokenUpdateContext) async throws](./updateautosignintoken%28_,updatecontext%29.md)
  Sets the current Automatic Sign-In token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager/autosigninauthorization)*