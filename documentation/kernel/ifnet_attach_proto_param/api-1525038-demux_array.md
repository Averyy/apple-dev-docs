# demux_array

**Framework**: Kernel  
**Kind**: structp  
**Role**: Instance Property

An array of ifnet_demux_desc structures describing the protocol.

**Availability**:
- macOS 10.6+

## Declaration

```c
struct ifnet_demux_desc *demux_array;
```

## See Also

### Fields
- [demux_count](./api-1525033-demux_count.md)
  The number of entries in the demux_array array.
- [input](./api-1524849-input.md)
  The function to be called for inbound packets.
- [pre_output](./api-1524845-pre_output.md)
  The function to be called for outbound packets.
- [event](./api-1524843-event.md)
  The function to be called for interface events.
- [ioctl](./api-1525050-ioctl.md)
  The function to be called for ioctls.
- [detached](./api-1524863-detached.md)
  The function to be called for handling the detach.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_attach_proto_param/1525038-demux_array)*