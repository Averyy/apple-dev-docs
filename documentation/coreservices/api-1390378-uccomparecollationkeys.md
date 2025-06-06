# UCCompareCollationKeys(_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Uses collation keys to compare Unicode strings.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCCompareCollationKeys(_ key1Ptr: UnsafePointer<UCCollationValue>!, _ key1Length: Int, _ key2Ptr: UnsafePointer<UCCollationValue>!, _ key2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus
```

#### Return_value

A result code.  This function can return `paramErr`, for example, if `key1Ptr` or `key2Ptr` are `NULL`.

#### Discussion

If you wish to compare the same strings several times, as when sorting a list of strings, it may be most efficient for you to derive a collation key for each string and then compare the collation keys. A collation key is a transformation of the string that depends on the collator object (that is, it depends on the locale, the collation variant if any, and the collation options).

Collation keys that are generated using the same collator object—but for different strings—can quickly be compared with each other, without further reference to the collator object or collation tables. The disadvantage is that the collation keys may be rather large. After you use the function  [`UCGetCollationKey(_:_:_:_:_:_:)`](1390468-ucgetcollationkey.md)  to create a collation key from a given string and collator object, you can call the `UCCompareCollationKeys` function to compare two collation keys that were generated with the same collator object.

If you are comparing different strings, it may be more efficient for you to call the function  [`UCCompareText(_:_:_:_:_:_:_:)`](1390642-uccomparetext.md)  multiple times using the same collator object. 

Note that collation keys should be used only in a runtime context. They should not be stored in a persistent state (such as to disk) because the format of a collation key could change in the future.

## Parameters

- `key1Ptr`: A pointer to the collation key (a   array) for the first string to compare. You can obtain a collation key with the function  . The collation key supplied in   for the first string must be generated with the same collator object as that used to generate the collation key supplied in   for the second string. 
- `key1Length`: An   value specifying the actual length of the collation key supplied in the   parameter. You can obtain this value from the function   when you obtain the new collation key. 
- `key2Ptr`: A pointer to the collation key (a   array) for the second string to compare. You can obtain a collation key with the function  . The collation key supplied in   for the second string must be generated with the same collator object as that used to generate the collation key supplied in   for the first string.
- `key2Length`: An   value specifying the actual length of the collation key supplied in the   parameter. You can obtain this value from the function   when you obtain the new collation key.
- `equivalent`: A pointer to a   value or pass  . On return,   produces a value of   if the strings represented by the collation keys are equivalent for the options you have specified in the collator object. If you wish simply to sort a list of strings in order, using your specified options, you can pass   for the   parameter and only use the   parameter’s result. In this case, all available comparison criteria are used to put the strings in a deterministic order, even if they are considered “equivalent” for the options you have specified. Note that you can set either the   or the   parameters to  , but not both. 
- `order`: A pointer to a signed, 32-bit integer value, or pass  . If you wish simply to test the strings represented by the collation keys for equivalence, using your specified options (which can be much faster than determining ordering), you can pass   for the   parameter and only use the   parameter’s result. (Note that either the   or the   parameters may be  , but not both. 

## See Also

- [func UCCreateCollator(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390403-uccreatecollator.md)
  Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.
- [func UCCompareText(CollatorRef!, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390642-uccomparetext.md)
  Uses locale-specific collation information to compare Unicode strings.
- [func UCGetCollationKey(CollatorRef!, UnsafePointer<UniChar>!, Int, Int, UnsafeMutablePointer<Int>!, UnsafeMutablePointer<UCCollationValue>!) -> OSStatus](1390468-ucgetcollationkey.md)
  Uses locale-specific collation information to generate a collation key for a Unicode string.
- [func UCDisposeCollator(UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390435-ucdisposecollator.md)
  Disposes a collator object.
- [func UCCompareTextDefault(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390472-uccomparetextdefault.md)
  Uses the default system locale to compare Unicode strings.
- [func UCCompareTextNoLocale(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390513-uccomparetextnolocale.md)
  Uses a fixed, locale-insensitive order to compare Unicode strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390378-uccomparecollationkeys)*