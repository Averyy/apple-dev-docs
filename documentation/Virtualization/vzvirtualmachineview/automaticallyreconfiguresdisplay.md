# automaticallyReconfiguresDisplay

**Framework**: Virtualization  
**Kind**: property

A Boolean value that indicates whether the graphics display associated with this view automatically reconfigures with respect to view changes.

**Availability**:
- macOS 14.0+

## Declaration

```swift
@MainActor
var automaticallyReconfiguresDisplay: Bool { get set }
```

#### Discussion

Set this property to [`true`](https://developer.apple.com/documentation/Swift/true) to automatically resize or reconfigure this graphics display when the view properties update. For example, resizing the display when the view has a live resize operation. When enabled, the graphics display automatically reconfigures to match the host display environment.

You can set this property on only a single [`VZVirtualMachineView`](vzvirtualmachineview.md) targeting a particular [`VZGraphicsDisplay`](vzgraphicsdisplay.md) at a time. If multiple `VZVirtualMachineView` views targeting the same VZGraphicsDisplay enable this property, only one view respects the property, and the framework disables the property on the other views.

The default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var capturesSystemKeys: Bool](vzvirtualmachineview/capturessystemkeys.md)
  A Boolean value that determines whether the system should send certain system keyboard shortcuts to the guest instead of the host.
- [var virtualMachine: VZVirtualMachine?](vzvirtualmachineview/virtualmachine.md)
  The VM to display in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzvirtualmachineview/automaticallyreconfiguresdisplay)*