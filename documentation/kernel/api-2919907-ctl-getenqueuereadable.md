# ctl_getenqueuereadable

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.13+

## Declaration

```swift
errno_t ctl_getenqueuereadable(kern_ctl_ref kctlref, u_int32_t unit, u_int32_t *difference);
```

## See Also

- [ctl_deregister](1809161-ctl_deregister.md)
- [ctl_enqueuedata](1809168-ctl_enqueuedata.md)
- [ctl_enqueuembuf](1809171-ctl_enqueuembuf.md)
- [ctl_getenqueuespace](1809173-ctl_getenqueuespace.md)
- [ctl_register](1809176-ctl_register.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/2919907-ctl_getenqueuereadable)*