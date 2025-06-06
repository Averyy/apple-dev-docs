# kUCCollateDigitsAsNumberMask

**Framework**: Core Services  
**Kind**: data

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var kUCCollateDigitsAsNumberMask: Int { get }
```

#### Discussion

If the corresponding bit is set (and if the bit corresponding to `kUCCollateDigitsOverrideMask` is also set), then numeric substrings up to six digits long are collated by their numeric value—that is, they are treated as a single text element whose primary weight depends on the numeric value of the digit string. This primary weight will be greater than the weight of any valid Unicode character, but less than the primary weight of any unassigned Unicode character. For example, this will result in “Chapter 9” sorting before “Chapter 10.” Currently, these digit strings can include digits with numeric value 0-9 in any script (excluding the ideographic characters for 1-9). If the bit is clear, digits are treated like other characters for sorting. Numeric substrings longer than 6 digits are always treated as normal characters. This option is available with Mac OS 9 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreservices/kuccollatedigitsasnumbermask)*