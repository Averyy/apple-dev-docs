# commandLine

**Framework**: Virtualization  
**Kind**: property  
**Role**: Instance Property

The command-line parameters to pass to the Linux kernel at boot time.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var commandLine: String { get set }
```

```objc
@property (copy) NSString * commandLine;
```

#### Discussion

For information about the parameters you can pass to a Linux kernel, see “[The kernel’s command-line parameters](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html)”.

## See Also

### Configuring the boot parameters
- [var initialRamdiskURL: URL?](./initialramdiskurl.md)
  The location of an optional RAM disk, which the boot loader maps into memory before it boots the Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxbootloader/commandline)*