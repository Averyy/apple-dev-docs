# restoreImageURL

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The restore image URL used to initialize this installer.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var restoreImageURL: URL { get }
```

```objc
@property (readonly) NSURL * restoreImageURL;
```

## See Also

### Getting Information About an Installation
- [var progress: Progress](./progress.md)
  A progress object that you can use to observe or cancel an installation.
- [var virtualMachine: VZVirtualMachine](./virtualmachine.md)
  The virtual machine used to initialize this installer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/restoreimageurl)*