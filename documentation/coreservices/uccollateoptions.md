# UCCollateOptions

**Framework**: Core Services  
**Kind**: tdef

Specifies options for Unicode string comparison.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
typealias UCCollateOptions = UInt32
```

#### Discussion

For a description of the `UCCollateOptions` values, see [`Standard Options Mask`](carbon_core/unicode_utilities/1390444-standard_options_mask.md).

## Topics

### Constants
- [var kUCCollateComposeInsensitiveMask: Int](kuccollatecomposeinsensitivemask.md)
- [var kUCCollateWidthInsensitiveMask: Int](kuccollatewidthinsensitivemask.md)
- [var kUCCollateCaseInsensitiveMask: Int](kuccollatecaseinsensitivemask.md)
  If the corresponding bit is set, then uppercase and titlecase characters are treated as equivalent to the corresponding lowercase characters.
- [var kUCCollateDiacritInsensitiveMask: Int](kuccollatediacritinsensitivemask.md)
  If the corresponding bit is set, then characters with diacritics are treated as equivalent to the corresponding characters without diacritics.
- [var kUCCollatePunctuationSignificantMask: Int](kuccollatepunctuationsignificantmask.md)
- [var kUCCollateDigitsOverrideMask: Int](kuccollatedigitsoverridemask.md)
- [var kUCCollateDigitsAsNumberMask: Int](kuccollatedigitsasnumbermask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/uccollateoptions)*