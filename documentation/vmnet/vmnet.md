# vmnet

**Framework**: vmnet  
**Kind**: module

Connect with network interfaces to read and write packets on guest operating systems.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.10+

#### Overview

The vmnet framework is an API for virtual machines to read and write packets.

The API allows a Guest OS interface to be in host mode or shared mode. Interfaces in host mode can communicate with the native host system and other interfaces running in host mode. In shared mode, the network interface can send and receive packets to the Internet, the native host, and other interfaces running in sharing mode.

> **Note**: For more information about virtualization technologies, see the [`Hypervisor`](https://developer.apple.com/documentation/Hypervisor) framework.

##### Requirements

The vmnet framework has the following requirements:

###### Entitlements

A sandboxed user space process must have the `com.apple.vm.networking` entitlement in order to use vmnet API.

##### Architecture

![None](https://docs-assets.developer.apple.com/published/f44bf3214239dd313122f60d6de7c4a8/media-2557515%402x.png)

The VM Network API provides support for an interface in the guest operating system. The API provides the MAC address and MTU that needs to be configured on the guest OS interface. The interface receives a private IPv4 address via DHCP. IPv4 traffic originating from the guest operating system must use the private IPv4 address. Packets sent from a different IPv4 address are dropped by the system.

You can create a maximum of 32 interfaces with a limit of 4 per guest operating system. Each read/write call allows up to 200 packets to be read or written for a maximum of 256KB. Each packet written should be a complete ethernet frame.

## Topics

### Essentials
- [com.apple.vm.networking](../BundleResources/Entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
### Starting and Stopping Interfaces
- [func vmnet_start_interface(xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](vmnet_start_interface(_:_:_:).md)
  Starts host or shared mode on an interface with a specified configuration.
- [func vmnet_interface_set_event_callback(interface_ref, interface_event_t, dispatch_queue_t?, vmnet_interface_event_callback_t?) -> vmnet_return_t](vmnet_interface_set_event_callback(_:_:_:_:).md)
  Schedules a callback to be executed when events for the specified interface are received.
- [func vmnet_stop_interface(interface_ref, dispatch_queue_t, vmnet_interface_completion_handler_t) -> vmnet_return_t](vmnet_stop_interface(_:_:_:).md)
  Stops the interface.
### Reading and Writing Packets
- [func vmnet_read(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t](vmnet_read(_:_:_:).md)
  Attempts to read a specified number of packets from an interface.
- [func vmnet_write(interface_ref, UnsafeMutablePointer<vmpktdesc>, UnsafeMutablePointer<Int32>) -> vmnet_return_t](vmnet_write(_:_:_:).md)
  Attempts to write specified packets to an interface.
### Data Types
- [enum vmnet_return_t](vmnet_return_t.md)
  Values returned by functions in the vmnet Framework.
- [struct vmpktdesc](vmpktdesc.md)
  Describes a packet.
- [typealias interface_ref](interface_ref.md)
  A virtual network interface.
- [struct interface_event_t](interface_event_t.md)
  Interface event types.
- [enum operating_modes_t](operating_modes_t.md)
  The operating modes for an interface.
### Constants
- [interface_desc XPC Dictionary Keys](interface_desc_xpc_dictionary_keys.md)
  XPC dictionary keys supported by the `interface_desc` parameter passed to the `vmnet` function to describe the parameters of the network interface.
- [interface_param XPC Dictionary Keys](interface_param_xpc_dictionary_keys.md)
  XPC dictionary keys used by the `interface_param` argument returned by the completion handler of the `vmnet` function that describes the parameters that should be used to configure the network interface.
- [event XPC Dictionary](event_xpc_dictionary.md)
  XPC dictionary keys used by the `event` value returned to the client in the `handler` callback specified by the `vmnet` function that provides information about the callback event.
### Reference
- [vmnet Constants](vmnet_constants.md)
- [vmnet Functions](vmnet_functions.md)
- [vmnet Data Types](vmnet_data_types.md)
### Variables
- [let vmnet_enable_virtio_header_key: UnsafePointer<CChar>](vmnet_enable_virtio_header_key-swift.var.md)
- [let vmnet_read_max_packets_key: UnsafePointer<CChar>](vmnet_read_max_packets_key.md)
- [let vmnet_write_max_packets_key: UnsafePointer<CChar>](vmnet_write_max_packets_key.md)
### Functions
- [func vmnet_interface_start_with_network(vmnet_network_ref, xpc_object_t, dispatch_queue_t, vmnet_start_interface_completion_handler_t) -> interface_ref?](vmnet_interface_start_with_network(_:_:_:_:).md)
- [func vmnet_network_configuration_add_dhcp_reservation(vmnet_network_configuration_ref, UnsafePointer<ether_addr_t>, UnsafePointer<in_addr>) -> vmnet_return_t](vmnet_network_configuration_add_dhcp_reservation(_:_:_:).md)
- [func vmnet_network_configuration_add_port_forwarding_rule(vmnet_network_configuration_ref, UInt8, sa_family_t, UInt16, UInt16, UnsafeRawPointer) -> vmnet_return_t](vmnet_network_configuration_add_port_forwarding_rule(_:_:_:_:_:_:).md)
- [func vmnet_network_configuration_create(vmnet_mode_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_configuration_ref?](vmnet_network_configuration_create(_:_:).md)
- [func vmnet_network_configuration_disable_dhcp(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_dhcp(_:).md)
- [func vmnet_network_configuration_disable_dns_proxy(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_dns_proxy(_:).md)
- [func vmnet_network_configuration_disable_nat44(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat44(_:).md)
- [func vmnet_network_configuration_disable_nat66(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_nat66(_:).md)
- [func vmnet_network_configuration_disable_router_advertisement(vmnet_network_configuration_ref)](vmnet_network_configuration_disable_router_advertisement(_:).md)
- [func vmnet_network_configuration_set_external_interface(vmnet_network_configuration_ref, UnsafePointer<CChar>) -> vmnet_return_t](vmnet_network_configuration_set_external_interface(_:_:).md)
- [func vmnet_network_configuration_set_ipv4_subnet(vmnet_network_configuration_ref, UnsafePointer<in_addr>, UnsafePointer<in_addr>) -> vmnet_return_t](vmnet_network_configuration_set_ipv4_subnet(_:_:_:).md)
- [func vmnet_network_configuration_set_ipv6_prefix(vmnet_network_configuration_ref, UnsafePointer<in6_addr>, UInt8) -> vmnet_return_t](vmnet_network_configuration_set_ipv6_prefix(_:_:_:).md)
- [func vmnet_network_configuration_set_mtu(vmnet_network_configuration_ref, UInt32) -> vmnet_return_t](vmnet_network_configuration_set_mtu(_:_:).md)
- [func vmnet_network_copy_serialization(vmnet_network_ref, UnsafeMutablePointer<vmnet_return_t>?) -> xpc_object_t?](vmnet_network_copy_serialization(_:_:).md)
- [func vmnet_network_create(vmnet_network_configuration_ref, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create(_:_:).md)
- [func vmnet_network_create_with_serialization(xpc_object_t, UnsafeMutablePointer<vmnet_return_t>?) -> vmnet_network_ref?](vmnet_network_create_with_serialization(_:_:).md)
- [func vmnet_network_get_ipv4_subnet(vmnet_network_ref, UnsafeMutablePointer<in_addr>, UnsafeMutablePointer<in_addr>)](vmnet_network_get_ipv4_subnet(_:_:_:).md)
- [func vmnet_network_get_ipv6_prefix(vmnet_network_ref, UnsafeMutablePointer<in6_addr>, UnsafeMutablePointer<UInt8>)](vmnet_network_get_ipv6_prefix(_:_:_:).md)
### Type Aliases
- [typealias vmnet_mode_t](vmnet_mode_t.md)
- [typealias vmnet_network_configuration_ref](vmnet_network_configuration_ref.md)
- [typealias vmnet_network_ref](vmnet_network_ref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet)*