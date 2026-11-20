# LineSpacingType.LineSpacingKindType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A kind of line spacing.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string LineSpacingType.LineSpacingKindType
```

## Discussion

This value takes one of the following forms:

- `between`: `value` points of space are added between lines, in addition to the natural line height.
- `exact`: Lines are exactly `value` points apart.
- `maximum`: Lines are at most `value` points apart.
- `minimum`: Lines are at least `value` points apart.
- `relative`: `value` is a multiple of the natural line height; 1.0 is single-spaced. Shown in Keynote as Lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/linespacingtype.linespacingkindtype)*