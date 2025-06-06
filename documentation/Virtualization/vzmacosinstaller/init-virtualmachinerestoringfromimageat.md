# init(virtualMachine:restoringFromImageAt:)

**Framework**: Virtualization  
**Kind**: init

Creates a macOS installer object.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(virtualMachine: VZVirtualMachine, restoringFromImageAt restoreImageFileURL: URL)
```

## Parameters

- `virtualMachine`: The virtual machine to install the operating system on.
- `restoreImageFileURL`: A file URL that indicates the macOS restore image to install.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/init(virtualmachine:restoringfromimageat:))*