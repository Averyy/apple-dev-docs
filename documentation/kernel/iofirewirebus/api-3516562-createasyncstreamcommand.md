# createAsyncStreamCommand

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.15.2+

## Declaration

```swift
virtual IOFWAsyncStreamCommand * createAsyncStreamCommand(UInt32 generation, UInt32 channel, UInt32 sync, UInt32 tag, IOMemoryDescriptor *hostMem, UInt32 size, int speed, FWAsyncStreamCallback completion, void *refcon, bool failOnReset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirebus/3516562-createasyncstreamcommand)*