# ConstUnicodeMappingPtr

**Framework**: Core Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a constant Unicode mapping pointer.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
typedef const UnicodeMapping *ConstUnicodeMappingPtr;
```

#### Discussion

Many Unicode Converter functions take a pointer to a Unicode mapping structure as a parameter. For functions that do not modify the Unicode mapping contents, the Unicode Converter provides a constant pointer to a Unicode mapping structure defined by the `ConstUnicodeMappingPtr` data type. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/constunicodemappingptr)*