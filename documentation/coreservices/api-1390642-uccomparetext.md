# UCCompareText(_:_:_:_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Uses locale-specific collation information to compare Unicode strings.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCCompareText(_ collatorRef: CollatorRef!, _ text1Ptr: UnsafePointer<UniChar>!, _ text1Length: Int, _ text2Ptr: UnsafePointer<UniChar>!, _ text2Length: Int, _ equivalent: UnsafeMutablePointer<DarwinBoolean>!, _ order: UnsafeMutablePointer<Int32>!) -> OSStatus
```

#### Return_value

A result code.  The function can return `paramErr` (for example, if `collatorRef`, `text1Ptr`, or `text2Ptr` are `NULL`.

#### Discussion

You can use the `UCCompareText` function to perform various types of string comparison for a given set of locale and collation specifications. You can

-  simply test whether two strings are equivalent 
-  determine the relative ordering of two strings 
-  check whether a given string is equivalent to any string in an ordered list 

You can also call the `UCCompareText` function multiple times to compare different strings using the same collator object. If you wish to compare the same strings several times, as when sorting a list of strings, it may be more efficient for you to derive a collation key for each string and then compare the collation keys. For more on comparison using collation keys, see the functions  [`UCGetCollationKey(_:_:_:_:_:_:)`](1390468-ucgetcollationkey.md)  and  [`UCCompareCollationKeys(_:_:_:_:_:_:)`](1390378-uccomparecollationkeys.md). 

## Parameters

- `collatorRef`: A valid reference to a collator object;   is not allowed. You can use the function   to obtain a collator reference. 
- `text1Ptr`: A pointer to the first Unicode string (a   array) to compare. 
- `text1Length`: The total count of Unicode characters in the first string being compared. 
- `text2Ptr`: A pointer to the second Unicode string to compare.
- `text2Length`: The total count of Unicode characters in the second string being compared.
- `equivalent`: A pointer to a   value or  . On return,   produces a value of   if the strings are equivalent for the options you have specified in the collator object. If you wish simply to sort a list of strings in order, using your specified options, you can pass   for the   parameter and only use the   parameter’s result. In this case, all available comparison criteria are used to put the strings in a deterministic order, even if they are considered “equivalent” for the options you have specified. Note that you can set either the   or the   parameters to  , but not both. 
- `order`: A pointer to a signed, 32-bit integer value, or pass  . If you wish simply to test strings for equivalence, using your specified options (which can be much faster than determining ordering), you can pass   for the   parameter and only use the   parameter’s result. (Note that either the   or the   parameters may be  , but not both. 

## See Also

- [func UCCreateCollator(LocaleRef!, LocaleOperationVariant, UCCollateOptions, UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390403-uccreatecollator.md)
  Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.
- [func UCGetCollationKey(CollatorRef!, UnsafePointer<UniChar>!, Int, Int, UnsafeMutablePointer<Int>!, UnsafeMutablePointer<UCCollationValue>!) -> OSStatus](1390468-ucgetcollationkey.md)
  Uses locale-specific collation information to generate a collation key for a Unicode string.
- [func UCCompareCollationKeys(UnsafePointer<UCCollationValue>!, Int, UnsafePointer<UCCollationValue>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390378-uccomparecollationkeys.md)
  Uses collation keys to compare Unicode strings.
- [func UCDisposeCollator(UnsafeMutablePointer<CollatorRef?>!) -> OSStatus](1390435-ucdisposecollator.md)
  Disposes a collator object.
- [func UCCompareTextDefault(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390472-uccomparetextdefault.md)
  Uses the default system locale to compare Unicode strings.
- [func UCCompareTextNoLocale(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390513-uccomparetextnolocale.md)
  Uses a fixed, locale-insensitive order to compare Unicode strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390642-uccomparetext)*