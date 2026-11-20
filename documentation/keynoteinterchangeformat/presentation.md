# Presentation

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A document’s root object, which describes one Keynote presentation.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Presentation
```

## Mentions

- [Understanding Keynote Interchange Format structure](./understanding-keynote-interchange-format-structure.md)

## Topics

### Slides
- [object Slide](./slide.md)
  A slide in a presentation.
- [object SlideBackground](./slidebackground.md)
  The background of a slide.
- [object SlideLayout](./slidelayout.md)
  A slide layout in a Keynote theme.
- [object SlideObject](./slideobject.md)
  An object on a slide or slide layout, with slide-specific information about it.
### Positions
- [object Geometry](./geometry.md)
  The bounding box in which an object is positioned.
- [object Offset](./offset.md)
  A horizontal and vertical displacement, in points.
- [object Position](./position.md)
  A point, in points, in whichever coordinate space the property using it defines, measured downward from that space’s top-left corner.
- [object Insets](./insets.md)
  Space reserved along each edge of an area, in points.
- [object TabStopType](./tabstoptype.md)
  A tab stop.
- [type VerticalAlignmentType](./verticalalignmenttype.md)
  Vertical alignment of text within a container.
### Shapes
- [object Shape](./shape.md)
  A path with a fill and a stroke.
- [object Rect](./rect.md)
  An axis-aligned rectangle in whichever coordinate space the property using it defines.
- [object Path](./path.md)
  A path that traces the outline of a shape or of an image’s mask.
- [type Stroke](./stroke.md)
  A stroke drawn along a path, such as a border around an object.
- [object ConnectionLine](./connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.
### Fills
- [type Fill](./fill.md)
  A style that fills an area with exactly one of a solid color, a gradient, or an image.
### Colors
- [object Color](./color.md)
  A color that the reader uses as part of a displayed object, in one of the forms the format supports.
### Numbers
- [object NumberFormatType](./numberformattype.md)
  A format for numbers, such as those in a numbered list.
### Text
- [type Text](./text.md)
  A body of text, such as the text of a text box, a table cell, or a slide’s presenter notes.
- [object TextRun](./textrun.md)
  A run of text with a single character style.
- [object TextStroke](./textstroke.md)
  A stroke for text, or a special value for no stroke.
- [object Textbox](./textbox.md)
  A container for text that someone places directly on a slide or slide layout.
- [object Paragraph](./paragraph.md)
  A paragraph of text.
- [object ParagraphProperties](./paragraphproperties.md)
  The paragraph-level properties of text.
- [object CharacterProperties](./characterproperties.md)
  The character-level properties of text.
- [type WritingDirectionType](./writingdirectiontype.md)
  The writing direction of the text.
- [type LineEnd](./lineend.md)
  A decoration drawn at the end of a connection line or of a shape’s open path, such as an arrowhead.
- [object LineSpacingType](./linespacingtype.md)
  The spacing between lines of text.
- [object LayoutProperties](./layoutproperties.md)
  The text layout properties of a shape style or a column of text.
### Links
- [type Hyperlink](./hyperlink.md)
  A clickable link attached to text.
### Canvas
- [type CanvasObject](./canvasobject.md)
  The identity, placement, and accessibility properties shared by objects you can place on a slide, in a group, or inline in text.
### Styling
- [object KeynoteTheme](./keynotetheme.md)
  The Keynote theme a presentation is based on.
- [object Stylesheet](./stylesheet.md)
  A collection of styles to use as presets for various objects in a document.
### Shadows
- [type Shadow](./shadow.md)
  The kind of shadow cast by an object, or `none` for no shadow.
- [object ContactShadow](./contactshadow.md)
  A shadow whose silhouette pools under the object’s bottom edge as though the object were standing on a ground plane.
- [object CurvedShadow](./curvedshadow.md)
  A shadow whose silhouette curls away from the object, as if it were a page lifting off the surface rather than lying flat.
- [object DropShadow](./dropshadow.md)
  A shadow whose silhouette appears as though cast by a light source facing down toward the plane of the object.
- [object Reflection](./reflection.md)
  A mirrored copy of the object that the reader drew directly below it on a ground plane aligned to the horizontal axis, fading out with distance.
### Lists
- [object ListLevelType](./listleveltype.md)
  One nesting level of a list style.
- [object ListProperties](./listproperties.md)
  The properties of a list style.
- [type ListLabelType](./listlabeltype.md)
  The kind of label shown at a list level.
### Tables
- [object Table](./table.md)
  A table of cells, nested two levels deep.
- [object Table.TransformationInfo](./table.transformationinfo.md)
  Information about how the reader derives a table.
- [type ColumnMetrics](./columnmetrics.md)
  The arrangement of a text area into columns, and the width of the gutters between them.
### Charts
- [type Chart](./chart.md)
  An object that plots a grid of data in a visual style such as column, pie, or scatter.
- [type ChartAxisCommon](./chartaxiscommon.md)
  The properties every chart axis shares, flattened into both the category axis and the value axis.
- [type ChartCommon](./chartcommon.md)
  The properties shared by every kind of chart.
- [type ChartLabelFormatting](./chartlabelformatting.md)
  The formatting of a chart element’s numeric labels.
- [object ChartCategoryAxis](./chartcategoryaxis.md)
  The axis along which a chart’s categories are laid out, on the chart types that have one.
- [object ChartData](./chartdata.md)
  The chart’s data as a grid of cells, together with how that grid maps onto the chart.
- [object ChartLegend](./chartlegend.md)
  The legend of a chart.
- [object ChartSeries](./chartseries.md)
  The appearance and label formatting of one of a chart’s data series.
- [object ChartValueAxis](./chartvalueaxis.md)
  A numeric axis that a chart’s values are measured against.
- [object AreaChart](./areachart.md)
  A 2D area chart.
- [object Area3DChart](./area3dchart.md)
  A 3D area chart.
- [object StackedAreaChart](./stackedareachart.md)
  A 2D stacked area chart.
- [object StackedArea3DChart](./stackedarea3dchart.md)
  A 3D stacked area chart.
- [object BarChart](./barchart.md)
  A 2D bar chart.
- [object Bar3DChart](./bar3dchart.md)
  A 3D horizontal bar chart.
- [object BarInteractiveChart](./barinteractivechart.md)
  An interactive horizontal bar chart, which shows one data set at a time.
- [object StackedBarChart](./stackedbarchart.md)
  A 2D stacked bar chart.
- [object StackedBar3DChart](./stackedbar3dchart.md)
  A 3D stacked horizontal bar chart.
- [object ColumnChart](./columnchart.md)
  A 2D column chart.
- [object Column3DChart](./column3dchart.md)
  A 3D vertical column chart.
- [object ColumnInteractiveChart](./columninteractivechart.md)
  An interactive vertical column chart, which shows one data set at a time.
- [object StackedColumnChart](./stackedcolumnchart.md)
  A 2D stacked column chart.
- [object StackedColumn3DChart](./stackedcolumn3dchart.md)
  A 3D stacked vertical column chart.
- [object LineChart](./linechart.md)
  A 2D line chart.
- [object Line3DChart](./line3dchart.md)
  A 3D line chart.
- [object PieChart](./piechart.md)
  A pie chart.
- [object Pie3DChart](./pie3dchart.md)
  A 3D pie chart.
- [object DonutChart](./donutchart.md)
  A donut chart.
- [object BubbleChart](./bubblechart.md)
  A bubble chart.
- [object BubbleInteractiveChart](./bubbleinteractivechart.md)
  An interactive bubble chart, which shows one data set at a time.
- [object ScatterChart](./scatterchart.md)
  A scatter chart.
- [object ScatterInteractiveChart](./scatterinteractivechart.md)
  An interactive scatter chart, which shows one data set at a time.
- [object RadarChart](./radarchart.md)
  A radar chart.
- [object MixedChart](./mixedchart.md)
  A mixed chart, which draws individual series as columns, lines, or areas.
- [object TwoAxisChart](./twoaxischart.md)
  A two-axis chart, which is a category chart with two independent value scales.
- [type CategoryComparisonChart](./categorycomparisonchart.md)
  The axes shared by every chart type that compares categories against a value scale.
- [type CorrelationChart](./correlationchart.md)
  The axes shared by every chart type that plots one value scale against another.
- [object GenericCategoryComparisonChart](./genericcategorycomparisonchart.md)
  An object with only the properties of CategoryComparisonChart.
- [object GenericChartAxisCommon](./genericchartaxiscommon.md)
  An object with only the properties of ChartAxisCommon.
- [object GenericChartCommon](./genericchartcommon.md)
  An object with only the properties of ChartCommon.
- [object GenericChartLabelFormatting](./genericchartlabelformatting.md)
  An object with only the properties of ChartLabelFormatting.
- [object GenericCorrelationChart](./genericcorrelationchart.md)
  An object with only the properties of CorrelationChart.
### Media
- [object Audio](./audio.md)
  A sound attached to a slide.
- [object Image](./image.md)
  A picture defined by a resource with optional styling.
- [object Movie](./movie.md)
  A movie or animated image defined by a resource with optional styling.
- [object PlaybackOptions](./playbackoptions.md)
  Options controlling playback of media.
- [object Duration](./duration.md)
  A length of time.
### Resources
- [type Resource](./resource.md)
  The data used for image, movie, and audio media, and for image fills and image bullets.
### Titles
- [object TitleOwning](./titleowning.md)
  The properties for defining a title that an object can display.
- [object CaptionOwning](./captionowning.md)
  The properties for defining an optional caption an object can display.
- [object PlaceableTitleOwning](./placeabletitleowning.md)
  The properties for defining a title an object can display, positioned above or below the object.
- [object GenericTitleOwning](./generictitleowning.md)
  An object with only the properties of title owning.
- [object GenericCaptionOwning](./genericcaptionowning.md)
  An object with only the properties of caption owning.
- [object GenericPlaceableTitleOwning](./genericplaceabletitleowning.md)
  A stand-in for an object with a free-standing title label, when the reader doesn’t recognize its kind.
### Common types
- [object Group](./group.md)
  An ordered set of objects that behave as one when selected, moved, or transformed.
- [object Size](./size.md)
  A width and height in whichever coordinate space the property using it defines.
- [object Label](./label.md)
  Styled text that the reader uses as a title or caption on an object.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.presentation`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `theme` (KeynoteTheme): The theme that supplies the presentation’s slide layouts, styles, and backgrounds. If it’s absent, the default is Keynote’s White theme.
- `slide_size` (Size): The size of every slide in the presentation, in points. If it’s absent, a reader must supply the size, for example, from the theme, or reject the document.
- `slides` ([Slide]) *(required)*: The presentation’s slides, in presentation order. Grouping in the slide navigator is expressed by each slide’s `Slide.depth` rather than by nesting arrays. Validation: minimum `1` item.
- `stylesheet` (Stylesheet): The presentation’s named styles: character, paragraph, list, line, shape, text box, image, movie, and table styles. The presentation’s objects and text can refer to these by their preset identifier. If this value is absent, Keynote uses the theme’s styles.

## See Also

### File format
- [object Manifest](./manifest.md)
  An object that declares which version of Keynote Interchange Format a .keyx file uses.
- [object Preset](./preset.md)
  A reusable, named set of properties that other objects inherit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/presentation)*