# typeStyledText

**Framework**: Core Services  
**Kind**: econst  
**Role**: Enumeration Case

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```c
typeStyledText = 'STXT'
```

## Discussion

Text that includes style information.

Styled text is stored as a record, in which the styles have the key `'ksty'` and the plain text is has the key '`ktxt'`. You can use this information to extract plain text from styled text without coercion.

However, getting rid of the style information, with or without coercion, may corrupt the text, since the styles imply what encoding to use. In fact, use of `typeText` and `typeStyledText` are not recommended, starting with macOS, because they are not safe with international characters—you should use one of the Unicode text types instead.

For important information, see the Version Notes section of the [typeUnicodeText](../api-1542918-typeunicodetext.md) enum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1556396-anonymous/typestyledtext)*