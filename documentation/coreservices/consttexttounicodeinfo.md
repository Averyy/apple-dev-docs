# ConstTextToUnicodeInfo

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a constant text to Unicode converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef const TextToUnicodeInfo ConstTextToUnicodeInfo;
```

#### Discussion

The  [`TruncateForTextToUnicode`](./api-1433518-truncatefortexttounicode.md) function requires a Unicode converter object as a parameter. This function does not modify the contents of the private structure to which the Unicode converter object refers, so it uses the constant Unicode converter object defined by the `ConstTextToUnicodeInfo` data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/consttexttounicodeinfo)*