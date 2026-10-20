# kauth_authorize_process

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 11.0+

## Declaration

```swift
int kauth_authorize_process(kauth_cred_t _credential, kauth_action_t _action, struct proc *_process, uintptr_t _arg1, uintptr_t _arg2, uintptr_t _arg3);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1547411-kauth_authorize_process)*