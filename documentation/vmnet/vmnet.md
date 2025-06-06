# vmnet

**Framework**: Vmnet  
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
- [var vmnet_enable_virtio_header_key: UnsafePointer<CChar>](vmnet_enable_virtio_header_key-swift.var.md)
- [var vmnet_read_max_packets_key: UnsafePointer<CChar>](vmnet_read_max_packets_key.md)
- [var vmnet_write_max_packets_key: UnsafePointer<CChar>](vmnet_write_max_packets_key.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/vmnet)*