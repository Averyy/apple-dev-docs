# maximumTransmissionUnit

**Framework**: Virtualization  
**Kind**: property

An integer value that indicates the maximum transmission unit (MTU) associated with this attachment.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var maximumTransmissionUnit: Int { get set }
```

#### Discussion

The client side of the associated datagram socket must be properly configured with the appropriate values for `SO_SNDBUF`, and `SO_RCVBUF`. Set these using the `setsockopt(_:_:_:_:_:)` system call. The system expects the value of `SO_RCVBUF` to be at least double the value of `SO_SNDBUF`, and for optimal performance, the recommended value of `SO_RCVBUF` is four times the value of `SO_SNDBUF`.

The default MTU is 1500. The maximum MTU allowed is 65535, and the minimum MTU allowed is 1500. An invalid MTU value results in an invalid virtual machine configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzfilehandlenetworkdeviceattachment/maximumtransmissionunit)*