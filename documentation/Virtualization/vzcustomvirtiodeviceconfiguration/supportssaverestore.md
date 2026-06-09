# supportsSaveRestore

**Framework**: Virtualization  
**Kind**: property

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var supportsSaveRestore: Bool { get set }
```

#### Discussion

Whether the device supports save/restore.

This property defaults to `NO`. Set to `YES` if the device supports save/restore. If `supportsSaveRestore` is `YES` but the delegate set on `VZCustomVirtioDevice` does not actually implement the save/restore methods, an exception will be raised.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzcustomvirtiodeviceconfiguration/supportssaverestore)*