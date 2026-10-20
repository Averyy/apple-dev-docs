# OSUnserializeBinary

**Framework**: Kernel  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.12+

## Declaration

```c
OSObjectPtr OSUnserializeBinary(const void *buffer, size_t bufferSize);
```

```c
OSPtr<OSObject> OSUnserializeBinary(const char *buffer, size_t bufferSize, OSString **errorString);
```

## See Also

### Serialization
- [OSUnserialize](./api-1584516-osunserialize.md)
- [OSUnserializeXML](./api-1584515-osunserializexml.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/1575008-osunserializebinary)*