# backtrace_user_copy_fn

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 12.0+

## Declaration

```swift
typedef errno_t (*backtrace_user_copy_fn)(void *ctx, void *dst, user_addr_t src, size_t size);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/backtrace_user_copy_fn)*