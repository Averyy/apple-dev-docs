# ctl_getenqueuespace

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```c
errno_t ctl_getenqueuespace(kern_ctl_ref kctlref, u_int32_t unit, size_t *space);
```

#### Return Value

0 - Success; the amount of space is returned to caller. EINVAL - Invalid parameters.

#### Discussion

Retrieve the amount of space currently available for data to be sent from the kernel control to the client.

## Parameters

- `kctlref`: The control reference of the kernel control.
- `unit`: The unit number of the kernel control instance.
- `space`: The address where to return the current space available

## See Also

### control
- [ctl_deregister](./api-1809161-ctl_deregister.md)
- [ctl_enqueuedata](./api-1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](./api-2919907-ctl_getenqueuereadable.md)
- [ctl_register](./api-1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809173-ctl_getenqueuespace)*