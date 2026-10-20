# HIShapeEnumerate(_:_:_:_:)

**Framework**: Application Services  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func HIShapeEnumerate(_ inShape: HIShape!, _ inOptions: OptionBits, _ inProc: HIShapeEnumerateProcPtr!, _ inRefcon: UnsafeMutableRawPointer!) -> OSStatus
```

```c
OSStatus HIShapeEnumerate(HIShapeRef inShape, OptionBits inOptions, HIShapeEnumerateProcPtr inProc, void *inRefcon);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1459161-hishapeenumerate)*