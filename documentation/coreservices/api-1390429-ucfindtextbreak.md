# UCFindTextBreak

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Uses locale-specific text-break information to find boundaries in Unicode text.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use CFStringTokenizer (for locale-sensitive word, line, paragraph, and sentence breaks) and CFStringGetRangeOfComposedCharactersAtIndex (for cluster breaks) instead.

## Declaration

```c
OSStatus UCFindTextBreak(TextBreakLocatorRef breakRef, UCTextBreakType breakType, UCTextBreakOptions options, const UniChar *textPtr, UniCharCount textLength, UniCharArrayOffset startOffset, UniCharArrayOffset *breakOffset);
```

## Return Value

A result code.  The text-break locator referenced by the `breakRef` parameter must support the type of boundary specified in the `breakType` parameter; otherwise, the function returns `kUCTextBreakLocatorMissingType`.

## Discussion

The `UCFindTextBreak` function starts from a specified offset in a text buffer, and then proceeds forward or backward (as requested) until it finds the next text boundary of a particular locale-specific type, using a given set of options. The different types of breaks or boundaries in a line of Unicode text can include

- Boundaries of characters (treating surrogate pairs as a single character). 
-  Boundaries of character clusters. A cluster is a group of characters that should be treated as single text element for editing operations such as cursor movement. Typically this includes groups such as a base character followed by a sequence of combining characters, for example, a Hangul syllable represented as a sequence of conjoining jamo characters or an Indic consonant cluster. 
-  Boundaries of words. This can be used to determine what to highlight as the result of a double-click. 
-  Potential line break locations. 

Finding boundaries of characters is a locale-independent operation, and support for it is built directly into the `UCFindTextBreak` function. If that is the only type of text boundary that you wish to locate, it is not necessary to call `UCCreateTextBreakLocator` and create a text-break locator object.

When finished with the text-break locator object, dispose it using the function  [`UCDisposeTextBreakLocator`](./api-1390419-ucdisposetextbreaklocator.md). 

## Parameters

- `breakRef`: A valid reference to a text-break locator object. If the type of boundary specified by the `breakType` parameter is `BreakChar`, you can pass `NULL`. You use the function [`UCCreateTextBreakLocator`](./api-1390362-uccreatetextbreaklocator.md) to obtain a text-break locator object reference. If non-`NULL`, the text-break locator object must support the type of boundary specified in the `breakType` parameter. 
- `breakType`: A value of type `UCTextBreakType`, with exactly one bit set to specify a single type of boundary to be located. Since support for finding character boundaries is locale-independent and built into the `UCFindTextBreak` function, if you specify `BreakChar` as the type of boundary, then the `breakRef` parameter is ignored and may be `NULL`. 
- `options`: A `UCTextBreakOptions` value to specify the operation of the `UCFindTextBreak` function. You can use text-break locator options to control some location-independent aspects of a text-boundary search. Note that if you do not specify any `UCTextBreakOptions` values, `UCFindTextBreak` searches forward, but assumes that the `startOffset` value refers to the character preceding the offset rather than the one at the offset. This can result in `UCFindTextBreak` returning an offset that is equal to the start offset. 
- `textPtr`: A pointer to the initial character of the Unicode string to search. 
- `textLength`: The total count of Unicode characters in the string to search. 
- `startOffset`: A `UniCharArrayOffset` value specifying the offset from which `UCFindTextBreak` is to begin searching for the next text boundary of the type specified in the `breakType` parameter. If `startOffset == 0` then `kUCTextBreakLeadingEdgeMask` must be set in the options parameter; if `startOffset == textLength` then `kUCTextBreakLeadingEdgeMask` must not be set. 
- `breakOffset`: A pointer to a `UniCharArrayOffset` value. On return, the value pointed to by the `breakOffset` parameter is set to the offset of the text boundary located by `UCFindTextBreak`. In normal usage (when exactly one of `kUCTextBreakLeadingEdgeMask` and `kUCTextBreakGoBackwardsMask` are set), the result returned in `breakOffset` is not equal to that supplied in the `startOffset` parameter unless an error occurs (and the function result is other than `noErr`). However, when `kUCTextBreakLeadingEdgeMask` and `kUCTextBreakGoBackwardsMask` are both set or both clear, the result produced in `breakOffset` can be equal to the value of `startOffset`.

## See Also

### Identifying Unicode Text Boundaries
- [UCCreateTextBreakLocator](./api-1390362-uccreatetextbreaklocator.md)
  Creates an object encapsulating locale and text-break information, for the purpose of finding boundaries in Unicode text.
- [UCDisposeTextBreakLocator](./api-1390419-ucdisposetextbreaklocator.md)
  Disposes a text-break locator object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390429-ucfindtextbreak)*