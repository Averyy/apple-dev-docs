# readCD

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual void readCD(IOService *client, UInt64 byteStart, IOMemoryDescriptor *buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes *attributes, IOStorageCompletion *completion);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/1581373-readcd)*