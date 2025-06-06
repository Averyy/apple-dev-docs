# kauth_scope_callback_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 11.0+

## Declaration

```swift
typedef int (*kauth_scope_callback_t)(kauth_cred_t _credential, void *_idata, kauth_action_t _action, uintptr_t _arg0, uintptr_t _arg1, uintptr_t _arg2, uintptr_t _arg3);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kauth_scope_callback_t)*