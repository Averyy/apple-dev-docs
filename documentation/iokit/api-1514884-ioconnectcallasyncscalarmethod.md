# IOConnectCallAsyncScalarMethod(_:_:_:_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- visionOS 1.0+

## Declaration

```swift
func IOConnectCallAsyncScalarMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>!, _ referenceCnt: UInt32, _ input: UnsafePointer<UInt64>!, _ inputCnt: UInt32, _ output: UnsafeMutablePointer<UInt64>!, _ outputCnt: UnsafeMutablePointer<UInt32>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514884-ioconnectcallasyncscalarmethod)*