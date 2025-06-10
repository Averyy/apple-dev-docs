# segname

**Framework**: Kernel  
**Kind**: structp

A string specifying the name of the segment that should eventually contain this section. For compactness, intermediate object files—files of type `MH_OBJECT`—contain only one segment, in which all sections are placed. The static linker places each section in the named segment when building the final product (any file that is not of type `MH_OBJECT`).

**Availability**:
- macOS 10.6+

## Declaration

```swift
char segname[16];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/section_64/1525275-segname)*