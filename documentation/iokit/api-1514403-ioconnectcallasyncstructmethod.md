# IOConnectCallAsyncStructMethod(_:_:_:_:_:_:_:_:_:)

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
func IOConnectCallAsyncStructMethod(_ connection: mach_port_t, _ selector: UInt32, _ wake_port: mach_port_t, _ reference: UnsafeMutablePointer<UInt64>!, _ referenceCnt: UInt32, _ inputStruct: UnsafeRawPointer!, _ inputStructCnt: Int, _ outputStruct: UnsafeMutableRawPointer!, _ outputStructCnt: UnsafeMutablePointer<Int>!) -> kern_return_t
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1514403-ioconnectcallasyncstructmethod)*