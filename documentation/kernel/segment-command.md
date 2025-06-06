# segment_command

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct segment_command {
    ...
};
```

## Topics

### Instance Properties
- [cmd](segment_command/1525326-cmd.md)
  Common to all load command structures. Set to `LC_SEGMENT` for this structure.
- [cmdsize](segment_command/1525493-cmdsize.md)
- [fileoff](segment_command/1525429-fileoff.md)
  Indicates the offset in this file of the data to be mapped at `vmaddr`.
- [filesize](segment_command/1525609-filesize.md)
- [flags](segment_command/1525271-flags.md)
- [initprot](segment_command/1525260-initprot.md)
- [maxprot](segment_command/1525877-maxprot.md)
- [nsects](segment_command/1525814-nsects.md)
- [segname](segment_command/1525506-segname.md)
- [vmaddr](segment_command/1525654-vmaddr.md)
- [vmsize](segment_command/1525419-vmsize.md)
  Indicates the number of bytes of virtual memory occupied by this segment. See also the description of `filesize`, below.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/segment_command)*