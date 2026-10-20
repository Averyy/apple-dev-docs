# attachment

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The network attachment that’s connected to this network device.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var attachment: VZNetworkDeviceAttachment? { get set }
```

```objc
@property (strong, nullable) VZNetworkDeviceAttachment * attachment;
```

#### Discussion

Setting this property results in an attempt to change the network device attachment which may fail. If the devices fails to attach, the system invokes [`virtualMachine(_:networkDevice:attachmentWasDisconnectedWithError:)`](../vzvirtualmachinedelegate/virtualmachine%28_,networkdevice,attachmentwasdisconnectedwitherror%29.md) and sets this property to `nil`. This property may change at any time while the VM is running based on the state of the host network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdevice/attachment)*