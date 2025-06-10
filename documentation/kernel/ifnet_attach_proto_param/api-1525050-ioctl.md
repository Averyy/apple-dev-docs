# ioctl

**Framework**: Kernel  
**Kind**: structp

The function to be called for ioctls.

**Availability**:
- macOS 10.6+

## Declaration

```swift
proto_media_ioctl ioctl;
```

## See Also

- [demux_array](ifnet_attach_proto_param/1525038-demux_array.md)
  An array of ifnet_demux_desc structures describing the protocol.
- [demux_count](ifnet_attach_proto_param/1525033-demux_count.md)
  The number of entries in the demux_array array.
- [input](ifnet_attach_proto_param/1524849-input.md)
  The function to be called for inbound packets.
- [pre_output](ifnet_attach_proto_param/1524845-pre_output.md)
  The function to be called for outbound packets.
- [event](ifnet_attach_proto_param/1524843-event.md)
  The function to be called for interface events.
- [detached](ifnet_attach_proto_param/1524863-detached.md)
  The function to be called for handling the detach.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ifnet_attach_proto_param/1525050-ioctl)*