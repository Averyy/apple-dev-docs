# createCompareAndSwapCommand

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOFWCompareAndSwapCommand * createCompareAndSwapCommand(FWAddress devAddress, const UInt32 *cmpVal, const UInt32 *newVal, int size, FWDeviceCallback completion, void *refcon, bool failOnReset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirenub/1520925-createcompareandswapcommand)*