# initWithData:

**Framework**: Virtualization  
**Kind**: method  
**Role**: Instance Method

Creates a signature from SHA-256 hash data.

**Availability**:
- macOS 27.0+

## Declaration

```objc
- (instancetype) initWithData:(NSData *) data;
```

## Discussion

The hash data must be exactly 32 bytes in length. If data isn’t exactly 32 bytes, the framework raises an exception.

## Parameters

- `data`: Data containing the SHA-256 hash.


---

*[View on Apple Developer](https://developer.apple.com/documentation/virtualization/vzefisignaturesha256hash/initwithdata:)*