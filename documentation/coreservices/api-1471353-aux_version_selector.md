# AUX Version Selector

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specifies version information for A/UX.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltAUXVersion](./api-1471353-aux_version_selector/gestaltauxversion.md)
  The version of A/UX if it is currently executing. The result is placed into the low-order word of the response parameter. If A/UX is not executing, the `Gestalt` function returns `gestaltUnknownErr`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1471353-aux_version_selector)*