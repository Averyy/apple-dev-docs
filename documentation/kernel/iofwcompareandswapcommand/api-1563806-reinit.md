# reinit

**Framework**: Kernel  
**Kind**: instm  
**Role**: Instance Method

**Availability**:
- macOS 10.11.4+

## Declaration

```cpp
virtual IOReturn reinit(FWAddress devAddress, const UInt32 *cmpVal, const UInt32 *newVal, int size, FWDeviceCallback completion, void *refcon, bool failOnReset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofwcompareandswapcommand/1563806-reinit)*