# ChartSeries.SeriesSymbolType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The shape of the data symbol drawn at each of a series’ data points.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartSeries.SeriesSymbolType
```

## Discussion

It also sets whether data symbols are drawn at all: `none` turns them off, and any other case turns them on. Only a series that draws an editable data symbol uses it; a bubble series doesn’t, because its circles are sized from the data.

This value takes one of the following forms:

- `circle`
- `diamond`
- `none`
- `plus`
- `square`
- `triangle`
- `x`
- `yield`: A triangle pointing the opposite way from `triangle`, apex toward the bottom.

## See Also

### Enumerations
- [type ChartSeries.ConnectionLineType](./chartseries.connectionlinetype.md)
  The style of the line drawn through a series’ data points.
- [type ChartSeries.FillReuseRule](./chartseries.fillreuserule.md)
  A rule that reuses one of a series’ own colors in place of an explicit fill.
- [type ChartSeries.MixedSeriesType](./chartseries.mixedseriestype.md)
  The shape a single series takes on a mixed or two-axis chart.
- [type ChartSeries.SeriesValueLabelPosition](./chartseries.seriesvaluelabelposition.md)
  The position of a data point’s value label, for a series that shows value labels.
- [type ChartSeries.ValueLabelsSelection](./chartseries.valuelabelsselection.md)
  The values of a data point that appear in its value label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartseries.seriessymboltype)*