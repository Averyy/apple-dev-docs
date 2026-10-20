# guestDidStop(_:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the guest operating system stopped the VM.

**Availability**:
- macOS 11.0+

## Declaration

```swift
optional func guestDidStop(_ virtualMachine: VZVirtualMachine)
```

```objc
- (void) guestDidStopVirtualMachine:(VZVirtualMachine *) virtualMachine;
```

## Parameters

- `virtualMachine`: The VM that called the delegate method.

## See Also

### Stopping the VM
- [func virtualMachine(VZVirtualMachine, didStopWithError: any Error)](./virtualmachine%28_,didstopwitherror%29.md)
  Tells the delegate that the VM stopped because of an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate/guestdidstop(_:))*