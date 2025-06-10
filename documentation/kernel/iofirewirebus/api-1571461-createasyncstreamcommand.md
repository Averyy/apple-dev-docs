# createAsyncStreamCommand

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOFWAsyncStreamCommand * createAsyncStreamCommand(UInt32 generation, UInt32 channel, UInt32 sync, UInt32 tag, IOMemoryDescriptor *hostMem, UInt32 size, int speed, FWAsyncStreamCallback completion, void *refcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirebus/1571461-createasyncstreamcommand)*