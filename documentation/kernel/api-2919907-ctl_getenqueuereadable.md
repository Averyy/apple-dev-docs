# ctl_getenqueuereadable

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.13+

## Declaration

```c
errno_t ctl_getenqueuereadable(kern_ctl_ref kctlref, u_int32_t unit, u_int32_t *difference);
```

## See Also

### control
- [ctl_deregister](./api-1809161-ctl_deregister.md)
- [ctl_enqueuedata](./api-1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](./api-1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuespace](./api-1809173-ctl_getenqueuespace.md)
- [ctl_register](./api-1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/2919907-ctl_getenqueuereadable)*