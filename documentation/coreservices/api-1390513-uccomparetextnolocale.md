# UCCompareTextNoLocale(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Uses a fixed, locale-insensitive order to compare Unicode strings.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCCompareTextNoLocale(_ options: UCCollateOptions, _ text1Ptr: UnsafePointer<UniChar>!, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>!, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus
```

#### Return_value

A result code. This function can return `paramErr` if you pass an invalid value for one of the parameters. For example, if you pass `0` for the `options` paramter, the function returns `paramErr`.

#### Discussion

You can call the `UCCompareTextNoLocale` function when you want to perform a fixed, locale-insensitive comparison that is guaranteed not to change from one system release to the next. This type of comparison could be used for sorting a Unicode key string in a database, for example. The `UCCompareTextNoLocale` function can provide comparison according to various fixed ordering schemes (only one is supported for Mac OS 8.6 and 9.0). This type of comparison is not usually used for a user-visible ordering, so the ordering schemes need not match any user’s expectation of a sensible collation order.

The `UCCompareTextNoLocale` function does not require a collator object or collation keys. Another advantage of `UCCompareTextNoLocale` on Mac OS 9 is that it is exported from the `UnicodeUtilitiesCoreLib` library, which does not depend on other libraries (the other comparison functions exported from `UnicodeUtilitiesLib`, which depends on `LocalesLib` and `TextCommon`). 

## Parameters

- `options`: A   value specifying the fixed ordering scheme to use for the string comparison. This value must be nonzero. Bits 24-31 of   specify which fixed ordering scheme to use. Currently there is only scheme— . See   for additional details. 
- `text1Ptr`: A pointer to the first Unicode string (a   array) to compare. 
- `text1Length`: The total count of Unicode characters in the first string being compared. 
- `text2Ptr`: A pointer to the second Unicode string to compare.
- `text2Length`: The total count of Unicode characters in the second string being compared.
- `equivalent`: A pointer to a   value or pass  . On return,   produces a value of   if the strings are equivalent for the ordering scheme you have specified. If you wish simply to sort a list of strings in order, using the specified ordering scheme, you can pass   for the   parameter and only use the   parameter’s result. In this case, all available comparison criteria are used to put the strings in a deterministic order, even if they are considered “equivalent” for the specified ordering scheme. Note that you can set either the   or the   parameters to  , but not both. 
- `order`: A pointer to a signed, 32-bit integer value, or pass  . If you wish simply to test the strings for equivalence, using the specified ordering scheme (which can be much faster than determining ordering), you can pass   for the   parameter and only use the   parameter’s result. (Note that either the   or the   parameters may be  , but not both. 

## See Also

- [func UCCreateCollator(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390403-uccreatecollator.md)
  Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.
- [func UCCompareText(CollatorRef!, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390642-uccomparetext.md)
  Uses locale-specific collation information to compare Unicode strings.
- [func UCGetCollationKey(CollatorRef!, UnsafePointer<UniChar>!, Int, Int, UnsafeMutablePointer<Int>!, UnsafeMutablePointer<UCCollationValue>!) -> OSStatus](1390468-ucgetcollationkey.md)
  Uses locale-specific collation information to generate a collation key for a Unicode string.
- [func UCCompareCollationKeys(UnsafePointer<UCCollationValue>!, Int, UnsafePointer<UCCollationValue>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390378-uccomparecollationkeys.md)
  Uses collation keys to compare Unicode strings.
- [func UCDisposeCollator(UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390435-ucdisposecollator.md)
  Disposes a collator object.
- [func UCCompareTextDefault(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390472-uccomparetextdefault.md)
  Uses the default system locale to compare Unicode strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390513-uccomparetextnolocale)*