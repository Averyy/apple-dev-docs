# delegate

**Framework**: Virtualization  
**Kind**: property

A custom object you use to determine when the VM stops.

**Availability**:
- macOS 11.0+

## Declaration

```swift
weak var delegate: (any VZVirtualMachineDelegate)? { get set }
```

## See Also

- [protocol VZVirtualMachineDelegate](vzvirtualmachinedelegate.md)
  The methods you use to respond to changes in the state of the VM.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachine/delegate)*