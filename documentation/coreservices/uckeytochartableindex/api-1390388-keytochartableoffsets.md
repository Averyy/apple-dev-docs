# keyToCharTableOffsets

**Framework**: Core Services  
**Kind**: structp  
**Role**: Instance Property

An array of offsets from the beginning of the `'uchr'` resource to each of the `UCKeyOutput` key-code-to-character tables in the `keyToCharData[]` array that follows this structure in the resource.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keyToCharTableOffsets: UInt32
```

```c
UInt32 keyToCharTableOffsets[1];
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uckeytochartableindex/1390388-keytochartableoffsets)*