# setGammaTable

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn setGammaTable(UInt32 channelCount, UInt32 dataCount, UInt32 dataWidth, void *data);
```

```cpp
virtual IOReturn setGammaTable(UInt32 channelCount, UInt32 dataCount, UInt32 dataWidth, void *data, bool syncToVBL);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/ioframebuffer/1397522-setgammatable)*