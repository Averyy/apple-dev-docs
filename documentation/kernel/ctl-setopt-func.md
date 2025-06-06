# ctl_setopt_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.13+

## Declaration

```swift
typedef errno_t (*ctl_setopt_func)(kern_ctl_ref kctlref, u_int32_t unit, void *unitinfo, int opt, void *data, size_t len);
```

#### Discussion

The ctl_setopt_func is used to handle set socket option calls for the SYSPROTO_CONTROL option level.

## Parameters

- `kctlref`: The control ref of the kernel control.
- `unit`: The unit number of the kernel control instance.
- `unitinfo`: The user-defined private data initialized by the ctl_connect_func callback.
- `opt`: The socket option.
- `data`: A pointer to the socket option data. The data has already been copied in to the kernel for you.
- `len`: The length of the socket option data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ctl_setopt_func)*