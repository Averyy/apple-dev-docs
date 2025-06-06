# virtualMachine(_:didStopWithError:)

**Framework**: Virtualization  
**Kind**: method

Tells the delegate that the VM stopped because of an error.

**Availability**:
- macOS 11.0+

## Declaration

```swift
optional func virtualMachine(_ virtualMachine: VZVirtualMachine, didStopWithError error: any Error)
```

## Parameters

- `virtualMachine`: The VM that called the delegate method.
- `error`: The error.

## See Also

- [func guestDidStop(VZVirtualMachine)](vzvirtualmachinedelegate/guestdidstop(_:).md)
  Tells the delegate that the guest operating system stopped the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate/virtualmachine(_:didstopwitherror:))*