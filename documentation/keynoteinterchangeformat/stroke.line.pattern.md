# Stroke.Line.Pattern

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The pattern that the reader uses to draw a stroke: solid, one of the dash styles, or one of the brush styles.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Stroke.Line.Pattern
```

## Discussion

`round_dash` also rounds the line’s caps and joins, and a dashed line with round caps is written as `round_dash` regardless of its dash pattern. Without round caps, a dash pattern that doesn’t match one of these cases is written as `short_dash`.

This value takes one of the following forms:

- `calligraphy`: A line that appears to be drawn with a calligraphy pen. Shown in Keynote as Calligraphy.
- `chalk`: A line that appears to be drawn with a piece of chalk pulled along a chalkboard. Shown in Keynote as Chalk.
- `dry_brush`: A line that appears to be painted with a dry brush on paper. Shown in Keynote as “Dry brush.”
- `feathered_brush`: A line that appears to be painted with a feathered brush on paper. Shown in Keynote as “Feathered brush.”
- `long_dash`: A dashed line with long dashes. Shown in Keynote as “Long dash.”
- `medium_dash`: A dashed line with medium dashes. Shown in Keynote as “Medium dash.”
- `pen`: A line that appears to be drawn with a pen that has uneven ink flow. Shown in Keynote as Pen.
- `round_dash`: A dotted line, drawn with small round dashes. Shown in Keynote as “Rounded dash.”
- `short_dash`: A dashed line with short dashes. Shown in Keynote as “Short dash.”
- `solid`: A solid line. Shown in Keynote as Solid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stroke.line.pattern)*