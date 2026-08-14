# withCString

**Framework**: Kernel  
**Kind**: clm

Allocates an OSString object with a copy of a c-string.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSString> withCString(const char *cString);
```

#### Return_value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.

## See Also

- [+ withCString](osstring/3433854-withcstring.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [+ withCStringNoCopy](osstring/3180978-withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withString](osstring/3180979-withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [- free](osstring/3180973-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180977-withcstring)*