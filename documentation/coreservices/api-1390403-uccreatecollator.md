# UCCreateCollator(_:_:_:_:)

**Framework**: Core Services  
**Kind**: func

Creates an object encapsulating locale and collation information, for the purpose of performing Unicode string comparison.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func UCCreateCollator(_ locale: LocaleRef!, _ opVariant: LocaleOperationVariant, _ options: UCCollateOptions, _ collatorRef: UnsafeMutablePointer<CollatorRef?>!) -> OSStatus
```

#### Return_value

A result code.  The function can return memory errors and `paramErr`, for example, if the `collatorRef` parameter is `NULL`. It can also return resource errors in Mac OS 9 and CarbonLib.

#### Discussion

To perform Unicode string comparison, you must supply locale and collation specifications to a collation function such as  [`UCCompareText(_:_:_:_:_:_:_:)`](1390642-uccomparetext.md). You provide this information by means of a collator object, created via the `UCCreateCollator` function. When finished with the collator object, you dispose of it using the function  [`UCDisposeCollator(_:)`](1390435-ucdisposecollator.md). 

##### 1770072

The collator object is allocated in the current heap. This function can move memory.

## Parameters

- `locale`: A valid   representing a specific locale, or pass   to request the default system locale. You can supply the value   in the   parameter of the Locales Utilities functions   and   to obtain the locales available for collation on the current system. 
- `opVariant`: A   value identifying a collation variant within the locale specified in the   parameter. You can also pass 0 to request the default collation variant for any locale. To obtain the varieties of locale-specific collation that are currently available, you can supply the value   in the   parameter of the Locales Utilities functions   and  . 
- `options`: A   value specifying any collation options that you want to use for the string comparison. 
- `collatorRef`: A pointer to a value of type  . On return, the   value contains a valid reference to a new collator object. 

## See Also

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
- [func UCCompareTextNoLocale(UCCollateOptions, UnsafePointer<UniChar>!, Int, UnsafePointer<UniChar>!, Int, UnsafeMutablePointer<DarwinBoolean>!, UnsafeMutablePointer<Int32>!) -> OSStatus](1390513-uccomparetextnolocale.md)
  Uses a fixed, locale-insensitive order to compare Unicode strings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390403-uccreatecollator)*