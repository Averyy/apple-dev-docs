# ctl_register

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.13+

## Declaration

```swift
errno_t ctl_register(struct kern_ctl_reg *userkctl, kern_ctl_ref *kctlref);
```

#### Return_value

0 - Kernel control was registered. EINVAL - The registration structure was not valid. ENOMEM - There was insufficient memory. EEXIST - A controller with that id/unit is already registered.

#### Discussion

Register a kernel control. This will enable clients to connect to the kernel control using a PF_SYSTEM socket.

## Parameters

- `userkctl`: A structure defining the kernel control to be attached. The ctl_connect callback must be specified, the other callbacks are optional. If ctl_connect is set to zero, ctl_register fails with the error code EINVAL.
- `kctlref`: Upon successful return, the kctlref will contain a reference to the attached kernel control. This reference is used to unregister the kernel control. This reference will also be passed in to the callbacks each time they are called.

## See Also

- [ctl_deregister](1809161-ctl_deregister.md)
- [ctl_enqueuedata](1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](1809173-ctl_getenqueuespace.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809176-ctl_register)*