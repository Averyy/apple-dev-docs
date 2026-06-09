# init(virtualMachine:)

**Framework**: Virtualization  
**Kind**: init

Initialize an adaptor for a virtual machine.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init(virtualMachine: VZVirtualMachine)
```

#### Discussion

If the virtual machine has graphics devices, the first display of the first graphics device is used. If the virtual machine has no graphics devices, the adaptor is created successfully but the view will have no display.

## Parameters

- `virtualMachine`: The virtual machine to adapt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineviewadaptor/init(virtualmachine:))*