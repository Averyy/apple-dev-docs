# initialRamdiskURL

**Framework**: Virtualization  
**Kind**: property

The location of an optional RAM disk, which the boot loader maps into memory before it boots the Linux kernel.

**Availability**:
- macOS 11.0+

## Declaration

```swift
var initialRamdiskURL: URL? { get set }
```

#### Discussion

The default value of this property is `nil`. If you want specific files to be available when your Linux kernel boots, provide a URL to a valid RAM disk file in this property.

## See Also

- [var commandLine: String](vzlinuxbootloader/commandline.md)
  The command-line parameters to pass to the Linux kernel at boot time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzlinuxbootloader/initialramdiskurl)*