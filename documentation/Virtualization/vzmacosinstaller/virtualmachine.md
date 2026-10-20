# virtualMachine

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The virtual machine used to initialize this installer.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var virtualMachine: VZVirtualMachine { get }
```

```objc
@property (readonly) VZVirtualMachine * virtualMachine;
```

## See Also

### Getting Information About an Installation
- [var progress: Progress](./progress.md)
  A progress object that you can use to observe or cancel an installation.
- [var restoreImageURL: URL](./restoreimageurl.md)
  The restore image URL used to initialize this installer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/virtualmachine)*