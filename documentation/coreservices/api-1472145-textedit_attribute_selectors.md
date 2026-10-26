# TextEdit Attribute Selectors

**Framework**: Core Services  
**Kind**: enum  
**Role**: Enumeration

Specify feature availability information for TextEdit.

**Availability**:
- Mac Catalyst 17.0+
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [gestaltTEAttr](./api-1472145-textedit_attribute_selectors/gestaltteattr.md)
  The `Gestalt` selector you pass to determine whichTextEdit attributes are present.
- [gestaltTEHasGetHiliteRgn](./api-1472145-textedit_attribute_selectors/gestalttehasgethilitergn.md)
  If true, TextEdit has `TEGetHiliteRgn`.
- [gestaltTESupportsInlineInput](./api-1472145-textedit_attribute_selectors/gestalttesupportsinlineinput.md)
  If `true`, TextEdit does Inline Input.
- [gestaltTESupportsTextObjects](./api-1472145-textedit_attribute_selectors/gestalttesupportstextobjects.md)
  If `true`, TextEdit does Text Objects.
- [gestaltTEHasWhiteBackground](./api-1472145-textedit_attribute_selectors/gestalttehaswhitebackground.md)
  If `true`, TextEdit supports overriding the `TERec`' data structure background field to white.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/1472145-textedit_attribute_selectors)*