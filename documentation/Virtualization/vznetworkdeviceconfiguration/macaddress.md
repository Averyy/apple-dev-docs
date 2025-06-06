# macAddress

**Framework**: Virtualization  
**Kind**: property

The media access control (MAC) address to assign to the network device.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@NSCopying
var macAddress: VZMACAddress { get set }
```

#### Discussion

The default value of this property is a random, locally administered, unicast address. Assign a custom value to this property if you want your network device to have a specific MAC address.

## See Also

- [var attachment: VZNetworkDeviceAttachment?](vznetworkdeviceconfiguration/attachment.md)
  The object that defines how the virtual network device communicates with the host system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vznetworkdeviceconfiguration/macaddress)*