# makeMapping

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOMemoryMap * makeMapping(IOMemoryDescriptor *owner, task_t intoTask, IOVirtualAddress atAddress, IOOptionBits options, IOByteCount offset, IOByteCount length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iosubmemorydescriptor/1571790-makemapping)*