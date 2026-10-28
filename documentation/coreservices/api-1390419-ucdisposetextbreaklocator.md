# UCDisposeTextBreakLocator

**Framework**: Core Services  
**Kind**: func  
**Role**: Function

Disposes a text-break locator object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use CFStringTokenizer (for locale-sensitive word, line, paragraph, and sentence breaks) and CFStringGetRangeOfComposedCharactersAtIndex (for cluster breaks) instead.

## Declaration

```c
OSStatus UCDisposeTextBreakLocator(TextBreakLocatorRef *breakRef);
```

## Return Value

A result code.  This function can return `paramErr`, for example, if the `breakRef` parameter is `NULL`.

## Discussion

To find boundaries in Unicode text, you must supply locale and text-break specifications to the function  [`UCFindTextBreak`](./api-1390429-ucfindtextbreak.md). You provide this information by means of a text-break locator object, created via the function  [`UCCreateTextBreakLocator`](./api-1390362-uccreatetextbreaklocator.md). When finished with the text-break locator object, you should dispose of it using the function `UCDisposeTextBreakLocator`. 

## Parameters

- `breakRef`: A reference to a valid text-break locator object. The `UCDisposeTextBreakLocator` function sets `*breakRef` to `NULL`. 

## See Also

### Identifying Unicode Text Boundaries
- [UCCreateTextBreakLocator](./api-1390362-uccreatetextbreaklocator.md)
  Creates an object encapsulating locale and text-break information, for the purpose of finding boundaries in Unicode text.
- [UCFindTextBreak](./api-1390429-ucfindtextbreak.md)
  Uses locale-specific text-break information to find boundaries in Unicode text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1390419-ucdisposetextbreaklocator)*