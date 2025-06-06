# proto_media_ioctl

**Framework**: Kernel  
**Kind**: tdef

**Availability**:
- macOS 10.4+

## Declaration

```swift
typedef errno_t (*proto_media_ioctl)(ifnet_t ifp, protocol_family_t protocol, unsigned long command, void *argument);
```

#### Return_value

See the discussion.

#### Discussion

proto_media_event allows this layer to handle ioctls. When an ioctl is handled, it is passed to the interface filters, protocol filters, protocol, and interface. If you do not support this ioctl, return EOPNOTSUPP. If you successfully handle the ioctl, return zero. If you return any error other than EOPNOTSUPP, other parts of the stack may not get an opportunity to process the ioctl. If you return EJUSTRETURN, processing will stop and a result of zero will be returned to the caller.

All undefined ioctls are reserved for future use by Apple. If you need to communicate with your kext using an ioctl, please use SIOCSIFKPI and SIOCGIFKPI.

## Parameters

- `ifp`: The interface.
- `protocol_family`: The protocol family.
- `command`: The ioctl command.
- `argument`: The argument to the ioctl.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/proto_media_ioctl)*