# UCGetCollationKey(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Uses locale-specific collation information to generate a collation key for a Unicode string.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCGetCollationKey(_ collatorRef: CollatorRef!, _ textPtr: UnsafePointer<UniChar>!, _ textLength: Int, _ maxKeySize: Int, _ actualKeySize: UnsafeMutablePointer<Int>!, _ collationKey: UnsafeMutablePointer<UCCollationValue>!) -> OSStatus
```

#### Return_value

A result code.  The function can return `paramErr`, for example, if the parameters `collatorRef`, `textPtr`, `actualKeySize`, or `collationKey` are `NULL`. It can also return memory errors. If `maxKeySize` is too small for the collation key, the function returns `kUCOutputBufferTooSmall`.

#### Discussion

If you want to compare the same strings several times, as when sorting a list of strings, it may be most efficient for you to derive a collation key for each string and then compare the collation keys. A collation key is a transformation of the string that depends on the collator object (that is, it depends on the locale, the collation variant if any, and the collation options).

Collation keys that are generated using the same collator object—but for different strings—can quickly be compared with each other, without further reference to the collator object or collation tables. The disadvantage is that the collation keys may be rather large. After you use the `UCGetCollationKey` function to create a collation key from a given string and collator object, you can call the function  [`UCCompareCollationKeys(_:_:_:_:_:_:)`](1390378-uccomparecollationkeys.md)  to compare two collation keys that were generated with the same collator object.

If you are comparing different strings, it may be more efficient for you to call the function [`UCCompareText(_:_:_:_:_:_:_:)`](1390642-uccomparetext.md) multiple times using the same collator object. 

Note that collation keys should be used only in a runtime context. They should not be stored in a persistent state (such as to disk) because the format of a collation key could change in the future.

##### 1770074

This function can move memory.

## Parameters

- `collatorRef`: A valid reference to a collator object;   is not allowed. You can use the function   to obtain a collator reference. 
- `textPtr`: A pointer to the Unicode string (a   array) for which to generate a collation key. 
- `textLength`: The total count of Unicode characters in the string referenced by the   parameter. 
- `maxKeySize`: An   value specifying the length of the   array passed in the   parameter. This dimension should typically be at least  , as the byte length of a collation key is typically more than 16 times the number of Unicode characters in the string. 
- `actualKeySize`: On return, the actual length of the   array returned in the   parameter.
- `collationKey`: An array of   values. On return, the array contains the new collation key. The collation key consists of a sequence of primary weights for all of the collation text elements in the string, followed by a separator and a sequence of secondary weights for all of the text elements in the string, and so on for several levels of significance. The separator is usually 0; however, 1 is used as the separator at the boundary between levels that are significant and levels that are insignificant for the options you supply in the collator object. 

## See Also

- [func UCCreateCollator(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390403-uccreatecollator.md)
  Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.
- [func UCCompareText(CollatorRef!, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390642-uccomparetext.md)
  Uses locale-specific collation information to compare Unicode strings.
- [func UCCompareCollationKeys(UnsafePointer<UCCollationValue>!, Int, UnsafePointer<UCCollationValue>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390378-uccomparecollationkeys.md)
  Uses collation keys to compare Unicode strings.
- [func UCDisposeCollator(UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390435-ucdisposecollator.md)
  Disposes a collator object.
- [func UCCompareTextDefault(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390472-uccomparetextdefault.md)
  Uses the default system locale to compare Unicode strings.
- [func UCCompareTextNoLocale(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390513-uccomparetextnolocale.md)
  Uses a fixed, locale-insensitive order to compare Unicode strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390468-ucgetcollationkey)*