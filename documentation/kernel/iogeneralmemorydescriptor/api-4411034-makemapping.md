# makeMapping

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 14.5+

## Declaration

```swift
virtual IOMemoryMap * makeMapping(IOMemoryDescriptor *owner, task_t intoTask, IOVirtualAddress atAddress, IOOptionBits options, IOByteCount offset, IOByteCount length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iogeneralmemorydescriptor/4411034-makemapping)*