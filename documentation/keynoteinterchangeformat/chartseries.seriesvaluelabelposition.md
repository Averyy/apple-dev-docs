# ChartSeries.SeriesValueLabelPosition

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The position of a data point’s value label, for a series that shows value labels.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartSeries.SeriesValueLabelPosition
```

## Discussion

Each chart type uses only the placements that suit it and replaces any other with one it supports. A pie wedge or donut segment, for instance, keeps `inside` and `outside`, and anything else (`auto` included) comes out as the automatic centered placement.

## See Also

### Enumerations
- [type ChartSeries.ConnectionLineType](./chartseries.connectionlinetype.md)
  The style of the line drawn through a series’ data points.
- [type ChartSeries.FillReuseRule](./chartseries.fillreuserule.md)
  A rule that reuses one of a series’ own colors in place of an explicit fill.
- [type ChartSeries.MixedSeriesType](./chartseries.mixedseriestype.md)
  The shape a single series takes on a mixed or two-axis chart.
- [type ChartSeries.SeriesSymbolType](./chartseries.seriessymboltype.md)
  The shape of the data symbol drawn at each of a series’ data points.
- [type ChartSeries.ValueLabelsSelection](./chartseries.valuelabelsselection.md)
  The values of a data point that appear in its value label.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartseries.seriesvaluelabelposition)*