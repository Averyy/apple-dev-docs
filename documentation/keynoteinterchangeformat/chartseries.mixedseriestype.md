# ChartSeries.MixedSeriesType

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The shape a single series takes on a mixed or two-axis chart.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartSeries.MixedSeriesType
```

## Discussion

Each series on these charts can take a different shape, and these are the only chart types that read this value. The choice also determines which of the series’ other style properties apply, since a series drawn as columns has neither data symbols nor a connecting line.

## See Also

### Enumerations
- [type ChartSeries.ConnectionLineType](./chartseries.connectionlinetype.md)
  The style of the line drawn through a series’ data points.
- [type ChartSeries.FillReuseRule](./chartseries.fillreuserule.md)
  A rule that reuses one of a series’ own colors in place of an explicit fill.
- [type ChartSeries.SeriesSymbolType](./chartseries.seriessymboltype.md)
  The shape of the data symbol drawn at each of a series’ data points.
- [type ChartSeries.SeriesValueLabelPosition](./chartseries.seriesvaluelabelposition.md)
  The position of a data point’s value label, for a series that shows value labels.
- [type ChartSeries.ValueLabelsSelection](./chartseries.valuelabelsselection.md)
  The values of a data point that appear in its value label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartseries.mixedseriestype)*