# installAVCCommandHandler

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn installAVCCommandHandler(IOFireWireAVCProtocolUserClient *userClient, IOFireWireAVCTargetCommandHandlerCallback callBack, OSAsyncReference64 asyncRef, UInt32 subUnitTypeAndID, UInt32 opCode, uint64_t userCallBack, uint64_t userRefCon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace/1571622-installavccommandhandler)*