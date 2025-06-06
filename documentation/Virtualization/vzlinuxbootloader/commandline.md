# commandLine

**Framework**: Virtualization  
**Kind**: property

The command-line parameters to pass to the Linux kernel at boot time.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var commandLine: String { get set }
```

#### Discussion

For information about the parameters you can pass to a Linux kernel, see “[`The kernel’s command-line parameters`](https://developer.apple.comhttps://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html)”.

## See Also

- [var initialRamdiskURL: URL?](vzlinuxbootloader/initialramdiskurl.md)
  The location of an optional RAM disk, which the boot loader maps into memory before it boots the Linux kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxbootloader/commandline)*