# virtualMachine(_:didStopWithError:)

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the VM stopped because of an error.

**Availability**:
- macOS 11.0+

## Declaration

```swift
optional func virtualMachine(_ virtualMachine: VZVirtualMachine, didStopWithError error: any Error)
```

```objc
- (void) virtualMachine:(VZVirtualMachine *) virtualMachine didStopWithError:(NSError *) error;
```

## Parameters

- `virtualMachine`: The VM that called the delegate method.
- `error`: The error.

## See Also

### Stopping the VM
- [func guestDidStop(VZVirtualMachine)](./guestdidstop%28_%29.md)
  Tells the delegate that the guest operating system stopped the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachinedelegate/virtualmachine(_:didstopwitherror:))*