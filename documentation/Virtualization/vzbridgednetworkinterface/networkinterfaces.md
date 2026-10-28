# networkInterfaces

**Framework**: Virtualization  
**Kind**: property  
**Role**: Type Property

The bridged network interfaces that you may use in your virtual machine.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class var networkInterfaces: [VZBridgedNetworkInterface] { get }
```

```objc
@property (class, copy, readonly) NSArray<VZBridgedNetworkInterface *> * networkInterfaces;
```

## Discussion

The system creates the objects in this property based on the available interfaces in the host machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzbridgednetworkinterface/networkinterfaces)*