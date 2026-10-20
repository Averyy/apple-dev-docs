# CreateSubMemoryDescriptor

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

**Availability**:
- DriverKit 20.0+
- macOS 11.0+

## Declaration

```c
static kern_return_t CreateSubMemoryDescriptor(uint64_t memoryDescriptorCreateOptions, uint64_t offset, uint64_t length, IOMemoryDescriptor *ofDescriptor, IOMemoryDescriptor **memory);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iomemorydescriptor/3674611-createsubmemorydescriptor)*