# ctl_deregister

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```c
errno_t ctl_deregister(kern_ctl_ref kctlref);
```

## Return Value

0 - Kernel control was unregistered. EINVAL - The kernel control reference was invalid. EBUSY - The kernel control has clients still attached.

## Discussion

Unregister a kernel control. A kernel extension must unregister it's kernel control(s) before unloading. If a kernel control has clients attached, this call will fail.

## Parameters

- `kctlref`: The control reference of the control to unregister.

## See Also

### control
- [ctl_enqueuedata](./api-1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](./api-2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](./api-1809173-ctl_getenqueuespace.md)
- [ctl_register](./api-1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809161-ctl_deregister)*