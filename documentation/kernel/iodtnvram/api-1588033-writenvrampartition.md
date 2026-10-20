# writeNVRAMPartition

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn writeNVRAMPartition(const OSSymbol *partitionID, IOByteCount offset, uint8_t *buffer, IOByteCount length);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iodtnvram/1588033-writenvrampartition)*