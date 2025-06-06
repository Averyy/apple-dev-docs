# ctl_enqueuedata

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.13+

## Declaration

```swift
errno_t ctl_enqueuedata(kern_ctl_ref kctlref, u_int32_t unit, void *data, size_t len, u_int32_t flags);
```

#### Return_value

0 - Data was enqueued to be read by the client. EINVAL - Invalid parameters. EMSGSIZE - The buffer is too large. ENOBUFS - The queue is full or there are no free mbufs.

#### Discussion

Send data from the kernel control to the client.

## Parameters

- `kctlref`: The control reference of the kernel control.
- `unit`: The unit number of the kernel control instance.
- `data`: A pointer to the data to send.
- `len`: The length of data to send.
- `flags`: Send flags. CTL_DATA_NOWAKEUP and CTL_DATA_EOR are currently the only supported flags.

## See Also

- [ctl_deregister](1809161-ctl_deregister.md)
- [ctl_enqueuembuf](1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](1809173-ctl_getenqueuespace.md)
- [ctl_register](1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809168-ctl_enqueuedata)*