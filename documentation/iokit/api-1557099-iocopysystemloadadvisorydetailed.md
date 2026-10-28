# IOCopySystemLoadAdvisoryDetailed

**Framework**: IOKit  
**Kind**: func  
**Role**: Function

Indicates how user activity, battery level, and thermal level each contribute to the overall "SystemLoadAdvisory" level. In the future, this combined level may represent new levels as well.

**Availability**:
- Mac Catalyst 18.4+
- macOS 10.6+

## Declaration

```c
CFDictionaryRef IOCopySystemLoadAdvisoryDetailed(void);
```

## Return Value

Returns a CFDictionaryRef, or NULL on error. Caller must release the returned dictionary.

## Discussion

See dictionary keys defined above.

## See Also

### IOSystemLoadAdvisory
- [IOGetSystemLoadAdvisory](./api-1557110-iogetsystemloadadvisory.md)
  Returns a hint about whether now would be a good time to perform time-insensitive work.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iokit/1557099-iocopysystemloadadvisorydetailed)*