# interface_param XPC Dictionary Keys

**Framework**: vmnet

XPC dictionary keys used by the `interface_param` argument returned by the completion handler of the `vmnet` function that describes the parameters that should be used to configure the network interface.

## Topics

### Constants
- [let vmnet_mac_address_key: UnsafePointer<CChar>](vmnet_mac_address_key.md)
- [let vmnet_mtu_key: UnsafePointer<CChar>](vmnet_mtu_key.md)
- [let vmnet_max_packet_size_key: UnsafePointer<CChar>](vmnet_max_packet_size_key.md)

## See Also

- [interface_desc XPC Dictionary Keys](interface_desc_xpc_dictionary_keys.md)
  XPC dictionary keys supported by the `interface_desc` parameter passed to the `vmnet` function to describe the parameters of the network interface.
- [event XPC Dictionary](event_xpc_dictionary.md)
  XPC dictionary keys used by the `event` value returned to the client in the `handler` callback specified by the `vmnet` function that provides information about the callback event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet/interface_param_xpc_dictionary_keys)*