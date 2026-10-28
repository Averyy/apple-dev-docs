# UCCreateTextBreakLocator

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Creates an object encapsulating locale and text-break information, for the purpose of finding boundaries in Unicode text.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use CFStringTokenizer (for locale-sensitive word, line, paragraph, and sentence breaks) and CFStringGetRangeOfComposedCharactersAtIndex (for cluster breaks) instead.

## Declaration

```c
OSStatus UCCreateTextBreakLocator(LocaleRef locale, LocaleOperationVariant opVariant, UCTextBreakType breakTypes, TextBreakLocatorRef *breakRef);
```

## Return Value

A result code.  The function can return memory errors and `paramErr` (for example, if the `breakRef` parameter is `NULL` or if invalid bits are set in the `breakTypes` parameter). It can also return resource errors in Mac OS 9 and CarbonLib.

## Discussion

To find boundaries in Unicode text, you must supply locale and text-break specifications to the function  [`UCFindTextBreak`](./api-1390429-ucfindtextbreak.md). You provide this information by means of a text-break locator object, created via the `UCCreateTextBreakLocator` function. When finished with the text-break locator object, you should dispose of it using the function  [`UCDisposeTextBreakLocator`](./api-1390419-ucdisposetextbreaklocator.md).

The `UCCreateTextBreakLocator` function creates a text-break locator object for a specified locale, a specified text-break variant within that locale, and a specified set of break types. The different types of breaks or boundaries in a line of Unicode text can include

- Boundaries of characters (treating surrogate pairs as a single character). 
-  Boundaries of character clusters. A cluster is a group of characters that should be treated as single text element for editing operations such as cursor movement. Typically this includes groups such as a base character followed by a sequence of combining characters, for example, a Hangul syllable represented as a sequence of conjoining jamo characters or an Indic consonant cluster. 
-  Boundaries of words. This can be used to determine what to highlight as the result of a double-click. 
-  Potential line break locations. 

### Special Considerations

This function can move memory.

## Parameters

- `locale`: A valid `LocaleRef` representing a specific locale, or pass `NULL` to request the default system locale. You can supply the value `kUnicodeTextBreakClass` in the `opClass` parameter of the Locales Utilities functions `LocaleOperationCountLocales` and `LocaleOperationGetLocales` to obtain the locales available for finding text boundaries on the current system. 
- `opVariant`: A `LocaleOperationVariant` value identifying a text-break operation variant within the locale specified in the `locale` parameter. You can also pass 0 to request the default text-break variant for any locale. To obtain the varieties of locale-specific text-break variants that are currently available, you can supply the value `kUnicodeTextBreakClass` in the `opClass` parameter of the Locales Utilities functions `LocaleOperationCountLocales` and `LocaleOperationGetLocales`. 
- `breakTypes`: A `UCTextBreakType` value specifying each type of text boundary that the text-break locator should support. You do not need to create a text-break locator solely for the `BreakChar` type; it is locale-independent and automatically supported by the function [`UCFindTextBreak`](./api-1390429-ucfindtextbreak.md). If `BreakChar` is the only type for which you call the `UCCreateTextBreakLocator` function, on return the `breakRef` parameter returns a `NULL` value (with no error). 
- `breakRef`: A pointer to a value of type `TextBreakLocatorRef`. On return, the `TextBreakLocatorRef` value contains a valid reference to a new text-break locator object. 

## See Also

### Identifying Unicode Text Boundaries
- [UCFindTextBreak](./api-1390429-ucfindtextbreak.md)
  Uses locale-specific text-break information to find boundaries in Unicode text.
- [UCDisposeTextBreakLocator](./api-1390419-ucdisposetextbreaklocator.md)
  Disposes a text-break locator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390362-uccreatetextbreaklocator)*