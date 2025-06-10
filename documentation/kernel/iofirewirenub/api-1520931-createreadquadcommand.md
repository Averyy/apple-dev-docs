# createReadQuadCommand

**Framework**: Kernel  
**Kind**: instm

**Availability**:
- macOS 10.11.4+

## Declaration

```swift
virtual IOFWReadQuadCommand * createReadQuadCommand(FWAddress devAddress, UInt32 *quads, int numQuads, FWDeviceCallback completion, void *refcon, bool failOnReset);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/iofirewirenub/1520931-createreadquadcommand)*