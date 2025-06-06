# networkInterfaces

**Framework**: Virtualization  
**Kind**: property

The bridged network interfaces that you may use in your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class var networkInterfaces: [VZBridgedNetworkInterface] { get }
```

#### Discussion

The system creates the objects in this property based on the available interfaces in the host machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkinterface/networkinterfaces)*