# UCCollationValue

**Framework**: Core Services  
**Kind**: tdef

Specifies a Unicode collation key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias UCCollationValue = UInt32
```

#### Discussion

Collation keys consist of an array of `UCCollationValue` values. The collation key consists of a sequence of primary weights for all of the collation text elements in the string, followed by a separator and a sequence of secondary weights for all of the text elements in the string, and so on for several levels of significance. The separator is usually 0; however, 1 is used as the separator at the boundary between levels that are significant and levels that are insignificant for the options you supply in the collator object. You can obtain a collation key with the function  [`UCGetCollationKey(_:_:_:_:_:_:)`](1390468-ucgetcollationkey.md).  


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uccollationvalue)*