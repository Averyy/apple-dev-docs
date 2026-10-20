# createWriteCommand

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOFWWriteCommand * createWriteCommand(FWAddress devAddress, IOMemoryDescriptor *hostMem, FWDeviceCallback completion, void *refcon, bool failOnReset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirenub/1520893-createwritecommand)*