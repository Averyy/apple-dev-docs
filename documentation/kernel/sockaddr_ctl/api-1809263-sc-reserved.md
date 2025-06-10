# sc_reserved

**Framework**: Kernel  
**Kind**: structp

Reserved, must be set to zero.

**Availability**:
- macOS 10.13+

## Declaration

```swift
u_int32_t sc_reserved[5];
```

## See Also

- [sc_len](sockaddr_ctl/1809243-sc_len.md)
  The length of the structure.
- [sc_family](sockaddr_ctl/1809246-sc_family.md)
  AF_SYSTEM.
- [ss_sysaddr](sockaddr_ctl/1809252-ss_sysaddr.md)
  AF_SYS_KERNCONTROL.
- [sc_id](sockaddr_ctl/1809255-sc_id.md)
  Controller unique identifier.
- [sc_unit](sockaddr_ctl/1809262-sc_unit.md)
  Kernel controller private unit number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sockaddr_ctl/1809263-sc_reserved)*