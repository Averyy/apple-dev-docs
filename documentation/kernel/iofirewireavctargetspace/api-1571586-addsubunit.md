# addSubunit

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOReturn addSubunit(IOFireWireAVCProtocolUserClient *userClient, IOFireWireAVCSubunitPlugHandlerCallback callBack, OSAsyncReference64 asyncRef, UInt32 subunitType, UInt32 numSourcePlugs, UInt32 numDestPlugs, uint64_t userCallBack, uint64_t userRefCon, UInt32 *subUnitID);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewireavctargetspace/1571586-addsubunit)*