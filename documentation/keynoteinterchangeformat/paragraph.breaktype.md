# Paragraph.BreakType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The break that ends a paragraph.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Paragraph.BreakType
```

## Discussion

It decides where the following text resumes: the next line, the next column, or the next page.

This value takes one of the following forms:

- `column`: Column break.
- `none`: No terminating break; only the last paragraph of the text can lack one, and there `none` is equivalent to omitting `break_type`. On any earlier paragraph a normal paragraph break is inserted instead.
- `nontopic`: A paragraph break that prevents topic or list labeling.
- `page`: Page break.
- `para`: Paragraph break.
- `section`: Section break. Keynote has no sections: `section` is always replaced by a page break, which in Keynote only ends the paragraph. Use `para` instead.

## See Also

### Enumerations
- [type Paragraph.Constituent](./paragraph.constituent.md)
  An element of a paragraph’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/paragraph.breaktype)*