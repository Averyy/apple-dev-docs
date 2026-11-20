# ChartData.PlotDirection

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The direction in which the data grid is read to produce the chart’s series.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartData.PlotDirection
```

## Discussion

This value takes one of the following forms:

- `columns_as_series`: Each column of the grid is a series, so `column_labels` name the series and `row_labels` name the categories.
- `rows_as_series`: Each row of the grid is a series, so `row_labels` name the series and `column_labels` name the categories.

## See Also

### Enumerations
- [type ChartData.ChartDataSource](./chartdata.chartdatasource.md)
  The stated source of a chart’s values.
- [type ChartData.ChartDataValue](./chartdata.chartdatavalue.md)
  A single value in the chart’s data grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartdata.plotdirection)*