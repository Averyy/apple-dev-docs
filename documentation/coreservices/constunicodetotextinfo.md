# ConstUnicodeToTextInfo

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a constant Unicode to text converter object.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef const UnicodeToTextInfo ConstUnicodeToTextInfo;
```

## Discussion

The [`TruncateForUnicodeToText`](./api-1433649-truncateforunicodetotext.md) function requires a Unicode converter object as a parameter. This function does not modify the contents of the private structure to which the Unicode converter object refers, so it uses the constant Unicode converter object defined by the `ConstUnicodeToTextInfo` data type. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/constunicodetotextinfo)*