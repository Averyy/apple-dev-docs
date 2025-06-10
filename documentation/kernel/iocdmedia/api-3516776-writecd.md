# writeCD

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual IOReturn writeCD(IOService *client, UInt64 byteStart, IOMemoryDescriptor *buffer, CDSectorArea sectorArea, CDSectorType sectorType, IOStorageAttributes *attributes, UInt64 *actualByteCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iocdmedia/3516776-writecd)*