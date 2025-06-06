# capturesSystemKeys

**Framework**: Virtualization  
**Kind**: property

A Boolean value that determines whether the system should send certain system keyboard shortcuts to the guest instead of the host.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
var capturesSystemKeys: Bool { get set }
```

#### Discussion

Defaults to `false.`

## See Also

- [var automaticallyReconfiguresDisplay: Bool](vzvirtualmachineview/automaticallyreconfiguresdisplay.md)
  A Boolean value that indicates whether the graphics display associated with this view automatically reconfigures with respect to view changes.
- [var virtualMachine: VZVirtualMachine?](vzvirtualmachineview/virtualmachine.md)
  The VM to display in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview/capturessystemkeys)*