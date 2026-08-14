# withString

**Framework**: Kernel  
**Kind**: clm

Allocates an OSString object with a copy of an OString object.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

## Declaration

```swift
static OSPtr<OSString> withString(const OSString *aString);
```

#### Return_value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

#### Discussion

Allocates an OSString object with a copy of an OString object.

## Parameters

- `aString`: OSString object to copy from. The string will be copied at the time of the call.

## See Also

- [+ withCString](osstring/3180977-withcstring.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withCString](osstring/3433854-withcstring.md)
  Allocates an OSString object with a copy of a c-string, up to a given length.
- [+ withCStringNoCopy](osstring/3180978-withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [- free](osstring/3180973-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3180979-withstring)*