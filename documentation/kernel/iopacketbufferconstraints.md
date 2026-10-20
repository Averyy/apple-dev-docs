# IOPacketBufferConstraints

**Framework**: Kernel  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS 10.6+

## Declaration

```c
typedef struct IOPacketBufferConstraints {
    ...
} IOPacketBufferConstraints;
```

#### Overview

Constraint parameters, specified by a driver, for the data buffer in a packet mbuf. This is observed by allocatePacket() to satisfy the stated requirements.

## Topics

### Instance Properties
- [alignLength](./iopacketbufferconstraints/api-1393417-alignlength.md)
- [alignStart](./iopacketbufferconstraints/api-1393367-alignstart.md)
- [reserved](./iopacketbufferconstraints/api-1393469-reserved.md)

## See Also

### Network Data
- [IONetworkData](./ionetworkdata.md)
  An object that manages a fixed-size named buffer.
- [IONetworkMedium](./ionetworkmedium.md)
  An object that encapsulates information about a network medium (i.e. 10Base-T, or 100Base-T Full Duplex).
- [IOPacketQueue](./iopacketqueue.md)
  Implements a bounded FIFO queue of mbuf packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iopacketbufferconstraints)*