# ctl_enqueuedata

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```c
errno_t ctl_enqueuedata(kern_ctl_ref kctlref, u_int32_t unit, void *data, size_t len, u_int32_t flags);
```

#### Return Value

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

### control
- [ctl_deregister](./api-1809161-ctl_deregister.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuereadable](./api-2919907-ctl_getenqueuereadable.md)
- [ctl_getenqueuespace](./api-1809173-ctl_getenqueuespace.md)
- [ctl_register](./api-1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1809168-ctl_enqueuedata)*