# vn_bwrite

**Framework**: Kernel  
**Kind**: func

System-provided implementation of "bwrite" vnop.

**Availability**:
- macOS 10.4+

## Declaration

```swift
int vn_bwrite(struct vnop_bwrite_args *ap);
```

#### Return_value

Results of buf_bwrite directly.

#### Discussion

This routine is available for filesystems which do not want to implement their own "bwrite" vnop. It just calls buf_bwrite() without modifying its arguments.

## Parameters

- `ap`: Standard parameters to a bwrite vnop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1562107-vn_bwrite)*