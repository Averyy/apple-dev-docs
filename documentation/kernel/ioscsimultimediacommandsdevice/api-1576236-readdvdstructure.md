# ReadDVDStructure

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn ReadDVDStructure(IOMemoryDescriptor *buffer, const UInt32 length, const UInt8 structureFormat, const UInt32 logicalBlockAddress, const UInt8 layer, const UInt8 agid);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioscsimultimediacommandsdevice/1576236-readdvdstructure)*