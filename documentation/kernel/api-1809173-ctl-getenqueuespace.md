# ctl_getenqueuespace

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.13+

## Declaration

```swift
errno_t ctl_getenqueuespace(kern_ctl_ref kctlref, u_int32_t unit, size_t *space);
```

#### Return_value

0 - Success; the amount of space is returned to caller. EINVAL - Invalid parameters.

#### Discussion

Retrieve the amount of space currently available for data to be sent from the kernel control to the client.

## Parameters

- `kctlref`: The control reference of the kernel control.
- `unit`: The unit number of the kernel control instance.
- `space`: The address where to return the current space available

## See Also

- [ctl_deregister](1809161-ctl_deregister.md)
- [ctl_enqueuedata](1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](2919907-ctl_getenqueuereadable.md)
- [ctl_register](1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809173-ctl_getenqueuespace)*