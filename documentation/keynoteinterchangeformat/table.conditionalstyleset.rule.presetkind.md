# Table.ConditionalStyleSet.Rule.PresetKind

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The built-in conditional-highlighting preset that a rule represents.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Table.ConditionalStyleSet.Rule.PresetKind
```

## Discussion

It lets readers associate the rule with a known visual style.

This value takes one of the following forms:

- `blue_fill`: Blue cell fill with white text.
- `blue_text`: Blue text preset.
- `bold`: Bold text preset.
- `custom`: A fully custom style, set entirely by `cell_style` and `text_style`.
- `gray_text`: Gray text preset.
- `green_fill`: Green cell fill with white text.
- `green_text`: Green text preset.
- `italics`: Italic text preset.
- `orange_fill`: Orange cell fill with white text.
- `red_fill`: Red cell fill with white text.
- `red_text`: Red text preset.
- `teal_fill`: Teal cell fill with white text.
- `yellow_fill`: Yellow cell fill with white text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.conditionalstyleset.rule.presetkind)*