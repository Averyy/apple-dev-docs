# ctl_info

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.13+

## Declaration

```swift
struct ctl_info {
    ...
};
```

#### Discussion

This structure is used with the CTLIOCGINFO ioctl to translate from a kernel control name to a control id.

## Topics

### Fields
- [ctl_id](ctl_info/1809204-ctl_id.md)
  The kernel control id, filled out upon return.
- [ctl_name](ctl_info/1809207-ctl_name.md)
  The kernel control name to find.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ctl_info)*