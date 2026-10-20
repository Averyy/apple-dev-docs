# withCString

**Framework**: Kernel  
**Kind**: clm  
**Role**: Type Method

Allocates an OSString object with a copy of a c-string, up to a given length.

**Availability**:
- DriverKit 19.0+
- macOS 12.0+

## Declaration

*DriverKit*

```c
static OSStringPtr withCString(const char *cString, size_t length);
```

*macOS*

```c
static OSPtr<OSString> withCString(const char *cString, size_t length);
```

#### Return Value

NULL on failure, otherwise the allocated OSString with reference count 1 to be released by the caller.

## Parameters

- `cString`: Pointer to null terminated c-string. The string will be copied at the time of the call.
- `length`: Maximum length of the string to copy.

## See Also

### Creating a String
- [+ withCString](./api-3180977-withcstring.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withCStringNoCopy](./api-3180978-withcstringnocopy.md)
  Allocates an OSString object with a copy of a c-string.
- [+ withString](./api-3180979-withstring.md)
  Allocates an OSString object with a copy of an OString object.
- [- free](./api-3180973-free.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/osstring/3433854-withcstring)*