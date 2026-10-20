# guestDidStop(_:)

**Framework**: Virtualization  
**Kind**: method

Tells the delegate that the guest operating system stopped the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
optional func guestDidStop(_ virtualMachine: VZVirtualMachine)
```

## Parameters

- `virtualMachine`: The VM that called the delegate method.

## See Also

- [func virtualMachine(VZVirtualMachine, didStopWithError: any Error)](vzvirtualmachinedelegate/virtualmachine(_:didstopwitherror:).md)
  Tells the delegate that the VM stopped because of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate/guestdidstop(_:))*