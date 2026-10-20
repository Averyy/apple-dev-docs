# network

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The network object that the you initialize the attachment with.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var network: vmnet_network_ref { get }
```

```objc
@property (readonly) vmnet_network_ref network;
```

## See Also

### Creating the vmnet network device attachment
- [init(network: vmnet_network_ref)](./init%28network%29.md)
  Creates the attachment and configures it with the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvmnetnetworkdeviceattachment/network)*