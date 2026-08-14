# withCStringNoCopy

**Framework**: Kernel  
**Kind**: clm

Allocates an OSString object with a copy of a c-string.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSString> withCStringNoCopy(const char *cString);
```

#### Return_value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSString object with a copy of a c-string. A synonym for OSString::withCString() for compatibility with kernel code.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.

## See Also

- [+ withCString](osstring/3180977-withcstring.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withCString](osstring/3433854-withcstring.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [+ withString](osstring/3180979-withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [- free](osstring/3180973-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180978-withcstringnocopy)*