# adaptor

**Framework**: Virtualization  
**Kind**: property

The virtual machine view adaptor.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var adaptor: VZVirtualMachineViewAdaptor? { get set }
```

#### Discussion

Use this property to assign a [`VZVirtualMachineViewAdaptor`](vzvirtualmachineviewadaptor.md), which is a sendable wrapper that connects a virtual machine view to a virtual machine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview/adaptor)*