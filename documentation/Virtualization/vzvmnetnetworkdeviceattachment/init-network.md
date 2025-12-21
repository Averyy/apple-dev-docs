# init(network:)

**Framework**: Virtualization  
**Kind**: init

Creates the attachment and configures it with the specified data.

**Availability**:
- macOS 26.0+

## Declaration

```swift
init(network: vmnet_network_ref)
```

#### Return Value

An initialized `VZVmnetNetworkDeviceAttachment` object, or `nil` if there was an error.

#### Discussion

To ensure proper isolation between application processes, a virtual machine (VM) can only use the `network` that the same application process creates. If an application’s VM tries to use a `network` that another application’s VM creates, initialization fails.

For more information on vmnet configuration requirements and restrictions, see [`vmnet`](https://developer.apple.com/documentation/vmnet)

The following example demonstrates how to create and initialize a custom network using `VZVmnetNetworkDeviceAttachment`.

## Parameters

- `network`: The logical network object

## See Also

- [var network: vmnet_network_ref](vzvmnetnetworkdeviceattachment/network.md)
  The network object that the you initialize the attachment with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvmnetnetworkdeviceattachment/init(network:))*