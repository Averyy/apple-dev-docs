# IOConnectCallAsyncScalarMethod(_:_:_:_:_:_:_:_:_:)

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

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

```c
kern_return_t IOConnectCallAsyncScalarMethod(mach_port_t connection, uint32_t selector, mach_port_t wake_port, uint64_t *reference, uint32_t referenceCnt, const uint64_t *input, uint32_t inputCnt, uint64_t *output, uint32_t *outputCnt);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514884-ioconnectcallasyncscalarmethod)*