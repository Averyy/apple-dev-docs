# ChartData.ChartDataValue

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

A single value in the chart’s data grid.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
(ChartData.ChartDataValue.date | ChartData.ChartDataValue.duration | ChartData.ChartDataValue.number | string("empty")) ChartData.ChartDataValue
```



**Allowed Types**: `ChartData.ChartDataValue.date`, `ChartData.ChartDataValue.duration`, `ChartData.ChartDataValue.number`, `string("empty")`

## Discussion

A value is a number, a date, or a duration; a cell holding anything else, text included, is read as empty.

This value takes one of the following forms:

- `date`: A cell holding a date.
- `duration`: A cell holding a length of time.
- `empty`: An empty cell. Any cell that doesn’t hold a number, a date, or a duration is written as `empty`.
- `number`: A cell holding a number.

## Topics

### Dictionaries
- [object ChartData.ChartDataValue.date](./chartdata.chartdatavalue/date.md)
  A cell holding a date.
- [object ChartData.ChartDataValue.duration](./chartdata.chartdatavalue/duration.md)
  A cell holding a length of time.
- [object ChartData.ChartDataValue.number](./chartdata.chartdatavalue/number.md)
  A cell holding a number.

## See Also

### Enumerations
- [type ChartData.ChartDataSource](./chartdata.chartdatasource.md)
  The stated source of a chart’s values.
- [type ChartData.PlotDirection](./chartdata.plotdirection.md)
  The direction in which the data grid is read to produce the chart’s series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartdata.chartdatavalue)*