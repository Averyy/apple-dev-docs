# section_64

**Framework**: Kernel  
**Kind**: tag

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct section_64 {
    ...
};
```

## Topics

### Instance Properties
- [addr](section_64/1525838-addr.md)
- [align](section_64/1525433-align.md)
- [flags](section_64/1525294-flags.md)
- [nreloc](section_64/1525232-nreloc.md)
- [offset](section_64/1525537-offset.md)
- [reloff](section_64/1525855-reloff.md)
- [reserved1](section_64/1525306-reserved1.md)
- [reserved2](section_64/1525350-reserved2.md)
- [reserved3](section_64/1525889-reserved3.md)
- [sectname](section_64/1525885-sectname.md)
- [segname](section_64/1525275-segname.md)
  A string specifying the name of the segment that should eventually contain this section. For compactness, intermediate object files—files of type `MH_OBJECT`—contain only one segment, in which all sections are placed. The static linker places each section in the named segment when building the final product (any file that is not of type `MH_OBJECT`).
- [size](section_64/1525835-size.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/section_64)*