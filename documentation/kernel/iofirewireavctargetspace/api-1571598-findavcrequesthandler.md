# findAVCRequestHandler

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn findAVCRequestHandler(IOFireWireAVCProtocolUserClient *userClient, UInt32 generation, UInt16 nodeID, IOFWSpeed speed, UInt32 handlerSearchIndex, const char *pCmdBuf, UInt32 cmdLen);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace/1571598-findavcrequesthandler)*