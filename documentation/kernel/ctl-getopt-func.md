# ctl_getopt_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef errno_t (*ctl_getopt_func)(kern_ctl_ref kctlref, u_int32_t unit, void *unitinfo, int opt, void *data, size_t *len);
```

#### Discussion

The ctl_getopt_func is used to handle client get socket option requests for the SYSPROTO_CONTROL option level. A buffer is allocated for storage and passed to your function. The length of that buffer is also passed. Upon return, you should set *len to length of the buffer used. In some cases, data may be NULL. When this happens, *len should be set to the length you would have returned had data not been NULL. If the buffer is too small, return an error.

## Parameters

- `kctlref`: The control ref of the kernel control.
- `unit`: The unit number of the kernel control instance.
- `unitinfo`: The user-defined private data initialized by the ctl_connect_func callback.
- `opt`: The socket option.
- `data`: A buffer to copy the results in to. May be NULL, see discussion.
- `len`: A pointer to the length of the buffer. This should be set to the length of the buffer used before returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ctl_getopt_func)*