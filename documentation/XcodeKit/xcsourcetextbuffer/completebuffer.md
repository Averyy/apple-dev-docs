# completeBuffer

**Framework**: XcodeKit  
**Kind**: property  
**Role**: Instance Property

The complete buffer’s string representation.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var completeBuffer: String { get set }
```

```objc
@property (copy) NSString * completeBuffer;
```

#### Discussion

Changes to the `lines` property are immediately reflected in this property, and vice versa.

## See Also

### Accessing Source Text
- [var contentUTI: String](./contentuti.md)
  The Uniform Type Identifier (UTI) of the content in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcodekit/xcsourcetextbuffer/completebuffer)*