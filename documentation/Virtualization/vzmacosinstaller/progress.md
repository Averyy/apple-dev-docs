# progress

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

A progress object that you can use to observe or cancel an installation.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var progress: Progress { get }
```

```objc
@property (readonly) NSProgress * progress;
```

## Mentions

- [Installing macOS on a Virtual Machine](../installing-macos-on-a-virtual-machine.md)

#### Discussion

Canceling the progress object before starting an installation raises an exception.

## See Also

### Getting Information About an Installation
- [var restoreImageURL: URL](./restoreimageurl.md)
  The restore image URL used to initialize this installer.
- [var virtualMachine: VZVirtualMachine](./virtualmachine.md)
  The virtual machine used to initialize this installer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzmacosinstaller/progress)*