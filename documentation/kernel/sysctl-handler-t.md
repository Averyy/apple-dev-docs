# sysctl_handler_t

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.5+

## Declaration

```swift
typedef int (*sysctl_handler_t)(struct sysctl_oid *oidp, void *arg1, int arg2, struct sysctl_req *req);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sysctl_handler_t)*