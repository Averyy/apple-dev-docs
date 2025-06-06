# sockaddr_ctl

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.13+

## Declaration

```swift
struct sockaddr_ctl {
    ...
};
```

#### Discussion

The controller address structure is used to establish contact between a user client and a kernel controller. The sc_id/sc_unit uniquely identify each controller. sc_id is a unique identifier assigned to the controller. The identifier can be assigned by the system at registration time or be a 32-bit creator code obtained from Apple Computer. sc_unit is a unit number for this sc_id, and is privately used by the kernel controller to identify several instances of the controller.

## Topics

### Fields
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
- [sc_reserved](sockaddr_ctl/1809263-sc_reserved.md)
  Reserved, must be set to zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/sockaddr_ctl)*