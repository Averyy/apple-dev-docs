# sc_reserved

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

Reserved, must be set to zero.

**Availability**:
- macOS 10.13+

## Declaration

```c
u_int32_t sc_reserved[5];
```

## See Also

### Fields
- [sc_len](./api-1809243-sc_len.md)
  The length of the structure.
- [sc_family](./api-1809246-sc_family.md)
  AF_SYSTEM.
- [ss_sysaddr](./api-1809252-ss_sysaddr.md)
  AF_SYS_KERNCONTROL.
- [sc_id](./api-1809255-sc_id.md)
  Controller unique identifier.
- [sc_unit](./api-1809262-sc_unit.md)
  Kernel controller private unit number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sockaddr_ctl/1809263-sc_reserved)*