# ether_frameout

**Framework**: Kernel  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
errno_t ether_frameout(ifnet_t interface, mbuf_t *packet, const struct sockaddr *dest, const char *dest_lladdr, const char *frame_type);
```

## See Also

- [ether_family_init](1397889-ether_family_init.md)
- [ether_add_proto](1397885-ether_add_proto.md)
- [ether_del_proto](1397887-ether_del_proto.md)
- [ether_demux](1397896-ether_demux.md)
- [ether_ioctl](1397890-ether_ioctl.md)
- [ether_check_multi](1397894-ether_check_multi.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1397892-ether_frameout)*