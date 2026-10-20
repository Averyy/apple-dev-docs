# iff_ioctl_func

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*iff_ioctl_func)(void *cookie, ifnet_t interface, protocol_family_t protocol, unsigned long ioctl_cmd, void *ioctl_arg);
```

#### Return_value

Return: 0 - This filter function handled the ioctl. EOPNOTSUPP - This filter function does not understand/did not handle this ioctl. EJUSTRETURN - This filter function handled the ioctl, processing should stop. Anything Else - Processing will stop, the error will be returned.

#### Discussion

iff_ioctl_func is used to filter ioctls sent to an interface. The interface is only valid for the duration of the filter call. If you need to keep a reference to the interface, be sure to call ifnet_reference and ifnet_release.

All undefined ioctls are reserved for future use by Apple. If you need to communicate with your kext using an ioctl, please use SIOCSIFKPI and SIOCGIFKPI.

## Parameters

- `cookie`: The cookie specified when this filter was attached.
- `interface`: The interface the packet is being transmitted on.
- `ioctl_cmd`: The ioctl command.
- `ioctl_arg`: A pointer to the ioctl argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iff_ioctl_func)*