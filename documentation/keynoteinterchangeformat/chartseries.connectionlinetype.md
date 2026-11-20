# ChartSeries.ConnectionLineType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The style of the line drawn through a series’ data points.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartSeries.ConnectionLineType
```

## Discussion

It also sets whether a line is drawn at all: `none` removes the line rather than falling back to a default. Only a series that joins its points with a line uses it; elsewhere the value is ignored and isn’t written back out.

## See Also

### Enumerations
- [type ChartSeries.FillReuseRule](./chartseries.fillreuserule.md)
  A rule that reuses one of a series’ own colors in place of an explicit fill.
- [type ChartSeries.MixedSeriesType](./chartseries.mixedseriestype.md)
  The shape a single series takes on a mixed or two-axis chart.
- [type ChartSeries.SeriesSymbolType](./chartseries.seriessymboltype.md)
  The shape of the data symbol drawn at each of a series’ data points.
- [type ChartSeries.SeriesValueLabelPosition](./chartseries.seriesvaluelabelposition.md)
  The position of a data point’s value label, for a series that shows value labels.
- [type ChartSeries.ValueLabelsSelection](./chartseries.valuelabelsselection.md)
  The values of a data point that appear in its value label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartseries.connectionlinetype)*