# ctl_deregister

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.13+

## Declaration

```swift
errno_t ctl_deregister(kern_ctl_ref kctlref);
```

#### Return_value

0 - Kernel control was unregistered. EINVAL - The kernel control reference was invalid. EBUSY - The kernel control has clients still attached.

#### Discussion

Unregister a kernel control. A kernel extension must unregister it's kernel control(s) before unloading. If a kernel control has clients attached, this call will fail.

## Parameters

- `kctlref`: The control reference of the control to unregister.

## See Also

- [ctl_enqueuedata](1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](1809173-ctl_getenqueuespace.md)
- [ctl_register](1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809161-ctl_deregister)*