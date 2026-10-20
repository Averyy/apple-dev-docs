# ctl_register

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```c
errno_t ctl_register(struct kern_ctl_reg *userkctl, kern_ctl_ref *kctlref);
```

#### Return Value

0 - Kernel control was registered. EINVAL - The registration structure was not valid. ENOMEM - There was insufficient memory. EEXIST - A controller with that id/unit is already registered.

#### Discussion

Register a kernel control. This will enable clients to connect to the kernel control using a PF_SYSTEM socket.

## Parameters

- `userkctl`: A structure defining the kernel control to be attached. The ctl_connect callback must be specified, the other callbacks are optional. If ctl_connect is set to zero, ctl_register fails with the error code EINVAL.
- `kctlref`: Upon successful return, the kctlref will contain a reference to the attached kernel control. This reference is used to unregister the kernel control. This reference will also be passed in to the callbacks each time they are called.

## See Also

### control
- [ctl_deregister](./api-1809161-ctl_deregister.md)
- [ctl_enqueuedata](./api-1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](./api-2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](./api-1809173-ctl_getenqueuespace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809176-ctl_register)*