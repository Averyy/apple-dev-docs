# ChartData.ChartDataSource

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The stated source of a chart’s values.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string ChartData.ChartDataSource
```

## Discussion

It’s recorded for provenance only: the grid in `rows` is what is read, whatever this value is.

This value takes one of the following forms:

- `chart_data_grid`: The chart’s data is the grid carried in `rows`. This is the only supported source, and the only value ever written.
- `table_formula_references`: Reserved for data drawn from table formula references and expressions. Not supported, and never written.
- `uninitialized`: A value for a chart whose data source hasn’t been set. It’s never written and, like every other value of this property, has no effect: the grid in `rows` is used either way.

## See Also

### Enumerations
- [type ChartData.ChartDataValue](./chartdata.chartdatavalue.md)
  A single value in the chart’s data grid.
- [type ChartData.PlotDirection](./chartdata.plotdirection.md)
  The direction in which the data grid is read to produce the chart’s series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/chartdata.chartdatasource)*